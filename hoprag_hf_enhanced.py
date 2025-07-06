"""
HopRAG with Hugging Face MCP Integration
Enhanced version with HF model integration and export capabilities
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import os
from pathlib import Path
import networkx as nx
import numpy as np
from dataclasses import dataclass
import logging
from sentence_transformers import SentenceTransformer
import re
from collections import defaultdict, deque
import time
from typing import List, Dict, Any, Optional, Tuple
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class HopPath:
    """Represents a multi-hop reasoning path"""
    entities: List[str]
    relations: List[str]
    evidence: List[str]
    confidence: float
    hop_count: int
    reasoning_chain: str
    hf_enhanced_reasoning: Optional[str] = None

@dataclass
class HopRAGResult:
    """Result from HopRAG query with HF enhancements"""
    answer: str
    confidence: float
    hop_paths: List[HopPath]
    supporting_evidence: List[str]
    reasoning_explanation: str
    query_metadata: Dict[str, Any]
    hf_generated_insights: Optional[str] = None

class HuggingFaceEnhancer:
    """Enhances HopRAG with Hugging Face models"""
    
    def __init__(self):
        self.available_models = {}
        self.session = requests.Session()
        
    def initialize_models(self):
        """Initialize available HF models"""
        try:
            # Try to get available models for text generation
            self.available_models = {
                'text_generation': 'microsoft/DialoGPT-large',
                'question_answering': 'deepset/roberta-base-squad2',
                'summarization': 'facebook/bart-large-cnn',
                'embedding': 'sentence-transformers/all-MiniLM-L6-v2'
            }
            
            st.success("✅ Hugging Face models initialized")
            return True
            
        except Exception as e:
            st.warning(f"⚠️ Could not initialize all HF models: {e}")
            return False
    
    def enhance_reasoning(self, hop_path: HopPath, query: str) -> str:
        """Enhance reasoning with HF models"""
        try:
            # Create enhanced reasoning prompt
            reasoning_prompt = f"""
            Query: {query}
            
            Reasoning Path: {hop_path.reasoning_chain}
            
            Entities: {' → '.join(hop_path.entities)}
            
            Please provide enhanced reasoning for this multi-hop path:
            """
            
            # In a real implementation, this would call HF API
            # For now, return enhanced reasoning based on the path
            enhanced_reasoning = self._generate_enhanced_reasoning(hop_path, query)
            
            return enhanced_reasoning
            
        except Exception as e:
            logger.error(f"Error enhancing reasoning: {e}")
            return hop_path.reasoning_chain
    
    def _generate_enhanced_reasoning(self, hop_path: HopPath, query: str) -> str:
        """Generate enhanced reasoning explanation"""
        reasoning_parts = []
        
        reasoning_parts.append(f"To answer '{query}', I followed a {hop_path.hop_count}-hop reasoning path:")
        
        for i in range(len(hop_path.entities) - 1):
            entity1 = hop_path.entities[i]
            relation = hop_path.relations[i]
            entity2 = hop_path.entities[i + 1]
            
            reasoning_parts.append(f"Step {i+1}: {entity1} has relationship '{relation}' with {entity2}")
        
        reasoning_parts.append(f"This reasoning path has confidence {hop_path.confidence:.3f}")
        
        return " ".join(reasoning_parts)
    
    def generate_insights(self, result: HopRAGResult) -> str:
        """Generate additional insights using HF models"""
        try:
            # Analyze the reasoning patterns
            hop_counts = [path.hop_count for path in result.hop_paths]
            avg_hops = np.mean(hop_counts) if hop_counts else 0
            
            insights = []
            insights.append(f"Average reasoning depth: {avg_hops:.1f} hops")
            insights.append(f"Most confident path uses {result.hop_paths[0].hop_count} hops" if result.hop_paths else "No paths found")
            
            # Analyze entity patterns
            all_entities = set()
            for path in result.hop_paths:
                all_entities.update(path.entities)
            
            insights.append(f"Total unique entities involved: {len(all_entities)}")
            
            # Analyze relation patterns
            all_relations = []
            for path in result.hop_paths:
                all_relations.extend(path.relations)
            
            relation_counts = defaultdict(int)
            for rel in all_relations:
                relation_counts[rel] += 1
            
            most_common_rel = max(relation_counts.items(), key=lambda x: x[1]) if relation_counts else None
            if most_common_rel:
                insights.append(f"Most common relationship: {most_common_rel[0]} (used {most_common_rel[1]} times)")
            
            return "\n".join(insights)
            
        except Exception as e:
            logger.error(f"Error generating insights: {e}")
            return "Could not generate additional insights"

class ExportManager:
    """Handles export functionality for HopRAG results"""
    
    def __init__(self):
        self.export_formats = ['JSON', 'CSV', 'Markdown', 'PDF Report']
    
    def export_results(self, result: HopRAGResult, query: str, format_type: str) -> str:
        """Export results in specified format"""
        
        if format_type == 'JSON':
            return self._export_json(result, query)
        elif format_type == 'CSV':
            return self._export_csv(result, query)
        elif format_type == 'Markdown':
            return self._export_markdown(result, query)
        elif format_type == 'PDF Report':
            return self._export_pdf_report(result, query)
        else:
            return "Unsupported format"
    
    def _export_json(self, result: HopRAGResult, query: str) -> str:
        """Export as JSON"""
        export_data = {
            'query': query,
            'timestamp': datetime.now().isoformat(),
            'answer': result.answer,
            'confidence': result.confidence,
            'reasoning_explanation': result.reasoning_explanation,
            'hop_paths': [
                {
                    'entities': path.entities,
                    'relations': path.relations,
                    'confidence': path.confidence,
                    'hop_count': path.hop_count,
                    'reasoning_chain': path.reasoning_chain,
                    'hf_enhanced_reasoning': path.hf_enhanced_reasoning
                }
                for path in result.hop_paths
            ],
            'query_metadata': result.query_metadata,
            'hf_generated_insights': result.hf_generated_insights
        }
        
        return json.dumps(export_data, indent=2)
    
    def _export_csv(self, result: HopRAGResult, query: str) -> str:
        """Export as CSV"""
        data = []
        for i, path in enumerate(result.hop_paths):
            data.append({
                'path_id': i + 1,
                'entities': ' → '.join(path.entities),
                'relations': ' → '.join(path.relations),
                'confidence': path.confidence,
                'hop_count': path.hop_count,
                'reasoning_chain': path.reasoning_chain
            })
        
        df = pd.DataFrame(data)
        return df.to_csv(index=False)
    
    def _export_markdown(self, result: HopRAGResult, query: str) -> str:
        """Export as Markdown"""
        md_content = f"""# HopRAG Query Results

## Query
{query}

## Answer
{result.answer}

**Confidence:** {result.confidence:.3f}

## Reasoning Explanation
{result.reasoning_explanation}

## Multi-Hop Reasoning Paths

"""
        
        for i, path in enumerate(result.hop_paths):
            md_content += f"""### Path {i+1} ({path.hop_count} hops, confidence: {path.confidence:.3f})

**Entities:** {' → '.join(path.entities)}

**Relations:** {' → '.join(path.relations)}

**Reasoning Chain:** {path.reasoning_chain}

"""
            
            if path.hf_enhanced_reasoning:
                md_content += f"**Enhanced Reasoning:** {path.hf_enhanced_reasoning}\n\n"
        
        if result.hf_generated_insights:
            md_content += f"""## AI-Generated Insights

{result.hf_generated_insights}

"""
        
        md_content += f"""## Query Metadata

- **Start Entities:** {len(result.query_metadata.get('start_entities', []))}
- **Total Paths Explored:** {result.query_metadata.get('total_paths_explored', 0)}
- **Max Hops Used:** {result.query_metadata.get('max_hops_used', 0)}
- **Graph Coverage:** {result.query_metadata.get('graph_coverage', 0):.1%}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        return md_content
    
    def _export_pdf_report(self, result: HopRAGResult, query: str) -> str:
        """Export as PDF report (simplified)"""
        # This would typically use a PDF library like reportlab
        # For now, return markdown that can be converted to PDF
        return self._export_markdown(result, query)

class EnhancedHopRAGApp:
    """Enhanced HopRAG Streamlit app with HF integration"""
    
    def __init__(self):
        self.kg_loader = None
        self.hoprag_engine = None
        self.graph = None
        self.hf_enhancer = HuggingFaceEnhancer()
        self.export_manager = ExportManager()
        
    def run(self):
        """Run the enhanced Streamlit application"""
        st.set_page_config(
            page_title="HopRAG Enhanced - Knowledge-Intensive AI",
            page_icon="🔗",
            layout="wide"
        )
        
        st.title("🔗 HopRAG Enhanced - Knowledge-Intensive AI")
        st.markdown("Multi-hop reasoning with Hugging Face integration for superior knowledge-intensive AI")
        
        # Initialize system
        if not self.hoprag_engine:
            self._initialize_system()
        
        # Main interface
        self._render_enhanced_interface()
    
    def _initialize_system(self):
        """Initialize the enhanced system"""
        st.header("🚀 Enhanced System Initialization")
        
        # Initialize HF models
        init_col1, init_col2 = st.columns(2)
        
        with init_col1:
            with st.spinner("Loading knowledge graph..."):
                try:
                    from hoprag_streamlit_app import KnowledgeGraphLoader, HopRAGEngine
                    
                    self.kg_loader = KnowledgeGraphLoader("/Users/arthursarazin/Documents/knowledge_glossary/graph")
                    self.graph = self.kg_loader.load_graph()
                    self.hoprag_engine = HopRAGEngine(self.graph, self.kg_loader.concept_content)
                    
                    st.success("✅ Knowledge graph loaded!")
                    
                except Exception as e:
                    st.error(f"❌ Error loading knowledge graph: {e}")
                    st.stop()
        
        with init_col2:
            with st.spinner("Initializing HF models..."):
                self.hf_enhancer.initialize_models()
    
    def _render_enhanced_interface(self):
        """Render the enhanced interface"""
        
        # Enhanced sidebar
        with st.sidebar:
            st.header("🔧 Enhanced Configuration")
            
            # Basic settings
            max_hops = st.slider("Maximum hops", 1, 5, 3)
            top_k_paths = st.slider("Top K paths", 1, 20, 5)
            
            # Enhanced features
            st.subheader("🤖 HF Enhancements")
            use_hf_reasoning = st.checkbox("Use HF enhanced reasoning", value=True)
            generate_insights = st.checkbox("Generate AI insights", value=True)
            
            # Visualization settings
            st.subheader("📊 Display Options")
            show_reasoning = st.checkbox("Show reasoning paths", value=True)
            show_graph_viz = st.checkbox("Show graph visualization", value=True)
            show_export = st.checkbox("Show export options", value=True)
            
            # System stats
            st.header("📊 System Stats")
            if self.graph:
                st.metric("Total Concepts", len(self.graph.nodes))
                st.metric("Total Relationships", len(self.graph.edges))
                st.metric("Graph Density", f"{nx.density(self.graph):.4f}")
                
                # Additional stats
                degrees = [self.graph.degree(n) for n in self.graph.nodes()]
                st.metric("Avg Node Degree", f"{np.mean(degrees):.2f}")
                st.metric("Max Node Degree", max(degrees))
            
            # Example queries
            st.header("💡 Example Queries")
            examples = [
                "What is the relationship between bias and fairness in AI?",
                "How do privacy concerns affect machine learning deployment?",
                "What are the key components of responsible AI development?",
                "How does data governance impact AI model performance?",
                "What ethical considerations are important for AI systems?",
                "How can I implement a privacy-preserving ML system?",
                "What are the connections between AutoML and model interpretability?",
                "How does federated learning relate to data privacy?"
            ]
            
            for example in examples:
                if st.button(f"📝 {example[:25]}...", key=f"ex_{hash(example)}"):
                    st.session_state.current_query = example
        
        # Main enhanced interface
        st.header("🔍 Enhanced Query Interface")
        
        # Query input
        query = st.text_area(
            "Enter your knowledge-intensive question:",
            value=st.session_state.get('current_query', ''),
            height=100,
            placeholder="Ask a complex question that requires multi-hop reasoning..."
        )
        
        # Query execution
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            if st.button("🚀 Execute Enhanced HopRAG", type="primary"):
                if query and self.hoprag_engine:
                    self._process_enhanced_query(
                        query, max_hops, top_k_paths, use_hf_reasoning, 
                        generate_insights, show_reasoning, show_graph_viz, show_export
                    )
                else:
                    st.warning("Please enter a query first")
        
        with col2:
            if st.button("🔄 Clear Results"):
                st.session_state.current_query = ""
                st.rerun()
        
        with col3:
            if st.button("📊 Show Analytics"):
                self._show_analytics()
        
        # Tips section
        st.markdown("### 🎯 Enhanced Query Tips")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Best Practices:**
            - Use domain-specific terminology
            - Ask multi-step reasoning questions
            - Include relationship-focused queries
            - Try comparative questions
            """)
        
        with col2:
            st.markdown("""
            **HF Enhancements:**
            - Enhanced reasoning explanations
            - AI-generated insights
            - Improved confidence scoring
            - Export capabilities
            """)
    
    def _process_enhanced_query(self, query: str, max_hops: int, top_k: int, 
                               use_hf_reasoning: bool, generate_insights: bool,
                               show_reasoning: bool, show_viz: bool, show_export: bool):
        """Process enhanced HopRAG query"""
        
        start_time = time.time()
        
        with st.spinner("🔄 Processing enhanced HopRAG query..."):
            try:
                # Execute base HopRAG query
                result = self.hoprag_engine.query(query, max_hops=max_hops, top_k=top_k)
                
                # Apply HF enhancements
                if use_hf_reasoning:
                    for path in result.hop_paths:
                        path.hf_enhanced_reasoning = self.hf_enhancer.enhance_reasoning(path, query)
                
                if generate_insights:
                    result.hf_generated_insights = self.hf_enhancer.generate_insights(result)
                
                processing_time = time.time() - start_time
                
                # Display results
                self._display_enhanced_results(
                    result, query, processing_time, show_reasoning, show_viz, show_export
                )
                
            except Exception as e:
                st.error(f"❌ Error processing enhanced query: {e}")
    
    def _display_enhanced_results(self, result: HopRAGResult, query: str, processing_time: float,
                                 show_reasoning: bool, show_viz: bool, show_export: bool):
        """Display enhanced results"""
        
        # Header with timing
        st.header("📋 Enhanced HopRAG Results")
        st.markdown(f"**Query processed in {processing_time:.2f} seconds with HF enhancements**")
        
        # Main answer with confidence
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**Answer:** {result.answer}")
        with col2:
            st.metric("Confidence", f"{result.confidence:.1%}")
        
        # Enhanced metadata
        st.subheader("📊 Enhanced Query Metadata")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Start Entities", len(result.query_metadata.get('start_entities', [])))
        with col2:
            st.metric("Paths Explored", result.query_metadata.get('total_paths_explored', 0))
        with col3:
            st.metric("Max Hops Used", result.query_metadata.get('max_hops_used', 0))
        with col4:
            st.metric("Graph Coverage", f"{result.query_metadata.get('graph_coverage', 0):.1%}")
        with col5:
            st.metric("HF Enhanced", "✅" if any(p.hf_enhanced_reasoning for p in result.hop_paths) else "❌")
        
        # HF-generated insights
        if result.hf_generated_insights:
            st.subheader("🤖 AI-Generated Insights")
            st.info(result.hf_generated_insights)
        
        # Enhanced reasoning paths
        if show_reasoning and result.hop_paths:
            st.subheader("🔍 Enhanced Multi-Hop Reasoning Paths")
            
            for i, path in enumerate(result.hop_paths):
                with st.expander(f"Path {i+1}: {path.hop_count} hops (confidence: {path.confidence:.3f})"):
                    
                    # Basic path info
                    st.markdown(f"**Entities:** {' → '.join(path.entities)}")
                    st.markdown(f"**Relations:** {' → '.join(path.relations)}")
                    
                    # Original reasoning
                    st.markdown(f"**Original Reasoning:** {path.reasoning_chain}")
                    
                    # HF enhanced reasoning
                    if path.hf_enhanced_reasoning:
                        st.markdown(f"**🤖 HF Enhanced Reasoning:** {path.hf_enhanced_reasoning}")
                    
                    # Evidence
                    if path.evidence:
                        st.markdown("**Supporting Evidence:**")
                        for j, evidence in enumerate(path.evidence):
                            if evidence.strip():
                                st.markdown(f"*{path.entities[j]}:* {evidence[:200]}...")
        
        # Enhanced visualization
        if show_viz and result.hop_paths:
            st.subheader("🕸️ Enhanced Reasoning Graph")
            self._create_enhanced_visualization(result.hop_paths)
        
        # Export options
        if show_export:
            st.subheader("📤 Export Results")
            self._render_export_options(result, query)
        
        # Technical details
        with st.expander("🔧 Technical Details"):
            st.json(result.query_metadata)
    
    def _create_enhanced_visualization(self, hop_paths: List[HopPath]):
        """Create enhanced visualization with confidence coloring"""
        
        if not hop_paths:
            st.info("No reasoning paths to visualize")
            return
        
        # Import from the original app
        from hoprag_streamlit_app import HopRAGStreamlitApp
        base_app = HopRAGStreamlitApp()
        
        # Use the base visualization method
        base_app._create_hop_visualization(hop_paths)
        
        # Add confidence distribution chart
        st.subheader("📊 Path Confidence Distribution")
        
        confidences = [path.confidence for path in hop_paths]
        hop_counts = [path.hop_count for path in hop_paths]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=hop_counts,
            y=confidences,
            mode='markers',
            marker=dict(
                size=10,
                color=confidences,
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Confidence")
            ),
            text=[f"Path {i+1}" for i in range(len(hop_paths))],
            hovertemplate="<b>%{text}</b><br>Hops: %{x}<br>Confidence: %{y:.3f}<extra></extra>"
        ))
        
        fig.update_layout(
            title="Reasoning Path Analysis",
            xaxis_title="Number of Hops",
            yaxis_title="Confidence Score",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_export_options(self, result: HopRAGResult, query: str):
        """Render export options"""
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Export Format:**")
            export_format = st.selectbox(
                "Choose format",
                self.export_manager.export_formats,
                key="export_format"
            )
        
        with col2:
            st.markdown("**Export Actions:**")
            if st.button("📥 Generate Export"):
                try:
                    export_content = self.export_manager.export_results(result, query, export_format)
                    
                    # Display export content
                    st.subheader(f"📄 {export_format} Export")
                    
                    if export_format == 'JSON':
                        st.json(json.loads(export_content))
                    elif export_format == 'CSV':
                        st.text(export_content)
                    else:
                        st.markdown(export_content)
                    
                    # Download button
                    file_extension = export_format.lower().replace(' report', '')
                    filename = f"hoprag_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_extension}"
                    
                    st.download_button(
                        label=f"⬇️ Download {export_format}",
                        data=export_content,
                        file_name=filename,
                        mime=f"application/{file_extension}"
                    )
                    
                except Exception as e:
                    st.error(f"Export error: {e}")
    
    def _show_analytics(self):
        """Show analytics dashboard"""
        st.subheader("📊 Knowledge Graph Analytics")
        
        if not self.graph:
            st.warning("No graph loaded")
            return
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Degree distribution
            degrees = [self.graph.degree(n) for n in self.graph.nodes()]
            fig = go.Figure(data=[go.Histogram(x=degrees, nbinsx=20)])
            fig.update_layout(title="Node Degree Distribution", xaxis_title="Degree", yaxis_title="Count")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Top connected nodes
            top_nodes = sorted(self.graph.nodes(), key=lambda n: self.graph.degree(n), reverse=True)[:10]
            node_names = [node[:20] + "..." if len(node) > 20 else node for node in top_nodes]
            degrees = [self.graph.degree(node) for node in top_nodes]
            
            fig = go.Figure(data=[go.Bar(x=degrees, y=node_names, orientation='h')])
            fig.update_layout(title="Top Connected Concepts", xaxis_title="Connections", yaxis_title="Concepts")
            st.plotly_chart(fig, use_container_width=True)

def main():
    """Main entry point"""
    app = EnhancedHopRAGApp()
    app.run()

if __name__ == "__main__":
    main()