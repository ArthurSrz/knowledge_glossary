"""
Interactive GraphRAG Interface
A user-friendly interface for querying your knowledge graph with GraphRAG
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any
import json
import os
from pathlib import Path

# Import our enhanced GraphRAG
from enhanced_graphrag import EnhancedGraphRAG, GraphRAGResult, GraphPath

class InteractiveGraphRAG:
    """Interactive interface for GraphRAG queries"""
    
    def __init__(self):
        self.graphrag = None
        self.initialize_graphrag()
    
    def initialize_graphrag(self):
        """Initialize the GraphRAG system"""
        try:
            self.graphrag = EnhancedGraphRAG()
            st.success("GraphRAG system initialized successfully!")
        except Exception as e:
            st.error(f"Failed to initialize GraphRAG: {e}")
    
    def run_streamlit_app(self):
        """Run the Streamlit interface"""
        st.set_page_config(
            page_title="Knowledge Graph RAG",
            page_icon="🧠",
            layout="wide"
        )
        
        st.title("🧠 Knowledge Graph RAG Interface")
        st.markdown("Query your knowledge graph with enhanced reasoning capabilities")
        
        # Sidebar for configuration
        with st.sidebar:
            st.header("Configuration")
            
            explain_reasoning = st.checkbox("Show reasoning explanation", value=True)
            show_graph_viz = st.checkbox("Show graph visualization", value=True)
            max_results = st.slider("Max results to show", 1, 20, 5)
            
            st.header("Query Examples")
            example_queries = [
                "What is machine learning?",
                "How does bias affect AI fairness?",
                "What are the privacy concerns in ML?",
                "Explain the relationship between data governance and ML",
                "How can I implement ethical AI systems?"
            ]
            
            for query in example_queries:
                if st.button(f"📝 {query[:30]}...", key=f"example_{hash(query)}"):
                    st.session_state.current_query = query
        
        # Main query interface
        col1, col2 = st.columns([2, 1])
        
        with col1:
            query = st.text_area(
                "Enter your question:",
                value=st.session_state.get('current_query', ''),
                height=100,
                placeholder="Ask anything about your knowledge graph..."
            )
            
            if st.button("🔍 Search", type="primary"):
                if query and self.graphrag:
                    self.process_query(query, explain_reasoning, show_graph_viz, max_results)
        
        with col2:
            st.markdown("### Quick Stats")
            if self.graphrag:
                try:
                    # Get basic stats
                    nx_graph = self.graphrag.graph_index.get_networkx_graph()
                    st.metric("Graph Nodes", len(nx_graph.nodes))
                    st.metric("Graph Edges", len(nx_graph.edges))
                    st.metric("Available Indices", 3)
                except:
                    st.info("Stats unavailable")
    
    def process_query(self, query: str, explain: bool, show_viz: bool, max_results: int):
        """Process a user query"""
        with st.spinner("Processing your query..."):
            try:
                result = self.graphrag.query(query, explain=False)
                self.display_results(result, query, explain, show_viz, max_results)
            except Exception as e:
                st.error(f"Error processing query: {e}")
    
    def display_results(self, result: GraphRAGResult, query: str, explain: bool, show_viz: bool, max_results: int):
        """Display query results"""
        
        # Main answer
        st.subheader("📋 Answer")
        st.markdown(result.answer)
        
        # Confidence and metadata
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Confidence", f"{result.confidence:.2%}")
        with col2:
            st.metric("Sources Used", len(result.source_nodes))
        with col3:
            st.metric("Reasoning Paths", len(result.reasoning_paths))
        
        # Reasoning explanation
        if explain and result.reasoning_paths:
            st.subheader("🔍 Reasoning Paths")
            
            for i, path in enumerate(result.reasoning_paths[:3]):
                with st.expander(f"Path {i+1} (Score: {path.score:.3f})"):
                    st.markdown(f"**Reasoning:** {path.reasoning}")
                    st.markdown(f"**Nodes:** {' → '.join(path.nodes)}")
                    st.markdown(f"**Edges:** {' → '.join(path.edges)}")
        
        # Source nodes
        if result.source_nodes:
            st.subheader("📚 Source Context")
            
            for i, node in enumerate(result.source_nodes[:max_results]):
                with st.expander(f"Source {i+1}" + (f" (Score: {node.score:.3f})" if hasattr(node, 'score') else "")):
                    st.markdown(node.node.text)
                    if hasattr(node.node, 'metadata') and node.node.metadata:
                        st.json(node.node.metadata)
        
        # Graph visualization
        if show_viz and result.reasoning_paths:
            st.subheader("🕸️ Graph Visualization")
            self.create_graph_visualization(result.reasoning_paths)
        
        # Technical details
        with st.expander("🔧 Technical Details"):
            st.json(result.graph_context)
    
    def create_graph_visualization(self, paths: List[GraphPath]):
        """Create an interactive graph visualization"""
        if not paths:
            st.info("No reasoning paths to visualize")
            return
        
        # Collect all nodes and edges from paths
        all_nodes = set()
        all_edges = []
        
        for path in paths[:3]:  # Top 3 paths
            all_nodes.update(path.nodes)
            for i in range(len(path.nodes) - 1):
                all_edges.append((path.nodes[i], path.nodes[i+1], path.edges[i]))
        
        # Create network graph
        node_list = list(all_nodes)
        edge_x = []
        edge_y = []
        edge_text = []
        
        # Simple circular layout
        import math
        n = len(node_list)
        node_positions = {}
        
        for i, node in enumerate(node_list):
            angle = 2 * math.pi * i / n
            x = math.cos(angle)
            y = math.sin(angle)
            node_positions[node] = (x, y)
        
        # Add edges
        for source, target, edge_type in all_edges:
            if source in node_positions and target in node_positions:
                x0, y0 = node_positions[source]
                x1, y1 = node_positions[target]
                edge_x.extend([x0, x1, None])
                edge_y.extend([y0, y1, None])
                edge_text.append(edge_type)
        
        # Create plotly figure
        fig = go.Figure()
        
        # Add edges
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='gray'),
            hoverinfo='none',
            mode='lines',
            showlegend=False
        ))
        
        # Add nodes
        node_x = [node_positions[node][0] for node in node_list]
        node_y = [node_positions[node][1] for node in node_list]
        
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_list,
            textposition="middle center",
            hovertext=node_list,
            marker=dict(
                size=30,
                color='lightblue',
                line=dict(width=2, color='blue')
            ),
            showlegend=False
        ))
        
        fig.update_layout(
            title="Reasoning Path Visualization",
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            annotations=[ dict(
                text="Nodes represent concepts, edges show relationships",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002,
                xanchor='left', yanchor='bottom',
                font=dict(color='gray', size=12)
            )],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)

def main():
    """Main function to run the interactive interface"""
    app = InteractiveGraphRAG()
    app.run_streamlit_app()

if __name__ == "__main__":
    main()