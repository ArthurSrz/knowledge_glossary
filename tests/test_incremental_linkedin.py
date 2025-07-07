#!/usr/bin/env python3
"""
Test script for incremental LinkedIn post building
"""

import networkx as nx
import time
from hoprag_streamlit_app import HopRAGEngine

def test_incremental_linkedin_building():
    """Test the incremental LinkedIn post building functionality"""
    
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
    print("INCREMENTAL LINKEDIN POST BUILDING TEST")
    print("="*80)
    
    # Track the incremental building
    linkedin_versions = []
    current_section = ""
    
    def incremental_stream_callback(message: str, msg_type: str = "info"):
        """Stream callback that tracks LinkedIn post building"""
        nonlocal current_section, linkedin_versions
        
        if msg_type == "linkedin_header":
            print(f"\n🎯 {message}")
            current_section = "header"
            
        elif msg_type == "linkedin_update":
            print(f"\n📝 **Post Update #{len(linkedin_versions) + 1}:**")
            print("-" * 40)
            print(message)
            print("-" * 40)
            linkedin_versions.append(message)
            
        elif msg_type == "linkedin_progress":
            print(f"  ⚡ {message}")
            
        elif msg_type == "linkedin_final":
            print(f"\n🎉 **FINAL LINKEDIN POST:**")
            print("=" * 60)
            print(message)
            print("=" * 60)
            
        elif msg_type in ["info", "success"]:
            print(f"  {message}")
            
        # Add visual delay to see the incremental building
        time.sleep(0.1)
    
    question = "How can organizations ensure ethical AI development?"
    print(f"Question: {question}")
    print("="*80)
    
    # Test the incremental generation
    result = engine.query(
        question, 
        max_hops=3, 
        top_k=5, 
        stream_callback=incremental_stream_callback
    )
    
    print(f"\n📊 **INCREMENTAL BUILDING ANALYSIS:**")
    print(f"- Total post versions tracked: {len(linkedin_versions)}")
    print(f"- Post grew from {len(linkedin_versions[0].split()) if linkedin_versions else 0} to {len(linkedin_versions[-1].split()) if linkedin_versions else 0} words")
    
    # Analyze the growth pattern
    if linkedin_versions:
        for i, version in enumerate(linkedin_versions):
            word_count = len(version.split())
            line_count = len(version.split('\n'))
            print(f"  Version {i+1}: {word_count} words, {line_count} lines")
    
    print(f"\n✅ Incremental LinkedIn post building test completed!")
    print(f"📱 Final post character count: {len(result.reasoning_paper)}")
    
    # Verify incremental building worked
    if len(linkedin_versions) > 1:
        print("✅ Successfully demonstrated incremental building!")
        return True
    else:
        print("❌ Incremental building not detected")
        return False

if __name__ == "__main__":
    success = test_incremental_linkedin_building()
    if success:
        print("\n🎉 All tests passed! Incremental LinkedIn building is working perfectly.")
    else:
        print("\n⚠️ Test failed - incremental building needs improvement.")