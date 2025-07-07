#!/usr/bin/env python3
"""
Test script to compare improved LinkedIn post generation
"""

import networkx as nx
from hoprag_streamlit_app import HopRAGEngine

def test_linkedin_improvement():
    """Test the improved LinkedIn post generation"""
    
    # Build test graph with rich content
    graph = nx.Graph()
    
    concepts = {
        "AI Ethics": """AI Ethics encompasses moral principles and guidelines for developing responsible artificial intelligence systems. It addresses concerns about bias, fairness, transparency, and accountability in AI development. Organizations must ensure their AI systems are designed with ethical considerations from the outset. Key principles include avoiding harm, ensuring fairness across different groups, maintaining transparency in decision-making processes, and implementing robust governance frameworks.""",
        
        "Bias": """Bias in AI refers to systematic prejudices embedded in algorithmic decision-making processes that can lead to unfair treatment of certain groups. This occurs when training data contains historical inequalities or when algorithms amplify existing societal biases. Examples include facial recognition systems that perform poorly on darker skin tones, or hiring algorithms that discriminate against women. Organizations must implement bias detection tools, use diverse training datasets, and conduct regular fairness audits.""",
        
        "Data Quality": """Data Quality refers to the accuracy, completeness, consistency, and reliability of datasets used in AI and machine learning systems. Poor data quality can significantly impact model performance and lead to erroneous conclusions. Key dimensions include accuracy, completeness, consistency, timeliness, and validity. Companies should invest 60-80% of their time in data cleaning and validation processes before model training."""
    }
    
    # Add nodes to graph
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    # Add relationships
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("Bias", "Data Quality", "CAUSED_BY")
    ]
    
    for src, dst, relation in edges:
        graph.add_edge(src, dst, relation=relation)
    
    # Test the enhanced engine
    engine = HopRAGEngine(graph, concepts)
    
    print("="*80)
    print("IMPROVED LINKEDIN POST GENERATION TEST")
    print("="*80)
    
    question = "How can organizations ensure ethical AI development?"
    print(f"Question: {question}")
    print("="*80)
    
    # Generate improved LinkedIn post
    result = engine.query(question, max_hops=3, top_k=5)
    
    print("🎉 **IMPROVED LINKEDIN POST:**")
    print("="*80)
    print(result.reasoning_paper)
    print("="*80)
    
    # Analyze the improvements
    post_lines = result.reasoning_paper.split('\n')
    
    print(f"\n📊 **POST ANALYSIS:**")
    print(f"- Total lines: {len(post_lines)}")
    print(f"- Character count: {len(result.reasoning_paper)}")
    print(f"- Word count: {len(result.reasoning_paper.split())}")
    
    # Check for improvement indicators
    improvements = []
    
    if "hot take" in result.reasoning_paper.lower() or "here's what" in result.reasoning_paper.lower():
        improvements.append("✅ Engaging hook with personality")
    
    if "the bottom line:" in result.reasoning_paper.lower() or "here's the reality:" in result.reasoning_paper.lower():
        improvements.append("✅ Conversational explanation style")
    
    if "game changer" in result.reasoning_paper.lower() or "trust me" in result.reasoning_paper.lower():
        improvements.append("✅ Personal and engaging takeaways")
    
    if any(word in result.reasoning_paper.lower() for word in ["never", "always", "start", "focus on"]):
        improvements.append("✅ Action-oriented advice")
    
    if "need to make sure" in result.reasoning_paper.lower() or "it's" in result.reasoning_paper.lower():
        improvements.append("✅ LinkedIn-friendly language")
    
    print(f"\n🚀 **IDENTIFIED IMPROVEMENTS:**")
    for improvement in improvements:
        print(f"  {improvement}")
    
    if len(improvements) >= 3:
        print(f"\n🎯 **SUCCESS!** LinkedIn post shows significant improvement in {len(improvements)} areas!")
        return True
    else:
        print(f"\n⚠️ **NEEDS WORK:** Only {len(improvements)} improvements detected")
        return False

if __name__ == "__main__":
    success = test_linkedin_improvement()
    if success:
        print("\n🎉 LinkedIn post generation significantly improved!")
    else:
        print("\n🔧 LinkedIn post generation needs more work")