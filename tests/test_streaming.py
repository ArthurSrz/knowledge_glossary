#!/usr/bin/env python3
"""
Test script for streaming functionality in HopRAG
"""

import networkx as nx
import time
from hoprag_streamlit_app import HopRAGEngine

def test_streaming_functionality():
    """Test the streaming display functionality"""
    
    # Build test graph
    graph = nx.Graph()
    
    concepts = {
        "AI Ethics": "AI Ethics encompasses moral principles for responsible AI development.",
        "Bias": "Bias in AI refers to systematic prejudices in algorithmic decisions.",
        "Fairness": "Fairness ensures equitable treatment across different groups.",
        "Machine Learning": "Machine Learning enables computers to learn from data.",
        "Data Quality": "Data Quality refers to accuracy and reliability of datasets.",
        "Model Performance": "Model Performance measures AI system effectiveness.",
        "Privacy": "Privacy protection ensures individual data rights.",
        "Data Protection": "Data Protection involves safeguarding personal information.",
        "GDPR": "GDPR establishes EU data protection regulations.",
        "Algorithmic Transparency": "Algorithmic Transparency requires explainable AI systems.",
        "Responsible AI": "Responsible AI integrates ethical considerations throughout development."
    }
    
    # Add nodes and edges
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("AI Ethics", "Fairness", "PROMOTES"),
        ("AI Ethics", "Responsible AI", "ENCOMPASSES"),
        ("Bias", "Fairness", "CONFLICTS_WITH"),
        ("Machine Learning", "Data Quality", "DEPENDS_ON"),
        ("Privacy", "Data Protection", "REQUIRES"),
        ("Data Protection", "GDPR", "ENFORCED_BY"),
        ("Responsible AI", "Algorithmic Transparency", "REQUIRES"),
        ("Fairness", "Responsible AI", "COMPONENT_OF")
    ]
    
    for src, dst, relation in edges:
        graph.add_edge(src, dst, relation=relation)
    
    # Test streaming
    engine = HopRAGEngine(graph, concepts)
    
    def mock_stream_callback(message: str, msg_type: str = "info"):
        """Mock streaming callback for testing"""
        prefix = {
            "info": "ℹ️ ",
            "success": "✅ ",
            "path": "🔗 ",
            "abstract": "📄 "
        }.get(msg_type, "📝 ")
        
        print(f"{prefix}{message}")
        time.sleep(0.1)  # Simulate UI update delay
    
    print("="*80)
    print("STREAMING HOPRAG TEST")
    print("="*80)
    
    question = "How do ethical considerations impact AI system development?"
    print(f"Question: {question}")
    print("="*80)
    
    # Test with streaming
    result = engine.query(
        question, 
        max_hops=4, 
        top_k=8, 
        stream_callback=mock_stream_callback
    )
    
    print("\n" + "="*80)
    print("FINAL RESULTS")
    print("="*80)
    
    print(f"\n📊 Query Results:")
    print(f"- Paths discovered: {len(result.hop_paths)}")
    print(f"- Average confidence: {sum(p.confidence for p in result.hop_paths) / len(result.hop_paths):.1%}")
    print(f"- Max path depth: {max(p.hop_count for p in result.hop_paths)} hops")
    
    print(f"\n📄 Research Abstract:")
    print("-" * 40)
    print(result.research_abstract[:300] + "...")
    
    print(f"\n📱 LinkedIn Post Preview:")
    print("-" * 40)
    print(result.reasoning_paper[:400] + "...")
    
    print("\n✅ Streaming test completed successfully!")
    
    return result

if __name__ == "__main__":
    test_streaming_functionality()