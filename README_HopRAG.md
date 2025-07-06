# HopRAG - Knowledge-Intensive AI System

A Streamlit application implementing HopRAG (Hop-based Retrieval Augmented Generation) for knowledge-intensive AI queries over your knowledge graph.

## 🔥 Features

### Core HopRAG Implementation
- **Multi-hop reasoning** across your knowledge graph
- **Entity recognition and linking** from natural language queries
- **Path discovery** with confidence scoring
- **Evidence aggregation** from multiple reasoning paths
- **Interactive visualization** of reasoning paths

### Enhanced Version Features
- **Hugging Face model integration** for enhanced reasoning
- **AI-generated insights** and explanations
- **Export capabilities** (JSON, CSV, Markdown, PDF)
- **Advanced analytics** and graph statistics
- **Enhanced visualizations** with confidence mapping

## 🚀 Quick Start

### 1. Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
# Use the launcher script
python launch_hoprag.py

# Or run directly
streamlit run hoprag_streamlit_app.py
```

### 3. Access the Application
Open your browser and go to: `http://localhost:8501`

## 📊 System Overview

### Knowledge Graph Structure
- **Nodes**: AI/ML concepts from your markdown files
- **Edges**: Relationships extracted from content
- **Properties**: Metadata and content from each concept

### HopRAG Process
1. **Query Processing**: Extract entities from user question
2. **Path Discovery**: Find multi-hop reasoning paths
3. **Evidence Aggregation**: Collect supporting evidence
4. **Answer Generation**: Synthesize final response
5. **Visualization**: Display reasoning paths and insights

## 🔧 Configuration Options

### Query Parameters
- **Maximum Hops**: Control reasoning depth (1-5)
- **Top K Paths**: Number of paths to explore (1-20)
- **Confidence Threshold**: Minimum path confidence

### Display Options
- **Show Reasoning Paths**: View detailed reasoning
- **Graph Visualization**: Interactive network graphs
- **Export Results**: Save queries and results

### HF Enhancements (Enhanced Version)
- **Enhanced Reasoning**: AI-improved explanations
- **Generated Insights**: Additional analysis
- **Model Integration**: Hugging Face model access

## 📁 File Structure

```
knowledge_glossary/
├── hoprag_streamlit_app.py       # Basic HopRAG implementation
├── hoprag_hf_enhanced.py         # Enhanced version with HF integration
├── launch_hoprag.py              # Launcher script
├── requirements.txt              # Dependencies
├── README_HopRAG.md             # This file
└── graph/                       # Knowledge graph source files
    ├── *.md                     # Concept definitions
    └── subgraph/               # Subcategories
```

## 🎯 Example Queries

### Basic Queries
- "What is machine learning?"
- "How does bias affect AI fairness?"
- "What are privacy concerns in ML?"

### Multi-hop Reasoning Queries
- "What is the relationship between data governance and AI ethics?"
- "How do privacy regulations impact machine learning deployment?"
- "What are the connections between AutoML and model interpretability?"

### Complex Knowledge-Intensive Queries
- "How can I implement a privacy-preserving machine learning system that addresses both technical and regulatory requirements?"
- "What are the key considerations for deploying AI systems in healthcare while maintaining patient privacy and ensuring fairness?"

## 🔍 Understanding Results

### Answer Components
- **Main Answer**: Direct response to your question
- **Confidence Score**: System confidence in the answer
- **Reasoning Paths**: Step-by-step reasoning chains
- **Supporting Evidence**: Source material from knowledge graph

### Visualization Elements
- **Node Size**: Importance in reasoning
- **Edge Color**: Relationship type
- **Path Highlighting**: Different reasoning paths
- **Confidence Mapping**: Visual confidence indicators

## 🤖 Hugging Face Integration

The enhanced version integrates with Hugging Face models for:

### Enhanced Reasoning
- Improved explanation generation
- Better entity linking
- More sophisticated path scoring

### AI Insights
- Pattern analysis across reasoning paths
- Relationship frequency analysis
- Knowledge gap identification

### Export Capabilities
- Structured data export
- Report generation
- Analysis preservation

## 📤 Export Options

### Available Formats
- **JSON**: Structured data export
- **CSV**: Tabular path analysis
- **Markdown**: Human-readable reports
- **PDF**: Formatted reports (planned)

### Export Contents
- Query and timestamp
- Answer with confidence
- All reasoning paths
- Supporting evidence
- System metadata

## 🛠️ Customization

### Adding New Concepts
1. Add markdown files to the `graph/` directory
2. Use `[[concept_name]]` links for relationships
3. Restart the application to reload

### Modifying Reasoning
- Adjust path scoring algorithms
- Modify entity extraction methods
- Customize visualization layouts

### Integration Options
- Connect to external knowledge bases
- Add custom model endpoints
- Implement specialized reasoning modules

## 🚨 Troubleshooting

### Common Issues
1. **Import Errors**: Install missing dependencies
2. **Memory Issues**: Reduce max_hops or top_k_paths
3. **Slow Performance**: Enable caching, reduce graph size
4. **Visualization Problems**: Check browser compatibility

### Performance Tips
- Use shorter concept descriptions
- Limit reasoning depth for complex queries
- Cache embeddings for repeated queries
- Optimize graph structure

## 🔮 Future Enhancements

### Planned Features
- Real-time graph updates
- Advanced NLP models
- Multi-modal reasoning
- Collaborative querying
- API endpoints

### Integration Roadmap
- Vector databases
- LLM fine-tuning
- Graph neural networks
- Explainable AI methods

## 📚 References

- [HopRAG Paper](https://arxiv.org/abs/2502.12442)
- [Hugging Face Models](https://huggingface.co/models)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [NetworkX Documentation](https://networkx.org/)

## 🤝 Contributing

Feel free to enhance the system by:
- Adding new reasoning algorithms
- Improving visualization
- Integrating additional models
- Optimizing performance

## 📄 License

This project is for educational and research purposes. Please respect the licenses of integrated models and libraries.

---

**Built with ❤️ using Streamlit, Hugging Face, and NetworkX**