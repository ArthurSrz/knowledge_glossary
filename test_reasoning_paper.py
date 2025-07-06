#!/usr/bin/env python3
"""
Test script for reasoning paper generation in HopRAG
"""

import sys
import os
import networkx as nx
sys.path.append('/Users/arthursarazin/Documents/knowledge_glossary')

# Import after path setup
from hoprag_streamlit_app import HopRAGEngine, KnowledgeGraphLoader, HopPath

def test_reasoning_paper_generation():
    """Test the enhanced path discovery and LinkedIn post generation"""
    
    # Create a more comprehensive test graph
    
    # Build a richer knowledge graph for testing
    graph = nx.Graph()
    
    # AI/ML concepts with deeper connections
    concepts = {
        "AI Ethics": "AI Ethics encompasses moral principles and guidelines for developing responsible artificial intelligence systems.",
        "Bias": "Bias in AI refers to systematic prejudices embedded in algorithmic decision-making processes.",
        "Fairness": "Fairness in AI ensures equitable treatment across different demographic groups and use cases.",
        "Machine Learning": "Machine Learning enables computers to learn patterns from data without explicit programming.",
        "Data Quality": "Data Quality refers to the accuracy, completeness, and reliability of datasets used in AI systems.",
        "Model Performance": "Model Performance measures how well an AI system achieves its intended objectives.",
        "Privacy": "Privacy protection ensures individual data rights and confidentiality in AI applications.",
        "Data Protection": "Data Protection involves legal and technical measures to safeguard personal information.",
        "GDPR": "GDPR establishes comprehensive data protection regulations across the European Union.",
        "Algorithmic Transparency": "Algorithmic Transparency requires AI systems to be explainable and interpretable.",
        "Responsible AI": "Responsible AI integrates ethical considerations throughout the AI development lifecycle.",
        "Data Governance": "Data Governance establishes policies and procedures for managing organizational data assets.",
        "Model Interpretability": "Model Interpretability enables understanding of how AI systems make decisions.",
        "Regulatory Compliance": "Regulatory Compliance ensures AI systems meet legal and industry standards."
    }
    
    # Add nodes to graph
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    # Add realistic edges with relations
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("AI Ethics", "Fairness", "PROMOTES"),
        ("AI Ethics", "Responsible AI", "ENCOMPASSES"),
        ("Bias", "Fairness", "CONFLICTS_WITH"),
        ("Bias", "Model Performance", "DEGRADES"),
        ("Machine Learning", "Data Quality", "DEPENDS_ON"),
        ("Machine Learning", "Model Performance", "DETERMINES"),
        ("Data Quality", "Model Performance", "IMPACTS"),
        ("Privacy", "Data Protection", "REQUIRES"),
        ("Privacy", "GDPR", "GOVERNED_BY"),
        ("Data Protection", "GDPR", "ENFORCED_BY"),
        ("Data Protection", "Data Governance", "PART_OF"),
        ("Responsible AI", "Algorithmic Transparency", "REQUIRES"),
        ("Responsible AI", "Model Interpretability", "INCLUDES"),
        ("Algorithmic Transparency", "Model Interpretability", "ENABLES"),
        ("Model Interpretability", "Regulatory Compliance", "SUPPORTS"),
        ("GDPR", "Regulatory Compliance", "DEFINES"),
        ("Data Governance", "Regulatory Compliance", "ENSURES"),
        ("Fairness", "Responsible AI", "COMPONENT_OF"),
        ("AI Ethics", "Data Governance", "INFLUENCES")
    ]
    
    for src, dst, relation in edges:
        graph.add_edge(src, dst, relation=relation)
    
    # Test the enhanced engine
    engine = HopRAGEngine(graph, concepts)
    
    # Test with a complex question
    question = "How do ethical considerations impact AI system development?"
    
    print("="*80)
    print("ENHANCED PATH DISCOVERY TEST")
    print("="*80)
    print(f"Graph: {len(graph.nodes)} nodes, {len(graph.edges)} edges")
    print(f"Question: {question}")
    print("="*80)
    
    # Test the enhanced path discovery
    result = engine.query(question, max_hops=5, top_k=10)
    
    print(f"\nDiscovered {len(result.hop_paths)} high-quality reasoning paths:")
    for i, path in enumerate(result.hop_paths):
        print(f"\nPath {i+1} (Confidence: {path.confidence:.3f}, Hops: {path.hop_count}):")
        print(f"  Entities: {' → '.join(path.entities)}")
        print(f"  Relations: {' → '.join(path.relations)}")
    
    print("\n" + "="*80)
    print("GENERATED LINKEDIN POST:")
    print("="*80)
    print(result.reasoning_paper)
    print("="*80)
    
    # Create some mock hop paths for additional testing
    mock_hop_paths = result.hop_paths
    
    # Create a mock HopRAG engine instance
    from unittest.mock import Mock
    mock_engine = Mock()
    mock_engine.graph = Mock()
    mock_engine.graph.nodes = range(100)  # Mock 100 nodes
    mock_engine.concept_content = {}
    
    # Create actual engine instance to test the method
    from hoprag_streamlit_app import HopRAGEngine
    import networkx as nx
    
    # Create a simple test graph
    graph = nx.Graph()
    graph.add_nodes_from(["AI Ethics", "Bias", "Fairness", "Machine Learning", "Data Quality", "Model Performance", "Privacy", "Data Protection", "GDPR"])
    concept_content = {node: f"Content about {node}" for node in graph.nodes}
    
    engine = HopRAGEngine(graph, concept_content)
    
    # Test reasoning paper generation
    question = "How do ethical considerations impact AI system development?"
    reasoning_paper = engine._generate_reasoning_paper(question, mock_hop_paths)
    
    print("="*80)
    print("LINKEDIN POST GENERATION TEST")
    print("="*80)
    print(f"Question: {question}")
    print("="*80)
    print(reasoning_paper)
    print("="*80)
    
    # Verify the LinkedIn post has the expected structure
    assert "🤔" in reasoning_paper or "🔍" in reasoning_paper or "💭" in reasoning_paper or "🚀" in reasoning_paper
    assert "🧠 Let me break this down" in reasoning_paper
    assert "💡 **Insight #" in reasoning_paper
    assert "🎯 **Key Takeaways:**" in reasoning_paper
    assert "#DataScience" in reasoning_paper
    assert "💬 What's your experience" in reasoning_paper
    
    # Verify insights are included
    assert "Insight #1:" in reasoning_paper
    assert "Insight #2:" in reasoning_paper
    assert "Insight #3:" in reasoning_paper
    
    # Verify it's LinkedIn-friendly
    assert "✅" in reasoning_paper  # Checkmark for takeaways
    assert "🔬 Generated insights" in reasoning_paper
    
    print("\n✅ All tests passed! LinkedIn post generation is working correctly.")
    line_count = len(reasoning_paper.split('\n'))
    print(f"📱 Generated LinkedIn post has {line_count} lines")
    print(f"📊 Contains {len(mock_hop_paths)} reasoning paths")
    
    return reasoning_paper

if __name__ == "__main__":
    test_reasoning_paper_generation()