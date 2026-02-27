---
partOf: "[[Graphs]]"
---
A sequence of edges connecting a sequence of **distinct** vertices in a graph, with no repeating vertices

More formally, a path of length k in a graph G = (X, E) is a sequence of vertices:

```
v0 — v1 — v2 — ... — vk
```

where every vi is distinct, and every consecutive pair (vi, vi+1) is an edge in E.

### Adjacency matrix of a path graph Pn

For a path on n vertices v1 — v2 — ... — vn, the adjacency matrix only has 1s on the **super- and sub-diagonals**:

```
   v1 v2 v3 v4 v5
v1[ 0  1  0  0  0 ]
v2[ 1  0  1  0  0 ]
v3[ 0  1  0  1  0 ]
v4[ 0  0  1  0  1 ]
v5[ 0  0  0  1  0 ]
```

The pattern is clean: M[i][j] = 1 only if |i − j| = 1, i.e. the vertices are immediate neighbours in the path.

---

## Key distinction

Note that Wikidata distinguishes between a **path** (a concept — a sequence of vertices within any graph) and a **path graph** (a graph whose entire structure _is_ a path). Your book likely uses "chemin" for the former and may use "graphe chemin" or Pn for the latter.