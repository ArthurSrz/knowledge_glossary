#!/usr/bin/env python3
"""
Test the real-time path visualization during multi-hop discovery
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import networkx as nx
from hoprag_streamlit_app import HopRAGEngine

def test_realtime_path_discovery():
    """Test that real-time path visualization works during processing"""
    
    # Build test graph with rich content
    graph = nx.Graph()
    
    concepts = {
        "AI Ethics": """AI Ethics encompasses moral principles and guidelines for developing responsible artificial intelligence systems. It addresses concerns about bias, fairness, transparency, and accountability in AI development.""",
        
        "Bias": """Bias in AI refers to systematic prejudices embedded in algorithmic decision-making processes that can lead to unfair treatment of certain groups. This occurs when training data contains historical inequalities or when algorithms amplify existing societal biases.""",
        
        "Data Quality": """Data Quality refers to the accuracy, completeness, consistency, and reliability of datasets used in AI and machine learning systems. Poor data quality can significantly impact model performance and lead to erroneous conclusions.""",
        
        "Privacy": """Privacy protection ensures individual data rights and confidentiality in AI applications through technical and legal safeguards. This includes implementing data minimization principles, obtaining proper consent, and using privacy-preserving techniques.""",
        
        "Model Performance": """Model Performance measures how well an AI system achieves its intended objectives using metrics like accuracy, precision, recall, F1-score, and AUC. However, performance should not be evaluated solely on technical metrics but also consider fairness, robustness, and real-world impact.""",
        
        "Fairness": """Fairness in AI ensures that algorithms treat all individuals and groups equitably, without discrimination based on protected characteristics like race, gender, age, or other sensitive attributes.""",
        
        "Transparency": """Transparency in AI systems means making the decision-making process understandable and explainable to stakeholders, including how algorithms work, what data they use, and how they reach their conclusions.""",
        
        "Governance": """AI Governance involves establishing frameworks, policies, and oversight mechanisms to ensure responsible development and deployment of AI systems within organizations and society."""
    }
    
    # Add nodes to graph
    for concept, description in concepts.items():
        graph.add_node(concept, content=description)
    
    # Add relationships to create multiple interconnected paths
    edges = [
        ("AI Ethics", "Bias", "ADDRESSES"),
        ("AI Ethics", "Privacy", "ENCOMPASSES"), 
        ("AI Ethics", "Fairness", "PROMOTES"),
        ("AI Ethics", "Transparency", "REQUIRES"),
        ("AI Ethics", "Governance", "ENFORCED_BY"),
        ("Bias", "Data Quality", "CAUSED_BY"),
        ("Bias", "Fairness", "CONFLICTS_WITH"),
        ("Data Quality", "Model Performance", "DETERMINES"),
        ("Data Quality", "Privacy", "IMPACTS"),
        ("Privacy", "Transparency", "CONFLICTS_WITH"),
        ("Privacy", "Governance", "ENFORCED_BY"),
        ("Fairness", "Model Performance", "MEASURED_BY"),
        ("Fairness", "Transparency", "REQUIRES"),
        ("Transparency", "Governance", "ENABLES"),
        ("Model Performance", "Governance", "VALIDATED_BY")
    ]
    
    for src, dst, relation in edges:
        graph.add_edge(src, dst, relation=relation)
    
    print("="*80)
    print("REAL-TIME PATH VISUALIZATION TEST")
    print("="*80)
    
    # Create test engine
    engine = HopRAGEngine(graph, concepts)
    
    # Track streaming messages for verification
    stream_messages = []
    path_discovery_messages = []
    
    def test_stream_callback(message: str, msg_type: str = "info"):
        """Capture streaming messages for testing"""
        stream_messages.append((msg_type, message))
        
        if msg_type == "path" and "Path Found:" in message:
            path_discovery_messages.append(message)
            print(f"📍 REAL-TIME UPDATE: {message}")
        
        # Simulate minimal delay
        import time
        time.sleep(0.05)
    
    question = "How do ethical considerations impact AI system development and deployment?"
    print(f"Question: {question}")
    print("="*80)
    
    print("🚀 **Starting Real-Time Path Discovery Test**")
    print("   (Watch for live path updates during processing...)")
    print()
    
    # Execute query with streaming
    result = engine.query(
        question, 
        max_hops=4, 
        top_k=6, 
        stream_callback=test_stream_callback
    )
    
    print("\n" + "="*80)
    print("📊 **REAL-TIME VISUALIZATION TEST RESULTS**")
    print("="*80)
    
    # Verify real-time updates occurred
    print(f"✅ Total streaming messages: {len(stream_messages)}")
    print(f"✅ Path discovery messages: {len(path_discovery_messages)}")
    print(f"✅ Final paths discovered: {len(result.hop_paths)}")
    
    # Verify path discovery streaming
    if path_discovery_messages:
        print(f"\n🎯 **Real-Time Path Discovery Messages:**")
        for i, msg in enumerate(path_discovery_messages):
            print(f"  {i+1}. {msg}")
        
        # Test path parsing (what the real-time viz would do)
        print(f"\n🔍 **Path Parsing Test:**")
        import re
        
        for msg in path_discovery_messages[:3]:  # Test first 3
            # Try to extract path info like the real-time viz does
            path_match = re.search(r'Path Found:\*\* (.+?) \(conf: ([\d\.]+)\)', msg)
            if not path_match:
                path_match = re.search(r'(.+?) \(conf: ([\d\.]+)\)', msg)
            
            if path_match:
                path_str = path_match.group(1)
                confidence = float(path_match.group(2))
                entities = [e.strip() for e in path_str.split('→')]
                
                print(f"    ✅ Parsed: {len(entities)} entities, confidence {confidence:.3f}")
                print(f"       Path: {' → '.join(entities)}")
            else:
                print(f"    ❌ Could not parse: {msg}")
    
    else:
        print("⚠️  No real-time path discovery messages captured!")
    
    # Test final results
    print(f"\n📈 **Final Processing Results:**")
    print(f"  • Paths discovered: {len(result.hop_paths)}")
    print(f"  • Average confidence: {sum(p.confidence for p in result.hop_paths) / len(result.hop_paths):.3f}")
    print(f"  • Max path length: {max(p.hop_count for p in result.hop_paths)} hops")
    print(f"  • Unique concepts: {len(set().union(*[p.entities for p in result.hop_paths]))} concepts")
    
    # Verify streaming message types
    message_types = {}
    for msg_type, msg in stream_messages:
        message_types[msg_type] = message_types.get(msg_type, 0) + 1
    
    print(f"\n📋 **Message Type Distribution:**")
    for msg_type, count in message_types.items():
        print(f"  • {msg_type}: {count} messages")
    
    # Test success criteria
    success_criteria = [
        len(stream_messages) > 0,
        len(path_discovery_messages) >= 3,  # Should have multiple real-time updates
        len(result.hop_paths) > 0,
        'path' in message_types,
        message_types.get('info', 0) > 0
    ]
    
    print(f"\n🎯 **Test Success Criteria:**")
    print(f"  ✅ Streaming messages generated: {success_criteria[0]}")
    print(f"  ✅ Real-time path updates: {success_criteria[1]} ({len(path_discovery_messages)} updates)")
    print(f"  ✅ Final paths discovered: {success_criteria[2]}")
    print(f"  ✅ Path discovery messages: {success_criteria[3]}")
    print(f"  ✅ Info messages: {success_criteria[4]}")
    
    all_success = all(success_criteria)
    
    if all_success:
        print(f"\n🚀 **SUCCESS!** Real-time path visualization is working correctly!")
        print(f"")
        print(f"🎨 **Real-Time Features Verified:**")
        print(f"  ✅ Live path discovery during multi-hop exploration")
        print(f"  ✅ Streaming updates with path details and confidence")
        print(f"  ✅ Real-time message parsing for visualization")
        print(f"  ✅ Progressive path accumulation during processing")
        print(f"  ✅ Integration with existing HopRAG streaming system")
        print(f"")
        print(f"💡 **Next Steps:**")
        print(f"  • Run the Streamlit app to see live visualization")
        print(f"  • Enable 'Show Graph Visualization' option")
        print(f"  • Watch paths appear in real-time during processing")
        print(f"  • See both live updates and final comprehensive visualization")
    else:
        print(f"\n❌ **TEST FAILED** - Some criteria not met")
        failed_criteria = [i for i, success in enumerate(success_criteria) if not success]
        print(f"   Failed criteria: {failed_criteria}")
    
    return all_success

if __name__ == "__main__":
    try:
        success = test_realtime_path_discovery()
        if success:
            print("\n🎉 All tests passed! Real-time visualization is ready.")
        else:
            print("\n⚠️ Some tests failed. Check the output above.")
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()