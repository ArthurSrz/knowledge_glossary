---
incorporatedInto: "[[Llama index]]"
---
There are three different LLM Path Extractors incorporated inside llama_index:

1. SimpleLLMPathExtractor
2. SchemaLLMPathExtractor
3. DynamicLLMPathExtractor (New)

###  SimpleLLMPathExtractor

```python
kg_extractor = SimpleLLMPathExtractor(
    llm=llm, max_paths_per_chunk=20, num_workers=4
)

simple_index = PropertyGraphIndex.from_documents(
    [document],
    llm=llm,
    embed_kg_nodes=False,
    kg_extractors=[kg_extractor],
   

kg_extractor = SimpleLLMPathExtractor( llm=llm, max_paths_per_chunk=20, num_workers=4 ) 

simple_index = PropertyGraphIndex.from_documents( [document], llm=llm, embed_kg_nodes=False, kg_extractors=[kg_extractor], show_progress=True, ) 

simple_index.property_graph_store.save_networkx_graph( name="./SimpleGraph.html" ) 

simple_index.property_graph_store.get_triplets( entity_names=["Barack Obama", "Obama"] )
```


### DynamicLLMPathExtractor without intial ontology 

Here, we let the LLM define the ontology on the fly, giving it full freedom to label the nodes as it best sees fit.


```python
kg_extractor = DynamicLLMPathExtractor(
    llm=llm,
    max_triplets_per_chunk=20,
    num_workers=4,
    # Let the LLM infer entities and their labels (types) on the fly
    allowed_entity_types=None,
    # Let the LLM infer relationships on the fly
    allowed_relation_types=None,
    # LLM will generate any entity properties, set `None` to skip property generation (will be faster without)
    allowed_relation_props=[],
    # LLM will generate any relation properties, set `None` to skip property generation (will be faster without)
    allowed_entity_props=[],
)

dynamic_index = PropertyGraphIndex.from_documents(
    [document],
    llm=llm,
    embed_kg_nodes=False,
    kg_extractors=[kg_extractor],
    show_progress=True,
)

dynamic_index.property_graph_store.save_networkx_graph(
    name="./DynamicGraph.html"
)

dynamic_index.property_graph_store.get_triplets(
    entity_names=["Barack Obama", "Obama"]
)
```


### ### With initial ontology for guided KG extraction :


Here, we have partial knowledge of what we want to detect, we know the article is about Barack Obama, so we define some entities and relations that could help guide the LLM in the labeling process as it detects the entities and relations. This doesn't guarantee that the LLM will use them, it simply guides it and gives it some ideas. It will still be up to the LLM to decide whether it uses the entities and relations we provide or not.

In [ ]:

kg_extractor = DynamicLLMPathExtractor(
    llm=llm,
    max_triplets_per_chunk=20,
    num_workers=4,
    allowed_entity_types=["POLITICIAN", "POLITICAL_PARTY"],
    allowed_relation_types=["PRESIDENT_OF", "MEMBER_OF"],
    allowed_relation_props=["description"],
    allowed_entity_props=["description"],
)

dynamic_index_2 = PropertyGraphIndex.from_documents(
    [document],
    llm=llm,
    embed_kg_nodes=False,
    kg_extractors=[kg_extractor],
    show_progress=True,
)

dynamic_index_2.property_graph_store.save_networkx_graph(
    name="./DynamicGraph_2.html"
)
dynamic_index_2.property_graph_store.get_triplets(
    entity_names=["Barack Obama", "Obama"]
)[:5]

kg_extractor = DynamicLLMPathExtractor( llm=llm, max_triplets_per_chunk=20, num_workers=4, allowed_entity_types=["POLITICIAN", "POLITICAL_PARTY"], allowed_relation_types=["PRESIDENT_OF", "MEMBER_OF"], allowed_relation_props=["description"], allowed_entity_props=["description"], ) dynamic_index_2 = PropertyGraphIndex.from_documents( [document], llm=llm, embed_kg_nodes=False, kg_extractors=[kg_extractor], show_progress=True, ) dynamic_index_2.property_graph_store.save_networkx_graph( name="./DynamicGraph_2.html" ) dynamic_index_2.property_graph_store.get_triplets( entity_names=["Barack Obama", "Obama"] )[:5]

Parsing nodes:   0%|          | 0/1 [00:00<?, ?it/s]

Extracting and inferring knowledge graph from text: 100%|██████████| 11/11 [00:47<00:00,  4.29s/it]

Out[ ]:

[(EntityNode(label='PERSON', embedding=None, properties={'description': '44th President of the United States', 'title': 'Barack Obama', 'triplet_source_id': 'd286a836-a5ad-43af-b6de-bd43f072512c'}, name='Obama'),
  Relation(label='MOVED_TO', source_id='Obama', target_id='Afghanistan', properties={'description': 'moved to bolster U.S. troop strength', 'title': 'Barack Obama', 'triplet_source_id': '23c1750d-de01-4a75-814e-b56b81b9bbb4'}),
  EntityNode(label='COUNTRY', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '23c1750d-de01-4a75-814e-b56b81b9bbb4'}, name='Afghanistan')),
 (EntityNode(label='POLITICIAN', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '8f9dc0b3-ff33-46e9-ad3f-040755d33fc7'}, name='Barack Obama'),
  Relation(label='ESTABLISHED', source_id='Barack Obama', target_id='White House Task Force to Protect Students from Sexual Assault', properties={'title': 'Barack Obama', 'triplet_source_id': '8af352da-b50d-4043-8002-870991473cf6'}),
  EntityNode(label='ORGANIZATION', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '8af352da-b50d-4043-8002-870991473cf6'}, name='White House Task Force to Protect Students from Sexual Assault')),
 (EntityNode(label='POLITICIAN', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '8f9dc0b3-ff33-46e9-ad3f-040755d33fc7'}, name='Barack Obama'),
  Relation(label='BECAME_CHAIRMAN_OF', source_id='Barack Obama', target_id="Illinois Senate\\'s Health and Human Services Committee", properties={'title': 'Barack Obama', 'triplet_source_id': '5bf11d65-0078-48bb-97b5-109b4469d46a'}),
  EntityNode(label='COMMITTEE', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '5bf11d65-0078-48bb-97b5-109b4469d46a'}, name="Illinois Senate\\'s Health and Human Services Committee")),
 (EntityNode(label='PERSON', embedding=None, properties={'description': '44th President of the United States', 'title': 'Barack Obama', 'triplet_source_id': 'd286a836-a5ad-43af-b6de-bd43f072512c'}, name='Obama'),
  Relation(label='USED', source_id='Obama', target_id='last day in office', properties={'description': 'used phrase "thanks, Obama"', 'title': 'Barack Obama', 'triplet_source_id': 'd286a836-a5ad-43af-b6de-bd43f072512c'}),
  EntityNode(label='EVENT', embedding=None, properties={'description': 'final day in office', 'title': 'Barack Obama', 'triplet_source_id': 'd286a836-a5ad-43af-b6de-bd43f072512c'}, name='last day in office')),
 (EntityNode(label='PERSON', embedding=None, properties={'description': '44th President of the United States', 'title': 'Barack Obama', 'triplet_source_id': 'd286a836-a5ad-43af-b6de-bd43f072512c'}, name='Obama'),
  Relation(label='SAID', source_id='Obama', target_id='34,000 U.S. troops', properties={'description': 'said the U.S. military would reduce the troop level in Afghanistan', 'title': 'Barack Obama', 'triplet_source_id': '23c1750d-de01-4a75-814e-b56b81b9bbb4'}),
  EntityNode(label='MILITARY_FORCE', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '23c1750d-de01-4a75-814e-b56b81b9bbb4'}, name='34,000 U.S. troops'))]

In [ ]:

kg_extractor = SchemaLLMPathExtractor(
    llm=llm,
    max_triplets_per_chunk=20,
    strict=False,  # Set to False to showcase why it's not going to be the same as DynamicLLMPathExtractor
    possible_entities=None,  # USE DEFAULT ENTITIES (PERSON, ORGANIZATION... etc)
    possible_relations=None,  # USE DEFAULT RELATIONSHIPS
    possible_relation_props=[
        "extra_description"
    ],  # Set to `None` to skip property generation
    possible_entity_props=[
        "extra_description"
    ],  # Set to `None` to skip property generation
    num_workers=4,
)

schema_index = PropertyGraphIndex.from_documents(
    [document],
    llm=llm,
    embed_kg_nodes=False,
    kg_extractors=[kg_extractor],
    show_progress=True,
)

schema_index.property_graph_store.save_networkx_graph(
    name="./SchemaGraph.html"
)
schema_index.property_graph_store.get_triplets(
    entity_names=["Barack Obama", "Obama"]
)[:5]

kg_extractor = SchemaLLMPathExtractor( llm=llm, max_triplets_per_chunk=20, strict=False, # Set to False to showcase why it's not going to be the same as DynamicLLMPathExtractor possible_entities=None, # USE DEFAULT ENTITIES (PERSON, ORGANIZATION... etc) possible_relations=None, # USE DEFAULT RELATIONSHIPS possible_relation_props=[ "extra_description" ], # Set to `None` to skip property generation possible_entity_props=[ "extra_description" ], # Set to `None` to skip property generation num_workers=4, ) schema_index = PropertyGraphIndex.from_documents( [document], llm=llm, embed_kg_nodes=False, kg_extractors=[kg_extractor], show_progress=True, ) schema_index.property_graph_store.save_networkx_graph( name="./SchemaGraph.html" ) schema_index.property_graph_store.get_triplets( entity_names=["Barack Obama", "Obama"] )[:5]

Parsing nodes:   0%|          | 0/1 [00:00<?, ?it/s]

Extracting paths from text with schema: 100%|██████████| 11/11 [00:52<00:00,  4.81s/it]

Out[ ]:

[(EntityNode(label='PERSON', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='Barack Obama'),
  Relation(label='HAS', source_id='Barack Obama', target_id='References', properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}),
  EntityNode(label='CONCEPT', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='References')),
 (EntityNode(label='PERSON', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='Barack Obama'),
  Relation(label='INTERCEPTED', source_id='Barack Obama', target_id='pipe bomb', properties={'title': 'Barack Obama', 'triplet_source_id': 'ada0abff-9671-4156-b06c-bf5067e6d54c'}),
  EntityNode(label='PRODUCT', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': 'ada0abff-9671-4156-b06c-bf5067e6d54c'}, name='pipe bomb')),
 (EntityNode(label='PERSON', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='Barack Obama'),
  Relation(label='HAS', source_id='Barack Obama', target_id='end of 2015', properties={'title': 'Barack Obama', 'triplet_source_id': '2b64d219-d19b-4346-a6a0-4369599af5d1'}),
  EntityNode(label='TIME', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '2b64d219-d19b-4346-a6a0-4369599af5d1'}, name='end of 2015')),
 (EntityNode(label='PERSON', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='Barack Obama'),
  Relation(label='GRADUATED_FROM', source_id='Barack Obama', target_id='Columbia University', properties={'title': 'Barack Obama', 'triplet_source_id': '65be5ae1-bc74-43ee-9655-855daf81f74f'}),
  EntityNode(label='ORGANIZATION', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '65be5ae1-bc74-43ee-9655-855daf81f74f'}, name='Columbia University')),
 (EntityNode(label='PERSON', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '87af3360-fa63-40c2-8440-f4114a7093fd'}, name='Barack Obama'),
  Relation(label='EDUCATION', source_id='Barack Obama', target_id='Schools and Universities', properties={'extra_description': 'Attended schools and universities', 'title': 'Barack Obama', 'triplet_source_id': '1f495d28-7df4-44dc-a3e3-bfc6161d3d2d'}),
  EntityNode(label='ORGANIZATION', embedding=None, properties={'title': 'Barack Obama', 'triplet_source_id': '1f495d28-7df4-44dc-a3e3-bfc6161d3d2d'}, name='Schools and Universities'))]

## Comparison and Analysis[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/Dynamic_KG_Extraction/#comparison-and-analysis)

Let's compare the results of the three extractors:

1. **SimpleLLMPathExtractor**: This extractor creates a basic knowledge graph without any predefined schema. It may produce a larger number of diverse relationships but might lack consistency in entity and relation naming.
    
2. **DynamicLLMPathExtractor**:
    
    - This new extractor combines the flexibility of SimpleLLMPathExtractor with some initial guidance from a schema. It can expand beyond the initial entity and relation types, potentially producing a rich and diverse graph while maintaining some level of consistency.
    - Not giving it any entities or relations to start with in the input gives the LLM complete freedom to infer the schema on the fly as it best sees fit. This is going to vary based on the LLM and the temperature used.
3. **SchemaLLMPathExtractor**: With a predefined schema, this extractor produces a more structured graph. The entities and relations are limited to those specified in the schema, which can lead to a more consistent but potentially less comprehensive graph. Even if we set "strict" to false, the extracted KG Graph doesn't reflect the LLM's pursuit of trying to find new entities and types that fall outside of the input schema's scope.
    

## Key observations:[¶](https://docs.llamaindex.ai/en/stable/examples/property_graph/Dynamic_KG_Extraction/#key-observations)

- The SimpleLLMPathExtractor graph might have the most diverse set of entities and relations.
- The SchemaLLMPathExtractor graph should be the most consistent but might miss a lot of relationships that don't fit the predefined schema, even if we don't impose a strict validation of the schema.
- The DynamicLLMPathExtractor graph should show a balance between diversity and consistency, potentially capturing important relationships that the schema-based approach might miss while still maintaining some structure.

- Use SimpleLLMPathExtractor for exploratory analysis where you want to capture a wide range of potential relationships for RAG applications, without caring about the entity types.
- Use SchemaLLMPathExtractor when you have a well-defined domain and want to ensure consistency in the extracted knowledge.
- Use DynamicLLMPathExtractor when you want a balance between structure and flexibility, allowing the model to discover new entity and relation types while still providing some initial guidance. This one is especially useful if you want a KG with labeled (typed) entities but don't have an input Schema (or you've partially defined the schema as a starting base).