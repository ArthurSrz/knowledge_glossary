"""
HopRAG Streamlit App - Knowledge-Intensive AI with Multi-Hop Reasoning
Implementation based on HopRAG paper: https://arxiv.org/abs/2502.12442
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any, Optional, Tuple
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

@dataclass
class HopRAGResult:
    """Result from HopRAG query"""
    answer: str
    confidence: float
    hop_paths: List[HopPath]
    supporting_evidence: List[str]
    reasoning_explanation: str
    reasoning_paper: str
    query_metadata: Dict[str, Any]

class KnowledgeGraphLoader:
    """Loads knowledge graph from markdown files"""
    
    def __init__(self, graph_path: str):
        self.graph_path = Path(graph_path)
        self.graph = nx.Graph()
        self.concept_content = {}
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def load_graph(self) -> nx.Graph:
        """Load knowledge graph from markdown files"""
        st.info("Loading knowledge graph from markdown files...")
        
        # Load all markdown files
        markdown_files = list(self.graph_path.glob("*.md"))
        progress_bar = st.progress(0)
        
        for i, file_path in enumerate(markdown_files):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                concept_name = file_path.stem
                self.concept_content[concept_name] = content
                
                # Add node to graph
                self.graph.add_node(concept_name, content=content)
                
                # Extract relationships from content
                self._extract_relationships(concept_name, content)
                
                progress_bar.progress((i + 1) / len(markdown_files))
                
            except Exception as e:
                logger.error(f"Error loading {file_path}: {e}")
        
        st.success(f"Loaded {len(self.graph.nodes)} concepts and {len(self.graph.edges)} relationships")
        return self.graph
    
    def _extract_relationships(self, concept_name: str, content: str):
        """Extract relationships from markdown content"""
        # Look for markdown links to other concepts
        links = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        for link in links:
            if link in self.concept_content:
                self.graph.add_edge(concept_name, link, relation="RELATED_TO")
        
        # Look for explicit relationships in content
        relation_patterns = [
            (r'is a type of (.+)', "IS_A"),
            (r'is related to (.+)', "RELATED_TO"),
            (r'depends on (.+)', "DEPENDS_ON"),
            (r'uses (.+)', "USES"),
            (r'implements (.+)', "IMPLEMENTS"),
        ]
        
        for pattern, relation_type in relation_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Clean up the match
                target = match.strip().rstrip('.,;:')
                if target in self.concept_content:
                    self.graph.add_edge(concept_name, target, relation=relation_type)

class HopRAGEngine:
    """Core HopRAG reasoning engine"""
    
    def __init__(self, knowledge_graph: nx.Graph, concept_content: Dict[str, str]):
        self.graph = knowledge_graph
        self.concept_content = concept_content
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.max_hops = 3
        self.top_k_paths = 10
        
    def query(self, question: str, max_hops: int = 3, top_k: int = 5) -> HopRAGResult:
        """Process query using HopRAG methodology"""
        
        # Step 1: Entity Recognition and Linking
        start_entities = self._extract_entities(question)
        
        # Step 2: Multi-hop Path Discovery
        hop_paths = self._discover_hop_paths(start_entities, question, max_hops)
        
        # Step 3: Evidence Aggregation
        evidence = self._aggregate_evidence(hop_paths)
        
        # Step 4: Answer Generation
        answer, confidence = self._generate_answer(question, hop_paths, evidence)
        
        # Step 5: Reasoning Explanation
        reasoning = self._generate_reasoning_explanation(question, hop_paths)
        
        # Step 6: Generate Reasoning Paper
        reasoning_paper = self._generate_reasoning_paper(question, hop_paths)
        
        return HopRAGResult(
            answer=answer,
            confidence=confidence,
            hop_paths=hop_paths[:top_k],
            supporting_evidence=evidence,
            reasoning_explanation=reasoning,
            reasoning_paper=reasoning_paper,
            query_metadata={
                "start_entities": start_entities,
                "total_paths_explored": len(hop_paths),
                "max_hops_used": max_hops,
                "graph_coverage": len(set().union(*[path.entities for path in hop_paths])) / len(self.graph.nodes)
            }
        )
    
    def _extract_entities(self, question: str) -> List[str]:
        """Extract relevant entities from question"""
        question_embedding = self.embedding_model.encode(question)
        
        # Find most similar concepts
        similarities = []
        for concept, content in self.concept_content.items():
            concept_embedding = self.embedding_model.encode(concept + " " + content[:500])
            similarity = np.dot(question_embedding, concept_embedding) / (
                np.linalg.norm(question_embedding) * np.linalg.norm(concept_embedding)
            )
            similarities.append((concept, similarity))
        
        # Sort by similarity and take top entities
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [concept for concept, _ in similarities[:5]]
    
    def _discover_hop_paths(self, start_entities: List[str], question: str, max_hops: int) -> List[HopPath]:
        """Discover multi-hop reasoning paths"""
        question_embedding = self.embedding_model.encode(question)
        all_paths = []
        
        for start_entity in start_entities:
            if start_entity not in self.graph.nodes:
                continue
                
            # BFS to find paths up to max_hops
            queue = deque([(start_entity, [start_entity], [], 0)])
            visited = set()
            
            while queue:
                current_node, path, relations, hop_count = queue.popleft()
                
                if hop_count >= max_hops:
                    continue
                
                # Generate evidence for current path
                evidence = [self.concept_content.get(node, "") for node in path]
                
                # Calculate path relevance
                path_text = " ".join(path) + " " + " ".join(evidence)
                path_embedding = self.embedding_model.encode(path_text[:1000])
                
                similarity = np.dot(question_embedding, path_embedding) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(path_embedding)
                )
                
                # Create reasoning chain
                reasoning_chain = self._create_reasoning_chain(path, relations)
                
                hop_path = HopPath(
                    entities=path.copy(),
                    relations=relations.copy(),
                    evidence=evidence,
                    confidence=similarity,
                    hop_count=hop_count,
                    reasoning_chain=reasoning_chain
                )
                all_paths.append(hop_path)
                
                # Expand to neighbors
                for neighbor in self.graph.neighbors(current_node):
                    if neighbor not in visited or len(path) < max_hops:
                        edge_data = self.graph.get_edge_data(current_node, neighbor)
                        relation = edge_data.get('relation', 'RELATED_TO')
                        
                        new_path = path + [neighbor]
                        new_relations = relations + [relation]
                        
                        queue.append((neighbor, new_path, new_relations, hop_count + 1))
                        visited.add(neighbor)
        
        # Sort paths by confidence
        all_paths.sort(key=lambda x: x.confidence, reverse=True)
        return all_paths[:self.top_k_paths]
    
    def _create_reasoning_chain(self, path: List[str], relations: List[str]) -> str:
        """Create human-readable reasoning chain"""
        if len(path) < 2:
            return path[0] if path else ""
        
        chain_parts = []
        for i in range(len(path) - 1):
            chain_parts.append(f"{path[i]} → {relations[i]} → {path[i+1]}")
        
        return " | ".join(chain_parts)
    
    def _aggregate_evidence(self, hop_paths: List[HopPath]) -> List[str]:
        """Aggregate evidence from multiple paths"""
        evidence_map = defaultdict(float)
        
        for path in hop_paths:
            for entity, evidence_text in zip(path.entities, path.evidence):
                # Weight evidence by path confidence
                evidence_map[evidence_text] += path.confidence
        
        # Sort by aggregated confidence
        sorted_evidence = sorted(evidence_map.items(), key=lambda x: x[1], reverse=True)
        return [evidence for evidence, _ in sorted_evidence[:10]]
    
    def _generate_answer(self, question: str, hop_paths: List[HopPath], evidence: List[str]) -> Tuple[str, float]:
        """Generate answer using retrieved evidence"""
        # Simple extractive approach - in practice, use a generative model
        
        # Combine top evidence
        combined_evidence = "\n".join(evidence[:3])
        
        # Extract relevant sentences
        sentences = re.split(r'[.!?]+', combined_evidence)
        question_embedding = self.embedding_model.encode(question)
        
        sentence_scores = []
        for sentence in sentences:
            if len(sentence.strip()) > 20:
                sentence_embedding = self.embedding_model.encode(sentence)
                score = np.dot(question_embedding, sentence_embedding) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(sentence_embedding)
                )
                sentence_scores.append((sentence.strip(), score))
        
        # Sort and take top sentences
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        answer_sentences = [sent for sent, _ in sentence_scores[:3]]
        answer = " ".join(answer_sentences)
        
        # Calculate confidence based on path quality
        avg_path_confidence = np.mean([path.confidence for path in hop_paths[:3]]) if hop_paths else 0.0
        
        return answer, avg_path_confidence
    
    def _generate_reasoning_explanation(self, question: str, hop_paths: List[HopPath]) -> str:
        """Generate explanation of reasoning process"""
        explanation_parts = [
            f"To answer '{question}', I explored {len(hop_paths)} reasoning paths:",
            ""
        ]
        
        for i, path in enumerate(hop_paths[:3]):
            explanation_parts.append(f"Path {i+1} ({path.hop_count} hops, confidence: {path.confidence:.3f}):")
            explanation_parts.append(f"  {path.reasoning_chain}")
            explanation_parts.append("")
        
        return "\n".join(explanation_parts)
    
    def _generate_reasoning_paper(self, question: str, hop_paths: List[HopPath]) -> str:
        """Generate reasoning paper with concatenated path narratives"""
        paper_parts = [
            f"# Reasoning Paper: {question}",
            "",
            "## Abstract",
            f"This paper presents a multi-hop reasoning analysis to answer the question: '{question}'. "
            f"Through systematic exploration of {len(hop_paths)} reasoning paths across our knowledge graph, "
            f"we identify key conceptual relationships and evidence chains that inform our response.",
            "",
            "## Methodology",
            "We employed a graph-based multi-hop reasoning approach, exploring paths up to 3 hops from "
            "initial entities. Each path was scored for relevance and confidence, with evidence aggregated "
            "from multiple reasoning chains.",
            "",
            "## Reasoning Paths Analysis",
            ""
        ]
        
        # Generate detailed narrative for each path
        for i, path in enumerate(hop_paths[:5]):  # Top 5 paths for paper
            paper_parts.extend([
                f"### Path {i+1}: {' → '.join(path.entities)}",
                f"**Confidence Score:** {path.confidence:.3f} | **Hop Count:** {path.hop_count}",
                "",
                f"**Reasoning Chain:** {path.reasoning_chain}",
                "",
                "**Evidence Analysis:**"
            ])
            
            # Generate narrative from evidence
            for j, evidence in enumerate(path.evidence):
                if evidence.strip():
                    # Extract key sentences from evidence
                    sentences = [s.strip() for s in evidence.split('.') if len(s.strip()) > 20]
                    if sentences:
                        paper_parts.append(f"*{path.entities[j]}*: {sentences[0]}.")
            
            paper_parts.extend(["", "---", ""])
        
        # Synthesis section
        paper_parts.extend([
            "## Synthesis and Conclusion",
            "",
            "Based on the analysis of multiple reasoning paths, we can synthesize the following key insights:",
            ""
        ])
        
        # Extract common themes across paths
        all_entities = set()
        all_relations = set()
        for path in hop_paths[:5]:
            all_entities.update(path.entities)
            all_relations.update(path.relations)
        
        paper_parts.extend([
            f"- **Key Concepts Identified:** {', '.join(sorted(list(all_entities))[:10])}",
            f"- **Relationship Types:** {', '.join(sorted(list(all_relations))[:8])}",
            f"- **Confidence Range:** {min(p.confidence for p in hop_paths[:5]):.3f} - {max(p.confidence for p in hop_paths[:5]):.3f}",
            "",
            "The convergence of multiple reasoning paths provides strong evidence for our conclusions, "
            "with cross-validation through independent conceptual chains strengthening our confidence in the results.",
            "",
            "## References",
            "- Knowledge Graph: Local markdown-based concept repository",
            "- Reasoning Engine: HopRAG multi-hop reasoning system",
            f"- Query Processing Time: {len(hop_paths)} paths explored",
            ""
        ])
        
        return "\n".join(paper_parts)

class HopRAGStreamlitApp:
    """Streamlit application for HopRAG"""
    
    def __init__(self):
        self.kg_loader = None
        self.hoprag_engine = None
        self.graph = None
        
    def run(self):
        """Run the Streamlit application"""
        st.set_page_config(
            page_title="HopRAG - Knowledge-Intensive AI",
            page_icon="🔗",
            layout="wide"
        )
        
        st.title("🔗 HopRAG - Knowledge-Intensive AI")
        st.markdown("Multi-hop reasoning over your knowledge graph for enhanced AI capabilities")
        
        # Initialize system
        if not self.hoprag_engine:
            self._initialize_system()
        
        # Main interface
        self._render_interface()
    
    def _initialize_system(self):
        """Initialize the HopRAG system"""
        st.header("🚀 System Initialization")
        
        with st.spinner("Loading knowledge graph..."):
            try:
                # Load knowledge graph
                self.kg_loader = KnowledgeGraphLoader("/Users/arthursarazin/Documents/knowledge_glossary/graph")
                self.graph = self.kg_loader.load_graph()
                
                # Initialize HopRAG engine
                self.hoprag_engine = HopRAGEngine(self.graph, self.kg_loader.concept_content)
                
                st.success("✅ HopRAG system initialized successfully!")
                
            except Exception as e:
                st.error(f"❌ Error initializing system: {e}")
                st.stop()
    
    def _render_interface(self):
        """Render the main interface"""
        
        # Sidebar configuration
        with st.sidebar:
            st.header("🔧 Configuration")
            
            max_hops = st.slider("Maximum hops", 1, 5, 3)
            top_k_paths = st.slider("Top K paths", 1, 20, 5)
            show_reasoning = st.checkbox("Show reasoning paths", value=True)
            show_reasoning_paper = st.checkbox("Show reasoning paper", value=True)
            show_graph_viz = st.checkbox("Show graph visualization", value=True)
            
            st.header("📊 System Stats")
            if self.graph:
                st.metric("Total Concepts", len(self.graph.nodes))
                st.metric("Total Relationships", len(self.graph.edges))
                st.metric("Graph Density", f"{nx.density(self.graph):.4f}")
            
            st.header("💡 Example Queries")
            examples = [
                "What is the relationship between bias and fairness in AI?",
                "How do privacy concerns affect machine learning deployment?",
                "What are the key components of responsible AI development?",
                "How does data governance impact AI model performance?",
                "What ethical considerations are important for AI systems?"
            ]
            
            for example in examples:
                if st.button(f"📝 {example[:30]}...", key=f"ex_{hash(example)}"):
                    st.session_state.current_query = example
        
        # Main query interface
        st.header("🔍 Query Interface")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            query = st.text_area(
                "Enter your knowledge-intensive question:",
                value=st.session_state.get('current_query', ''),
                height=100,
                placeholder="Ask a complex question that requires multi-hop reasoning..."
            )
            
            if st.button("🚀 Execute HopRAG Query", type="primary"):
                if query and self.hoprag_engine:
                    self._process_query(query, max_hops, top_k_paths, show_reasoning, show_reasoning_paper, show_graph_viz)
                else:
                    st.warning("Please enter a query first")
        
        with col2:
            st.markdown("### 🎯 Query Tips")
            st.markdown("""
            - Ask complex questions requiring multiple reasoning steps
            - Use domain-specific terms from your knowledge graph
            - Questions about relationships work well
            - Try asking "how" and "why" questions
            """)
    
    def _process_query(self, query: str, max_hops: int, top_k: int, show_reasoning: bool, show_reasoning_paper: bool, show_viz: bool):
        """Process a HopRAG query"""
        
        start_time = time.time()
        
        with st.spinner("🔄 Processing HopRAG query..."):
            try:
                result = self.hoprag_engine.query(query, max_hops=max_hops, top_k=top_k)
                
                processing_time = time.time() - start_time
                
                self._display_results(result, processing_time, show_reasoning, show_reasoning_paper, show_viz)
                
            except Exception as e:
                st.error(f"❌ Error processing query: {e}")
    
    def _display_results(self, result: HopRAGResult, processing_time: float, show_reasoning: bool, show_reasoning_paper: bool, show_viz: bool):
        """Display query results"""
        
        # Main answer
        st.header("📋 HopRAG Answer")
        st.markdown(f"**Query processed in {processing_time:.2f} seconds**")
        
        # Answer with confidence
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(result.answer)
        with col2:
            st.metric("Confidence", f"{result.confidence:.1%}")
        
        # Metadata
        st.header("📊 Query Metadata")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Start Entities", len(result.query_metadata.get('start_entities', [])))
        with col2:
            st.metric("Paths Explored", result.query_metadata.get('total_paths_explored', 0))
        with col3:
            st.metric("Max Hops Used", result.query_metadata.get('max_hops_used', 0))
        with col4:
            st.metric("Graph Coverage", f"{result.query_metadata.get('graph_coverage', 0):.1%}")
        
        # Reasoning paths
        if show_reasoning and result.hop_paths:
            st.header("🔍 Multi-Hop Reasoning Paths")
            
            for i, path in enumerate(result.hop_paths):
                with st.expander(f"Path {i+1}: {path.hop_count} hops (confidence: {path.confidence:.3f})"):
                    st.markdown(f"**Reasoning Chain:**")
                    st.text(path.reasoning_chain)
                    
                    st.markdown(f"**Entities:** {' → '.join(path.entities)}")
                    st.markdown(f"**Relations:** {' → '.join(path.relations)}")
                    
                    # Show evidence
                    st.markdown("**Supporting Evidence:**")
                    for j, evidence in enumerate(path.evidence):
                        if evidence.strip():
                            st.markdown(f"*Entity {j+1}:* {evidence[:200]}...")
        
        # Reasoning paper
        if show_reasoning_paper and result.reasoning_paper:
            st.header("📄 Reasoning Paper")
            st.markdown(result.reasoning_paper)
        
        # Graph visualization
        if show_viz and result.hop_paths:
            st.header("🕸️ Reasoning Graph Visualization")
            self._create_hop_visualization(result.hop_paths)
        
        # Reasoning explanation
        if result.reasoning_explanation:
            st.header("💭 Reasoning Explanation")
            st.text(result.reasoning_explanation)
        
        # Supporting evidence
        if result.supporting_evidence:
            st.header("📚 Supporting Evidence")
            for i, evidence in enumerate(result.supporting_evidence[:5]):
                with st.expander(f"Evidence {i+1}"):
                    st.markdown(evidence[:500] + "..." if len(evidence) > 500 else evidence)
    
    def _create_hop_visualization(self, hop_paths: List[HopPath]):
        """Create interactive visualization of reasoning paths"""
        
        if not hop_paths:
            st.info("No reasoning paths to visualize")
            return
        
        # Collect all nodes and edges
        all_nodes = set()
        all_edges = []
        
        for path_idx, path in enumerate(hop_paths[:3]):  # Top 3 paths
            all_nodes.update(path.entities)
            
            for i in range(len(path.entities) - 1):
                all_edges.append({
                    'source': path.entities[i],
                    'target': path.entities[i+1],
                    'relation': path.relations[i],
                    'path_idx': path_idx,
                    'confidence': path.confidence
                })
        
        # Create network graph
        fig = go.Figure()
        
        # Position nodes using NetworkX spring layout
        G = nx.Graph()
        for edge in all_edges:
            G.add_edge(edge['source'], edge['target'])
        
        pos = nx.spring_layout(G, k=3, iterations=50)
        
        # Add edges
        edge_traces = []
        colors = ['red', 'blue', 'green']
        
        for path_idx in range(3):
            path_edges = [e for e in all_edges if e['path_idx'] == path_idx]
            
            edge_x = []
            edge_y = []
            
            for edge in path_edges:
                if edge['source'] in pos and edge['target'] in pos:
                    x0, y0 = pos[edge['source']]
                    x1, y1 = pos[edge['target']]
                    edge_x.extend([x0, x1, None])
                    edge_y.extend([y0, y1, None])
            
            edge_trace = go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=2, color=colors[path_idx]),
                hoverinfo='none',
                mode='lines',
                name=f'Path {path_idx + 1}',
                showlegend=True
            )
            
            fig.add_trace(edge_trace)
        
        # Add nodes
        node_x = []
        node_y = []
        node_text = []
        node_info = []
        
        for node in all_nodes:
            if node in pos:
                x, y = pos[node]
                node_x.append(x)
                node_y.append(y)
                node_text.append(node)
                node_info.append(f"Concept: {node}")
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            textposition="middle center",
            hovertext=node_info,
            marker=dict(
                size=20,
                color='lightblue',
                line=dict(width=2, color='darkblue')
            ),
            textfont=dict(size=10),
            showlegend=False
        )
        
        fig.add_trace(node_trace)
        
        fig.update_layout(
            title="Multi-Hop Reasoning Paths",
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[dict(
                text="Different colors represent different reasoning paths",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002,
                xanchor='left', yanchor='bottom',
                font=dict(color='gray', size=12)
            )],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)

def main():
    """Main application entry point"""
    app = HopRAGStreamlitApp()
    app.run()

if __name__ == "__main__":
    main()