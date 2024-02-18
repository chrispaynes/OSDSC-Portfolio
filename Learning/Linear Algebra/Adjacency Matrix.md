==An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph. If a graph has $n$ vertices, the adjacency matrix is an $n \times n$ matrix.==

In an undirected graph, the adjacency matrix is symmetric since the edge between vertex $i$ and vertex $j$ is the same as the edge between vertex $j$ and vertex $i$. For a directed graph, the adjacency matrix may not be symmetric, as the presence of an edge from vertex $i$ to vertex $j$ does not necessarily imply the existence of an edge from $j$ to $i$.

The entry $A[i][j]$ in the adjacency matrix represents the connection between vertex $i$ and vertex $j$. The interpretation of this entry depends on whether the graph is weighted or unweighted:

1. **Unweighted Graphs:**
   - $A[i][j] = 1$ if there is an edge between vertex $i$ and vertex $j$.
   - $A[i][j] = 0$ if there is no edge between vertex $i$ and vertex $j$.

2. **Weighted Graphs:**
   - $A[i][j]$ represents the weight of the edge between vertex $i$ and vertex $j$.
   - $A[i][j] = \infty$ or $A[i][j] = -1$ can be used to indicate the absence of an edge between $i$ and $j$ in the case of weighted graphs.

Here is an example of an adjacency matrix for an undirected graph:

```c
    1  2  3  4
  +------------
1 | 0  1  1  0
2 | 1  0  1  1
3 | 1  1  0  1
4 | 0  1  1  0
```

In this example, a 1 in the $A[2][3]$ entry indicates that there is an edge between vertex 2 and vertex 3 in the graph.