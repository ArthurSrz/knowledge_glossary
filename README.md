# Data knowledge graph

### Daily Stats

![Knowledge Glossary Growth](stats/chart.png)

A personal knowledge graph containing **865 interconnected concepts** in data science, machine learning, and AI. Built as an [Obsidian](https://obsidian.md/) vault with typed relationships, this graph can serve as the foundation for a **data ontology**.

## Structure

Each concept is a markdown file with:
- **YAML frontmatter** defining typed relationships (`partOf`, `uses`, `subclass of`, etc.)
- **Definition/description** of the concept
- **Wiki-links** (`[[concept]]`) connecting to related terms

```yaml
# Example: Knowledge graph.md
---
uses:
  - "[[Ontology]]"
  - "[[Taxonomy]]"
subclass of:
  - "[[knowledge base]]"
  - "[[labeled directed graph]]"
studied in:
  - "[[Ontology engineering]]"
---
```

## Topics covered

- **Machine Learning**: Algorithms, model training, evaluation metrics, feature engineering
- **Data Engineering**: Pipelines, data lineage, ETL, data quality
- **NLP & LLMs**: Embeddings, RAG, transformers, prompt engineering
- **MLOps**: Model versioning, deployment, monitoring, drift detection
- **Data Privacy**: PII management, FERPA, compliance
- **Knowledge Representation**: Ontologies, taxonomies, knowledge graphs

## Potential uses as a data ontology

1. Semantic search & retrieval

Use the typed relationships to build a **GraphRAG system** that navigates concepts through their semantic connections rather than just keyword matching.

2. Data catalog enrichment

Import this ontology into a data catalog to provide standardized terminology and hierarchical classification for data assets across an organization.

3. Onboarding & training

Serve as an interactive learning resource for data teams, with concept definitions and relationship paths showing how ideas connect.

4. LLM grounding

Provide structured domain knowledge to LLMs for more accurate, consistent responses about data concepts—reducing hallucination through explicit relationship constraints.

5. Metadata schema design

Use the relationship types (`partOf`, `uses`, `subclass of`) as a blueprint for designing metadata schemas in data platforms.

6. Knowledge graph construction

Convert this vault into a formal knowledge graph (Neo4j, RDF) by:
- Extracting nodes from file names
- Parsing frontmatter for typed edges
- Enriching with definitions as node properties

7. Concept disambiguation

Establish canonical definitions and relationships to resolve ambiguity when different teams use data terminology inconsistently.

## Thesaurus — SKOS Broader/Narrower Hierarchy

The graph uses `broader:` in YAML frontmatter to encode [SKOS](https://www.w3.org/2004/02/skos/)-style hierarchical relationships. **701 of 866 concepts** (80.9%) are classified into a `broader` parent, forming 167 parent clusters.

The `broader:` property means "this concept is a subtype/subclass/instance of the parent" — equivalent to `skos:broader`. Reading in the opposite direction gives `skos:narrower`.

### Hierarchy by parent concept

| Broader (parent) | Narrower (children) |
|---|---|
| Agentic System | action module, agency, agent harness, agent identity, agent role type, Autonomy, claude code, claude managed agents, comparag agent, context mode, Human-in-the-loop, Model Context Protocol (MCP), ReAct data agent, ReAct mode, search module, Subagent, Tool arena, Tool Assignment Gate, Toolkits, Tools |
| AI | AI engineering, AI Hierarchy of needs, AI Proof detection model, AI stack, Artificial Intelligence (AI), claude cowork, compilatio IA, Fiabilite de compilatio, HGR-AI-1, Man-Computer Symbiosis, The Shift from Models to Compound AI Systems |
| AI prompt | chain-of-thought, Prompt Identity, Prompt Optimization Techniques, Prompt Template Info, Prompt Template Types, Prompt templates, Prompt-based techniques, prompts, system prompt |
| Application development | API toolset, Backend, Data processing toolset, Dependency injection, DevOps, Documentation, Frontend, Hook, License, Log, Open source software, Package installer, Plugins, Programming language, Readme file, Scenario (computing), Session, Software Development Kit (SDK), Web worker, application programming interface, boilerplate, bundle, callback, collaboration tools, control flow, default, exception handling, idempotence, implementation detail, macros, parsing, query, scenario, settings.json |
| Artificial Intelligence (AI) | Agentic System, compound AI systems, computer vision, connexionism, Expert systems, Narrow AI, Natural Language Processing, Symbolism |
| artificial neural network | artificial neuron, autoencoder, Backpropagation, biological neural network, Convolutional neural networks, Embedding network, Forward propagation, Hidden states, multilayer perceptron, neuron layer, ReLU activation function, Sigmoid function, Weights |
| Backend | celery, Django, PostgreSQL, Redis |
| Bayesian inference | Bayesian epistemology, Bayesian network, Théorie du cerveau bayésien |
| bias | Feedback loop bias, Historical bias, recall bias |
| Centrality | betweenness centrality, closeness centrality, Degree centrality, Eigenvector centrality |
| Clustering | Elbow method, K-Means Clustering |
| Confusion Matrix | False Negative (FN), False Positive (FP), True Negative (TN), True Positive (TP) |
| CRISP-DM Process | Data preparation, Deployment, Evaluate results, Explore the data, Gather data, Identify factors, modeling, Prepare for modeling, Problem definition, Test solution |
| data | Data quality, Data quantity, Data silos, data type, Datum, index, metadata, open data, raw data |
| Data preparation | feature engineering, Label encoding, Min-max normalization, One-hot encoding, Split data, Tidy Data, Validate data, Z-Score normalization |
| Data privacy | Data privacy laws, Fair Information Practices, Financial Privacy, Management of PII, Medical Data Privacy, Privacy by design, Rights of Individuals, Sensitive Information, Technological privacy |
| Data quality | class imbalance, completeness, missing at random, missing completely at random, missing not at random, Outliers |
| Data science team | Data engineer, Data scientist, Engineering team, Machine learning engineer, Software engineer |
| data type | continuum data, JSON, Semi-structured data, Spatial Reference System Identifier (SRID), Structured data, Unstructured data |
| Decision tree | Random forest, Recursive tree building, Regression trees, Tree depth |
| Deep learning | artificial neural network, foundation model, Keras, Transfer learning, Transformers |
| Design thinking | Don Norman's principles of Interaction Design, Empathy, Ideate, Perception, Simplicity VS. Flexibility, Standford's design thinking process, User research |
| Embeddings | embedding, Embeddings models, latent space, vectorization, Word embeddings |
| Evaluation | Cross validation, detection tool performance, Evaluation dataset, Evaluation metrics, Hindsight scenario testing |
| Evaluation metrics | accuracy, coefficient of determination, confusion matrix, F1 Score, False Positive Rate, LLM Metrics, Perplexity, Precision, Recall, Receiver Operating Characteristic curve, Regression Error Metrics, True Positive Rate (Recall) |
| Fairness | accountable AI, bias, Data privacy, Ethical checklist, Ethical risks, Fair AI, Individual fairness, Transparency |
| feature selection | Embedded methods, Filter methods, Principal Component Analysis, Wrapper methods |
| Fine-tuning | Instruction dataset, Low-Rank Adaptation, supervised finetuning, Unsloth |
| Git | add, branch -vv, checkout, checkout -b, commit, commit amend, Git worktree, Github, Pull request, Staging Area, Stash, Working directory |
| Graph algorithm | centrality, community detection, Dijkstra's shortest path, Node similarity |
| Graph theory | adjacency matrix, Arc, complete graph, Edges, Graph network analysis, Graph projection, Heterogeneous graph, Multipartite graph, Network graph, node, Path, Property graph model |
| Hugging Face | AutoModel, Autotokenizer, DatasetDict, Datasets, Trainer, TrainingAguments |
| Inference | backward chaining, Batch prediction, causal inference, Inference engine, Inference pipeline, Online prediction |
| Infrastructure | authentication protocol, central processing unit, cloud computing, communication protocol, Datawarehouse, Dedicated server, Deploy, Environment, Fault tolerance, Graphics processing unit, Horizontal scaling, HTTP, IAM execution role, Layered architecture, Memory, Message-oriented middleware, modularity, NoSQL database, persistence, Personal computing resources, Service-oriented architecture (SOA), Shards, Shared computing resources, SSH Agent, Virtualization, VRAM |
| Interpretability | Counterfactual explanations, Local Interpretable Model-Agnostic Explanations (LIME), Shapley Additive Explanations (SHAP) |
| knowledge graph | adar-Adamic index, alias, context graph, CYPHER, graph hop, graphs, inferred from attribute of entity, Ingoing relationships, list of values as qualifiers, Object, Outgoing relationships, Properties, Property, Relationship aggregation, Relationship quality, Text2Cypher |
| knowledge organization system | concept, controlled vocabulary, model vocabulary, Ontology, organizing principles, subject heading, taxonomy, thesaurus |
| Language modeling | autoregressive language models, Large Language Model, masked language models |
| Large Language Model | AI prompt, chat engines, chat modes, Hallucination, In-Context Learning, LLaMA, LLM Models, LLM Path Extractors, moderation, Ollama, RAG (Retrieval-Augmented Generation), Retrieval Augmented Generation |
| machine learning | AutoML, Edge ML, Federated learning, Hyperparameters, loss function, ML system, Optimizer algorithm, Regularization, Reinforcement Learning, supervised learning, training algorithm, Unsupervised Learning |
| Metric | business impact, Information Gain (IG), Learning curve, Margin, measure, r2, reach, Similarity scores, Threshold value |
| ML models | Decoders model, feature, Feature bagging, Inherent error, Instructor model, Linear models, Machine Leaning Baseline, Neural network models, Offline models, Online models, optimizer, other-losses, parameter, prediction, Support vector, Target, Train loss |
| ML system | best-classification-rate AI detection system, cold start problem, Excessive latency, machine learning systems, ML system design process, ML System failures, Nano-precision detection system, Reproducibility |
| Model maintenance | ML system monitoring, Model decay, Model registry, model versioning, Retraining, Scheduled retraining |
| Model tuning | Fine-tuning, Pruning, Quantization |
| Natural Language Processing | Bag of words, Embeddings, Language modeling, Sentiment analysis, token, Tokenizer |
| Pipelines | Delta live tables, Feature pipeline, Ingestion, Training pipeline |
| Probability | Bayes' theorem, confidence interval, Odds, probability measure, variance |
| Process | Application development, cadence, change management, collaborators, context, continuous learning, crawl-walk-run, data, Design thinking, Experimentation, Feasability, Feedback, Goals, Instructions, knowledge, Management, Mapping, monitor, Situation, stability, Stretch pants approach, type of process, Updating, Visibility |
| Product | brief mission, customization, Feature-list, newsletter, Personalization, Powerpoint, product packaging, Project description, Project Title, Slide deck, Speckit, Spotify story, Technology-list |
| Programming language | App script, Elixir, functional programming, Java, Mark-up language, Python, Visual Basic Application |
| Python | CountVectorizer, Hugging Face, Jupyter notebooks, Matplotlib, Numpy, openpyxl, Pandas, Pydantic, Pypi, PyTorch, Sci-kit Learn, SpaCy, Virtual Environment |
| RAG (Retrieval-Augmented Generation) | condense_plus_context, condense_question, Hypothetical Document Embeddings (HyDE), Retrieval Depth, Retriever, Retriever Orchestration, vanilla RAG design |
| Schema design | Denormalized schema, Nested schema, Normalized schema, Schema-field consumption statistics |
| semantics | discourse topic, implicature, implicitness, latent, latent travel, meaning, null morpheme, subtext |
| Shareholders agreement | abuse of majority, Blocking minority, minority interest vs full ownership, Share transfer clauses |
| spreadsheet | active cell, calculated-fields, conditional-formatting, cross-sheet source references, excel, Excel vs. Gsheet problem, google sheet, handled-vs-gaps, named-ranges, partial column range, platform-limits, separators-and-dates, sheets-api, sparkline, structured-references, table cell, theme color |
| Stochastic processes | constancy, continuity, Impermanence, Independent Cascade Model, permanence, Smoothing |
| supervised learning | Decision tree, K-Nearest Neighbor algorithm, Naive Bayes Classifier, Support Vector Machine |
| systems theory | Equifinality, Feedback loops, Flywheel effect, study of complex systems |
| Transformers | attention weights, Decoder-only, Encoder-only |
| User research | Task analysis, Task flow diagram, User inputs, User outputs, User support, User tests, User training, UX Problem Statement |
| Vector space | Distance, Geometric concept, manifold, Tensors, vector |
| version control | Artifact Management, Git, Repository, rollback, rollback capability, Traceable Artifacts |

*Showing parent concepts with 3+ children. Full hierarchy includes 167 parents across 701 classified concepts.*

## Usage

Open the `graph/` folder in [Obsidian](https://obsidian.md/) to explore the knowledge graph visually using the Graph View.

To convert to other formats:
- **Neo4j**: Parse markdown frontmatter into Cypher CREATE statements
- **RDF/OWL**: Map relationship types to predicates — `broader:` maps directly to `skos:broader`
- **JSON-LD**: Export as linked data for web interoperability


