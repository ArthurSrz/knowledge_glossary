---
improvesAccuracyOf: "[[Retrieval Augmented Generation]]"
same:
  - "[[Hybrid search]]"
failureMode: "[[Tag Filter Vocabulary Mismatch]]"
---

# Filtered Vector Search

Narrows the vector search space using metadata filters (tags, categories, date ranges)
before semantic similarity is computed. Reduces latency and improves precision — when
filter vocabulary is consistent with ingestion vocabulary.

## Pre-filter Gate

Metadata filters applied *before* embedding search act as a hard gate: if the filter
returns zero candidates, semantic search never runs. High-quality embeddings become
irrelevant — the gate blocked everything upstream.

This means filter vocabulary must be consistent end-to-end:
- **Ingestion time**: tags assigned to documents
- **Query time**: tags passed as filter parameters

A mismatch produces silent zero-result failures that appear identical to "no relevant
documents exist."

## When to disable filtering

When filter vocabulary consistency cannot be guaranteed, set filters to `include_all`
and rely on semantic scoring + rerank to scope relevance. Reranking after retrieval
is a soft gate — it ranks rather than excludes.
