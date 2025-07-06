#!/usr/bin/env python3
"""
Test script for reasoning paper generation in HopRAG
"""

import sys
sys.path.append('/Users/arthursarazin/Documents/knowledge_glossary')

from hoprag_streamlit_app import HopRAGEngine, KnowledgeGraphLoader, HopPath
import os

def test_reasoning_paper_generation():
    """Test the reasoning paper generation functionality"""
    
    # Create some mock hop paths for testing
    mock_hop_paths = [
        HopPath(
            entities=["AI Ethics", "Bias", "Fairness"],
            relations=["RELATED_TO", "AFFECTS"],
            evidence=[
                "AI Ethics is a crucial field that addresses moral and ethical implications of artificial intelligence systems.",
                "Bias in AI systems can lead to unfair treatment of certain groups and individuals.",
                "Fairness in AI requires careful consideration of how systems impact different populations."
            ],
            confidence=0.85,
            hop_count=2,
            reasoning_chain="AI Ethics → RELATED_TO → Bias → AFFECTS → Fairness"
        ),
        HopPath(
            entities=["Machine Learning", "Data Quality", "Model Performance"],
            relations=["DEPENDS_ON", "IMPACTS"],
            evidence=[
                "Machine Learning algorithms require high-quality training data to perform effectively.",
                "Data Quality is fundamental to building reliable and accurate AI systems.",
                "Model Performance is directly correlated with the quality of input data and training processes."
            ],
            confidence=0.78,
            hop_count=2,
            reasoning_chain="Machine Learning → DEPENDS_ON → Data Quality → IMPACTS → Model Performance"
        ),
        HopPath(
            entities=["Privacy", "Data Protection", "GDPR"],
            relations=["REQUIRES", "ENFORCED_BY"],
            evidence=[
                "Privacy is a fundamental right that must be protected in AI systems.",
                "Data Protection regulations establish frameworks for handling personal information.",
                "GDPR provides comprehensive guidelines for data processing and individual rights."
            ],
            confidence=0.72,
            hop_count=2,
            reasoning_chain="Privacy → REQUIRES → Data Protection → ENFORCED_BY → GDPR"
        )
    ]
    
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