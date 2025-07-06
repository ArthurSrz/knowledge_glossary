#!/usr/bin/env python3
"""
Test script for enhanced path discovery in HopRAG
"""

import networkx as nx
from hoprag_streamlit_app import HopRAGEngine

def test_enhanced_path_discovery():
    """Test the enhanced path discovery functionality"""
    
    # Build a richer knowledge graph for testing
    graph = nx.Graph()
    
    # AI/ML concepts with deeper connections
    concepts = {
        "AI Ethics": "AI Ethics encompasses moral principles and guidelines for developing responsible artificial intelligence systems. It addresses concerns about bias, fairness, transparency, and accountability in AI development.",
        "Bias": "Bias in AI refers to systematic prejudices embedded in algorithmic decision-making processes. These biases can lead to unfair treatment of certain groups and perpetuate societal inequalities.",
        "Fairness": "Fairness in AI ensures equitable treatment across different demographic groups and use cases. It requires careful consideration of how AI systems impact various populations and communities.",
        "Machine Learning": "Machine Learning enables computers to learn patterns from data without explicit programming. It forms the foundation of modern AI systems and requires high-quality data and careful model design.",
        "Data Quality": "Data Quality refers to the accuracy, completeness, and reliability of datasets used in AI systems. Poor data quality can significantly impact model performance and fairness.",
        "Model Performance": "Model Performance measures how well an AI system achieves its intended objectives. It includes metrics like accuracy, precision, recall, and other domain-specific measures.",
        "Privacy": "Privacy protection ensures individual data rights and confidentiality in AI applications. It involves implementing technical and legal safeguards to protect personal information.",
        "Data Protection": "Data Protection involves legal and technical measures to safeguard personal information. It encompasses regulations, policies, and technical implementations for data security.",
        "GDPR": "GDPR establishes comprehensive data protection regulations across the European Union. It provides individuals with rights over their personal data and imposes obligations on organizations.",
        "Algorithmic Transparency": "Algorithmic Transparency requires AI systems to be explainable and interpretable. It enables stakeholders to understand how decisions are made and builds trust in AI systems.",
        "Responsible AI": "Responsible AI integrates ethical considerations throughout the AI development lifecycle. It ensures that AI systems are developed and deployed in ways that benefit society while minimizing harm."
    }
    
    # Add nodes to graph
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    # Add realistic edges with meaningful relations
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("AI Ethics", "Fairness", "PROMOTES"),
        ("AI Ethics", "Responsible AI", "ENCOMPASSES"),
        ("AI Ethics", "Algorithmic Transparency", "REQUIRES"),
        ("Bias", "Fairness", "CONFLICTS_WITH"),
        ("Bias", "Model Performance", "DEGRADES"),
        ("Machine Learning", "Data Quality", "DEPENDS_ON"),
        ("Machine Learning", "Model Performance", "DETERMINES"),
        ("Machine Learning", "Bias", "CAN_INTRODUCE"),
        ("Data Quality", "Model Performance", "IMPACTS"),
        ("Data Quality", "Bias", "INFLUENCES"),
        ("Privacy", "Data Protection", "REQUIRES"),
        ("Privacy", "GDPR", "GOVERNED_BY"),
        ("Data Protection", "GDPR", "ENFORCED_BY"),
        ("Responsible AI", "Algorithmic Transparency", "REQUIRES"),
        ("Responsible AI", "Privacy", "PROTECTS"),
        ("Algorithmic Transparency", "Fairness", "ENABLES"),
        ("Fairness", "Responsible AI", "COMPONENT_OF")
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
    print(f"Average confidence: {sum(p.confidence for p in result.hop_paths) / len(result.hop_paths):.3f}")
    print(f"Path lengths: {[p.hop_count for p in result.hop_paths]}")
    
    for i, path in enumerate(result.hop_paths[:5]):  # Show top 5
        print(f"\nPath {i+1} (Confidence: {path.confidence:.3f}, Hops: {path.hop_count}):")
        print(f"  Entities: {' → '.join(path.entities)}")
        print(f"  Relations: {' → '.join(path.relations)}")
        print(f"  Chain: {path.reasoning_chain}")
    
    print("\n" + "="*80)
    print("GENERATED LINKEDIN POST:")
    print("="*80)
    print(result.reasoning_paper)
    print("="*80)
    
    # Verify improvements
    assert len(result.hop_paths) > 0, "No paths discovered"
    assert max(p.hop_count for p in result.hop_paths) >= 2, "No multi-hop paths found"
    assert len(set(tuple(p.entities) for p in result.hop_paths)) == len(result.hop_paths), "Paths are not diverse"
    
    print(f"\n✅ Enhanced path discovery test passed!")
    print(f"📊 Generated {len(result.hop_paths)} diverse reasoning paths")
    print(f"🔍 Maximum path depth: {max(p.hop_count for p in result.hop_paths)} hops")
    print(f"🎯 Average confidence: {sum(p.confidence for p in result.hop_paths) / len(result.hop_paths):.3f}")
    
    return result

if __name__ == "__main__":
    test_enhanced_path_discovery()