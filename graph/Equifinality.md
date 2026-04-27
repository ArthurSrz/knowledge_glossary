---
instance of: "[[graph/Principle]]"
---
The principle that in open systems a given end can be reached by many potential means. This concept is at the core of every [[graph/Tool arena]] aiming at comparing [[Tools]] two-by-two. It is because two tools are *equifinal* that we can compare them : they were designed to reach the same goal. 

Let's take the example of [[RAG (Retrieval-Augmented Generation)]] systems. Their purpose is to orient a [[Large Language Model]] into accomplishing some task into a certain [[Context]]. This task and context is stored inside an external [[graph/Memory]] sources. This goal (*to orient a LLM into accomplishing some task into a certain context*) can be reached by many potential designs of the RAG system. 

With this in mind, when you set two tools with the same goal and the same context, you get a good comparison base, as they are in an *equifinality* configuration. And so subjective evaluation **on top of the two tools output makes sense**. You compare two *equifinal* designs. 

CompaRAG implements this conceptual framework. 
