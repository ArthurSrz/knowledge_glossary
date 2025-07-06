#!/usr/bin/env python3
"""
Test script for content-aware LinkedIn post generation
"""

import networkx as nx
from hoprag_streamlit_app import HopRAGEngine

def test_content_aware_insights():
    """Test the enhanced content-aware insight generation"""
    
    # Build test graph with rich content
    graph = nx.Graph()
    
    # Rich, detailed concepts that should produce varied insights
    concepts = {
        "AI Ethics": """AI Ethics encompasses moral principles and guidelines for developing responsible artificial intelligence systems. It addresses concerns about bias, fairness, transparency, and accountability in AI development. Organizations must ensure their AI systems are designed with ethical considerations from the outset. Key principles include avoiding harm, ensuring fairness across different groups, maintaining transparency in decision-making processes, and implementing robust governance frameworks. Companies should establish ethics review boards and conduct regular audits of their AI systems.""",
        
        "Bias": """Bias in AI refers to systematic prejudices embedded in algorithmic decision-making processes that can lead to unfair treatment of certain groups. This occurs when training data contains historical inequalities or when algorithms amplify existing societal biases. Examples include facial recognition systems that perform poorly on darker skin tones, or hiring algorithms that discriminate against women. Organizations must implement bias detection tools, use diverse training datasets, and conduct regular fairness audits to mitigate these issues.""",
        
        "Data Quality": """Data Quality refers to the accuracy, completeness, consistency, and reliability of datasets used in AI and machine learning systems. Poor data quality can significantly impact model performance and lead to erroneous conclusions. Key dimensions include accuracy (correctness of data), completeness (no missing values), consistency (uniform format), timeliness (up-to-date information), and validity (data conforms to business rules). Companies should invest 60-80% of their time in data cleaning and validation processes before model training.""",
        
        "Privacy": """Privacy protection ensures individual data rights and confidentiality in AI applications through technical and legal safeguards. This includes implementing data minimization principles, obtaining proper consent, and using privacy-preserving techniques like differential privacy and federated learning. Organizations must comply with regulations such as GDPR and CCPA, which grant individuals rights to access, rectify, and delete their personal data. Privacy-by-design should be integrated into all AI system architectures from the beginning.""",
        
        "Model Performance": """Model Performance measures how well an AI system achieves its intended objectives using metrics like accuracy, precision, recall, F1-score, and AUC. However, performance should not be evaluated solely on technical metrics but also consider fairness, robustness, and real-world impact. Organizations should establish baseline performance thresholds, monitor models continuously in production, and implement automated retraining pipelines when performance degrades. A/B testing and shadow mode deployment can help validate model improvements before full rollout."""
    }
    
    # Add nodes to graph
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    # Add meaningful relationships
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("AI Ethics", "Privacy", "ENCOMPASSES"),
        ("Bias", "Data Quality", "CAUSED_BY"),
        ("Data Quality", "Model Performance", "DETERMINES"),
        ("Privacy", "Data Quality", "CONSTRAINS")
    ]
    
    for src, dst, relation in edges:
        graph.add_edge(src, dst, relation=relation)
    
    # Test the enhanced engine
    engine = HopRAGEngine(graph, concepts)
    
    print("="*80)
    print("CONTENT-AWARE LINKEDIN POST GENERATION TEST")
    print("="*80)
    
    question = "How can organizations build trustworthy AI systems?"
    print(f"Question: {question}")
    print("="*80)
    
    # Test with content-aware generation
    result = engine.query(question, max_hops=3, top_k=5)
    
    print("GENERATED LINKEDIN POST:")
    print("="*80)
    print(result.reasoning_paper)
    print("="*80)
    
    # Test with different question to show variety
    print("\n" + "="*80)
    print("TESTING VARIETY WITH DIFFERENT QUESTION")
    print("="*80)
    
    question2 = "What are the biggest challenges in data science projects?"
    print(f"Question: {question2}")
    print("="*80)
    
    result2 = engine.query(question2, max_hops=3, top_k=5)
    
    print("GENERATED LINKEDIN POST:")
    print("="*80)
    print(result2.reasoning_paper)
    print("="*80)
    
    # Compare the two results
    print("\n" + "="*40)
    print("CONTENT COMPARISON ANALYSIS")
    print("="*40)
    
    # Check if posts are different
    post1_insights = result.reasoning_paper.split("💡 **Insight #")
    post2_insights = result2.reasoning_paper.split("💡 **Insight #")
    
    print(f"Post 1 insights: {len(post1_insights)-1}")
    print(f"Post 2 insights: {len(post2_insights)-1}")
    
    # Check for content uniqueness
    post1_content = result.reasoning_paper
    post2_content = result2.reasoning_paper
    
    similarity = len(set(post1_content.split()) & set(post2_content.split())) / len(set(post1_content.split()) | set(post2_content.split()))
    print(f"Content similarity: {similarity:.2%}")
    
    if similarity < 0.7:
        print("✅ Posts show good variety and use different content!")
    else:
        print("⚠️ Posts are too similar - content extraction needs improvement")
    
    print(f"\n✅ Content-aware test completed!")
    
    return result, result2

if __name__ == "__main__":
    test_content_aware_insights()