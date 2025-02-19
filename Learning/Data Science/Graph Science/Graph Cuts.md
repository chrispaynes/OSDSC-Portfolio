==In graph theory, a cut in a graph refers to a partition of the vertices into two disjoint sets. The cut size is then defined as the number of edges crossing this partition. ==

==Formally, for an undirected graph $G = (V, E)$, where $V$ is the set of vertices and $E$ is the set of edges, a cut is represented by two disjoint sets of vertices $A$ and $B$, such that $A \cup B = V$ and $A \cap B = \emptyset$. The cut size is the number of edges with one endpoint in $A$ and the other in $B$.==

Mathematically, if $E(A, B)$ denotes the set of edges crossing the cut (having one endpoint in $A$ and the other in $B$), then the cut size $|E(A, B)|$ is the cardinality of $E(A, B)$.

==Graph cuts have various applications, particularly in the context of network flow problems and image segmentation. Minimizing the cut size can be related to finding a partition that separates certain components of interest. In image segmentation, for example, a cut can be used to separate regions with different characteristics or objects in an image. The minimum cut problem, which aims to find the cut with the smallest size, is a well-known problem in graph theory and optimization.==