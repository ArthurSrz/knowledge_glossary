# GraphRAG Legacy Files

This directory contains legacy GraphRAG implementation files that have been superseded by the new HopRAG implementation in the parent directory.

## 📁 Current Contents

### Core Implementation Files
- **`enhanced_graphrag.py`** - Enhanced GraphRAG implementation with multi-hop reasoning
- **`interactive_graphrag.py`** - Interactive Streamlit interface for GraphRAG

### Jupyter Notebooks
- **`coreandgraph_engine_maker.ipynb`** - Notebook for creating graph indices and storage contexts
- **`coreandgraph_query.ipynb`** - Notebook for querying the knowledge graph

### Persisted Data
- **`onto_graph/`** - Directory containing persisted graph indices and storage
  - `docstore.json` - Document storage
  - `graph_store.json` - Graph relationships storage
  - `index_store.json` - Index metadata
  - `property_graph_store.json` - Property graph storage
  - `default__vector_store.json` - Default vector embeddings
  - `image__vector_store.json` - Image embeddings (if any)

## 🔄 Migration Status

These files have been superseded by the new HopRAG implementation:

- ✅ **Replaced by**: `../hoprag_streamlit_app.py` (Basic HopRAG)
- ✅ **Replaced by**: `../hoprag_hf_enhanced.py` (Enhanced HopRAG with HF integration)
- ✅ **Replaced by**: `../launch_hoprag.py` (Easy launcher)

## 🚀 New HopRAG Features

The new implementation provides:
- **Multi-hop reasoning** following the HopRAG paper methodology
- **Hugging Face integration** for enhanced model capabilities
- **Better visualization** with interactive graph displays
- **Export capabilities** for results and analysis
- **Improved user interface** with configuration options

## 💡 Usage Recommendation

**For new projects**: Use the new HopRAG implementation in the parent directory.

**For reference**: These legacy files can be useful for:
- Understanding the evolution of the system
- Accessing specific LlamaIndex implementations
- Debugging legacy functionality
- Academic reference for GraphRAG approaches

## 🗂️ File Purposes

### Python Files
- **`enhanced_graphrag.py`** - Multi-index GraphRAG implementation with Text2Cypher
- **`interactive_graphrag.py`** - Streamlit interface for the enhanced GraphRAG

### Jupyter Notebooks
- **`coreandgraph_engine_maker.ipynb`** - Creates and persists graph indices
- **`coreandgraph_query.ipynb`** - Interactive querying and testing

### Persisted Data (`onto_graph/` - 4.8MB)
- **`default__vector_store.json`** (4.3MB) - Vector embeddings for concepts
- **`property_graph_store.json`** (0.5MB) - Property graph relationships
- **`docstore.json`** (0.05MB) - Document storage with metadata
- **`index_store.json`** (minimal) - Index metadata and configuration

## ✅ Cleanup Completed

**Removed files:**
- ❌ `OntoGraph.html` - Large static visualization (62KB)
- ❌ `lib/` directory - JavaScript dependencies (not needed)
- ❌ `.DS_Store` - macOS system file
- ❌ `image__vector_store.json` - Empty image vectors
- ❌ `graph_store.json` - Empty graph storage

**Retained useful files:**
- ✅ Core Python implementations (reference)
- ✅ Jupyter notebooks (development/testing)
- ✅ Persisted indices (4.8MB total - reasonable size)
- ✅ Documentation and utilities

## 🔧 Maintenance

These files are kept for reference and backup. The persisted data can be useful for:
- Quick loading of pre-built indices
- Fallback if new HopRAG system needs debugging
- Academic reference for LlamaIndex GraphRAG approaches

---

**Last Updated**: July 2025  
**Migration Completed**: ✅  
**Status**: Legacy/Reference Only