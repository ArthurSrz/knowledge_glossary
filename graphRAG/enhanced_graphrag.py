"""
Enhanced GraphRAG Implementation with MCP Integration
Combines vector search, knowledge graphs, and property graphs for advanced reasoning
"""

import os
import json
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
import torch
from sentence_transformers import SentenceTransformer

from llama_index.core import (
    StorageContext, 
    load_index_from_storage,
    Settings,
    Document
)
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import KnowledgeGraphRAGRetriever
from llama_index.core import get_response_synthesizer
from llama_index.core.schema import NodeWithScore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class GraphPath:
    """Represents a reasoning path through the knowledge graph"""
    nodes: List[str]
    edges: List[str]
    score: float
    reasoning: str
    
@dataclass
class GraphRAGResult:
    """Enhanced result with graph reasoning paths"""
    answer: str
    confidence: float
    reasoning_paths: List[GraphPath]
    source_nodes: List[NodeWithScore]
    graph_context: Dict[str, Any]

class Text2CypherGenerator:
    """Generates Cypher queries from natural language using HuggingFace models"""
    
    def __init__(self, model_name: str = "google/text2cypher-gemma-3-4b"):
        self.model_name = model_name
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                device_map="auto"
            )
            self.available = True
        except Exception as e:
            logger.warning(f"Text2Cypher model not available: {e}")
            self.available = False
    
    def generate_cypher(self, natural_language_query: str, schema_context: str = "") -> str:
        """Generate Cypher query from natural language"""
        if not self.available:
            return ""
        
        prompt = f"""
        Schema: {schema_context}
        Question: {natural_language_query}
        Cypher:
        """
        
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_length=200, temperature=0.7)
            cypher = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return cypher.split("Cypher:")[-1].strip()
        except Exception as e:
            logger.error(f"Error generating Cypher: {e}")
            return ""

class MultiHopReasoner:
    """Implements multi-hop reasoning across knowledge graphs"""
    
    def __init__(self, graph: nx.Graph, max_depth: int = 3):
        self.graph = graph
        self.max_depth = max_depth
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def find_reasoning_paths(self, start_nodes: List[str], query: str, top_k: int = 5) -> List[GraphPath]:
        """Find top-k reasoning paths through the graph"""
        query_embedding = self.embedding_model.encode(query)
        paths = []
        
        for start_node in start_nodes:
            if start_node not in self.graph.nodes:
                continue
                
            # BFS to find paths up to max_depth
            for target_node in self.graph.nodes:
                if start_node == target_node:
                    continue
                    
                try:
                    path = nx.shortest_path(self.graph, start_node, target_node)
                    if len(path) <= self.max_depth + 1:
                        # Calculate path score based on semantic similarity
                        path_text = " -> ".join(path)
                        path_embedding = self.embedding_model.encode(path_text)
                        similarity = np.dot(query_embedding, path_embedding) / (
                            np.linalg.norm(query_embedding) * np.linalg.norm(path_embedding)
                        )
                        
                        # Extract edge labels
                        edges = []
                        for i in range(len(path) - 1):
                            edge_data = self.graph.get_edge_data(path[i], path[i+1])
                            edges.append(edge_data.get('label', 'RELATED') if edge_data else 'RELATED')
                        
                        reasoning = self._generate_reasoning(path, edges)
                        
                        paths.append(GraphPath(
                            nodes=path,
                            edges=edges,
                            score=similarity,
                            reasoning=reasoning
                        ))
                        
                except nx.NetworkXNoPath:
                    continue
        
        # Sort by score and return top-k
        paths.sort(key=lambda x: x.score, reverse=True)
        return paths[:top_k]
    
    def _generate_reasoning(self, path: List[str], edges: List[str]) -> str:
        """Generate human-readable reasoning for a path"""
        reasoning_parts = []
        for i in range(len(path) - 1):
            reasoning_parts.append(f"{path[i]} {edges[i]} {path[i+1]}")
        return " → ".join(reasoning_parts)

class EnhancedGraphRAG:
    """Enhanced GraphRAG system with MCP integration and multi-hop reasoning"""
    
    def __init__(self, base_path: str = "/Users/arthursarazin/Documents/knowledge_glossary/graphRAG"):
        self.base_path = Path(base_path)
        self.setup_llm()
        self.load_indices()
        self.setup_text2cypher()
        self.setup_multihop_reasoner()
        
    def setup_llm(self):
        """Initialize LLM and embeddings"""
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.llm = OpenAI(temperature=0, model="gpt-4o", max_tokens=3000)
            Settings.llm = self.llm
        
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        Settings.chunk_size = 512
        
    def load_indices(self):
        """Load all storage contexts and indices"""
        try:
            # Vector index
            vector_storage_context = StorageContext.from_defaults(
                docstore=SimpleDocumentStore.from_persist_dir(persist_dir=str(self.base_path / "vector")),
                vector_store=SimpleVectorStore.from_persist_dir(persist_dir=str(self.base_path / "vector")),
                index_store=SimpleIndexStore.from_persist_dir(persist_dir=str(self.base_path / "vector")),
            )
            self.vector_index = load_index_from_storage(vector_storage_context)
            
            # Knowledge graph index
            graph_storage_context = StorageContext.from_defaults(
                docstore=SimpleDocumentStore.from_persist_dir(persist_dir=str(self.base_path / "knowledge_graph")),
                graph_store=SimpleGraphStore.from_persist_dir(persist_dir=str(self.base_path / "knowledge_graph")),
                index_store=SimpleIndexStore.from_persist_dir(persist_dir=str(self.base_path / "knowledge_graph")),
            )
            self.graph_index = load_index_from_storage(graph_storage_context)
            
            # Property graph index
            onto_storage_context = StorageContext.from_defaults(persist_dir=str(self.base_path / "onto_graph"))
            self.onto_index = load_index_from_storage(onto_storage_context)
            
            logger.info("All indices loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading indices: {e}")
            raise
    
    def setup_text2cypher(self):
        """Setup Text2Cypher generator"""
        self.text2cypher = Text2CypherGenerator()
        
    def setup_multihop_reasoner(self):
        """Setup multi-hop reasoning system"""
        try:
            nx_graph = self.graph_index.get_networkx_graph()
            self.multihop_reasoner = MultiHopReasoner(nx_graph)
            logger.info(f"Multi-hop reasoner initialized with {len(nx_graph.nodes)} nodes")
        except Exception as e:
            logger.error(f"Error setting up multi-hop reasoner: {e}")
            self.multihop_reasoner = None
    
    def enhanced_retrieve(self, query: str, top_k: int = 10) -> Tuple[List[NodeWithScore], List[GraphPath]]:
        """Enhanced retrieval combining vector, graph, and multi-hop reasoning"""
        
        # 1. Vector retrieval
        vector_retriever = self.vector_index.as_retriever(similarity_top_k=top_k)
        vector_nodes = vector_retriever.retrieve(query)
        
        # 2. Graph retrieval
        graph_retriever = self.graph_index.as_retriever(similarity_top_k=top_k)
        graph_nodes = graph_retriever.retrieve(query)
        
        # 3. Property graph retrieval
        onto_retriever = self.onto_index.as_retriever(similarity_top_k=top_k, depth=3)
        onto_nodes = onto_retriever.retrieve(query)
        
        # 4. Multi-hop reasoning
        reasoning_paths = []
        if self.multihop_reasoner:
            start_nodes = [node.node.text[:50] for node in vector_nodes[:3]]  # Use top vector results as seeds
            reasoning_paths = self.multihop_reasoner.find_reasoning_paths(start_nodes, query, top_k=5)
        
        # Combine and deduplicate nodes
        all_nodes = vector_nodes + graph_nodes + onto_nodes
        unique_nodes = []
        seen_texts = set()
        
        for node in all_nodes:
            node_text = node.node.text[:100]  # Use first 100 chars as key
            if node_text not in seen_texts:
                unique_nodes.append(node)
                seen_texts.add(node_text)
        
        # Sort by score
        unique_nodes.sort(key=lambda x: x.score if hasattr(x, 'score') else 0, reverse=True)
        
        return unique_nodes[:top_k], reasoning_paths
    
    def generate_cypher_query(self, query: str) -> str:
        """Generate Cypher query for graph databases"""
        if not self.text2cypher.available:
            return ""
        
        # Get schema context from the property graph
        schema_context = "Knowledge graph with concepts, relationships, and properties"
        return self.text2cypher.generate_cypher(query, schema_context)
    
    def synthesize_response(self, query: str, nodes: List[NodeWithScore], 
                          reasoning_paths: List[GraphPath]) -> GraphRAGResult:
        """Synthesize final response with graph reasoning"""
        
        # Prepare context
        context_parts = []
        
        # Add retrieved node contexts
        for node in nodes[:5]:  # Top 5 nodes
            context_parts.append(f"Source: {node.node.text}")
        
        # Add reasoning paths
        if reasoning_paths:
            context_parts.append("\nReasoning Paths:")
            for i, path in enumerate(reasoning_paths[:3]):  # Top 3 paths
                context_parts.append(f"Path {i+1}: {path.reasoning} (confidence: {path.score:.3f})")
        
        context = "\n".join(context_parts)
        
        # Generate response using LLM
        response_synthesizer = get_response_synthesizer(
            response_mode="tree_summarize",
            service_context=None
        )
        
        # Create enhanced prompt
        enhanced_prompt = f"""
        Based on the following context and reasoning paths, provide a comprehensive answer to the question.
        
        Question: {query}
        
        Context:
        {context}
        
        Please provide:
        1. A direct answer to the question
        2. Explanation of the reasoning process
        3. Confidence level in the answer
        
        Answer:
        """
        
        try:
            response = self.llm.complete(enhanced_prompt)
            answer = response.text
            
            # Extract confidence (simple heuristic)
            confidence = min(len(nodes) / 10.0, 1.0)  # Based on number of relevant nodes
            
            # Create graph context
            graph_context = {
                "total_nodes_retrieved": len(nodes),
                "reasoning_paths_found": len(reasoning_paths),
                "cypher_query": self.generate_cypher_query(query),
                "retrieval_sources": ["vector", "knowledge_graph", "property_graph"]
            }
            
            return GraphRAGResult(
                answer=answer,
                confidence=confidence,
                reasoning_paths=reasoning_paths,
                source_nodes=nodes,
                graph_context=graph_context
            )
            
        except Exception as e:
            logger.error(f"Error in response synthesis: {e}")
            return GraphRAGResult(
                answer="Error generating response",
                confidence=0.0,
                reasoning_paths=[],
                source_nodes=[],
                graph_context={}
            )
    
    def query(self, question: str, explain: bool = True) -> GraphRAGResult:
        """Main query method with enhanced GraphRAG"""
        logger.info(f"Processing query: {question}")
        
        # Enhanced retrieval
        nodes, reasoning_paths = self.enhanced_retrieve(question)
        
        # Synthesize response
        result = self.synthesize_response(question, nodes, reasoning_paths)
        
        if explain:
            self.explain_reasoning(result)
        
        return result
    
    def explain_reasoning(self, result: GraphRAGResult):
        """Explain the reasoning process"""
        print(f"\n{'='*50}")
        print("GRAPHRAG REASONING EXPLANATION")
        print(f"{'='*50}")
        
        print(f"Confidence: {result.confidence:.3f}")
        print(f"Sources used: {', '.join(result.graph_context.get('retrieval_sources', []))}")
        print(f"Nodes retrieved: {result.graph_context.get('total_nodes_retrieved', 0)}")
        
        if result.reasoning_paths:
            print(f"\nReasoning Paths ({len(result.reasoning_paths)}):")
            for i, path in enumerate(result.reasoning_paths[:3]):
                print(f"  {i+1}. {path.reasoning} (score: {path.score:.3f})")
        
        if result.graph_context.get('cypher_query'):
            print(f"\nGenerated Cypher Query:")
            print(f"  {result.graph_context['cypher_query']}")
        
        print(f"\n{'='*50}")

def main():
    """Test the enhanced GraphRAG system"""
    try:
        graphrag = EnhancedGraphRAG()
        
        # Test queries
        test_queries = [
            "What is machine learning and how does it relate to data governance?",
            "Explain the relationship between bias and fairness in AI systems",
            "How can I implement a privacy-preserving machine learning system?"
        ]
        
        for query in test_queries:
            print(f"\nQuery: {query}")
            result = graphrag.query(query, explain=True)
            print(f"Answer: {result.answer}")
            print("-" * 80)
            
    except Exception as e:
        logger.error(f"Error in main: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()