---
related_to: [In-Context Learning, Knowledge Base, Information Retrieval, Vectorization]
dependencies: [Query, Knowledge Base, Text Vectors]
components: [Query, Retrieval Context, Knowledge Base, Text Vectors, Keyword, Source Doc]
category: Input Data Enhancement
tags: [RAG, Récupération_Information, Knowledge_Base, Vectorisation]
---

# RAG (Retrieval-Augmented Generation)

**Définition** : Technique utilisant une requête utilisateur pour matcher les sources de mémoire externe les plus pertinentes et intégrer ces informations dans le prompt comme contexte additionnel.

**Composants** :
- **Query** : Requête de recherche formulée par l'utilisateur
- **Retrieval Context** : Contexte récupéré depuis les sources externes
- **Knowledge Base** : Base de connaissances stockant les informations
- **Text Vectors** : Représentations vectorielles des textes pour la recherche
- **Keyword** : Mots-clés extraits pour affiner la recherche
- **Source Doc** : Documents sources originaux

**Processus RAG** :
1. **Encoding** : Conversion de la requête en vecteur
2. **Retrieval** : Recherche de similarité dans la base vectorielle
3. **Ranking** : Classification des résultats par pertinence
4. **Context Integration** : Intégration du contexte dans le prompt
5. **Generation** : Génération de la réponse augmentée

**Types de RAG** :
- **Naive RAG** : Récupération simple et génération
- **Advanced RAG** : Pre-retrieval et post-retrieval optimization
- **Modular RAG** : Architecture modulaire avec composants spécialisés

**Avantages** :
- Accès à des connaissances à jour
- Réduction des hallucinations
- Personnalisation du contenu
- Scalabilité des connaissances

**Défis** :
- Qualité de la récupération
- Cohérence du contexte
- Latence additionnelle
- Maintenance de la base de connaissances
