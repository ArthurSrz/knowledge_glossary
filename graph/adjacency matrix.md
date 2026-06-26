
Given a graph G = (X, E) with n vertices, its **adjacency matrix** M is an **n × n square matrix** where each entry M[i][j] is defined as:

```
M[i][j] = 1   if there is an edge between vertex i and vertex j
M[i][j] = 0   otherwise
```
### Key properties

For an **undirected** graph, the matrix is always **symmetric** — meaning M[i][j] = M[j][i], since an edge between i and j goes both ways.

The **diagonal** is always **0** — since a vertex has no edge with itself (the anti-reflexive property your book mentioned).

---

### Concrete example

For the handshake problem with 3 people (A, B, C) where A-B and B-C shook hands:

```
   A  B  C
A[ 0  1  0 ]
B[ 1  0  1 ]
C[ 0  1  0 ]
```

Notice the symmetry and the zero diagonal — exactly reflecting the two properties from your book's definition.