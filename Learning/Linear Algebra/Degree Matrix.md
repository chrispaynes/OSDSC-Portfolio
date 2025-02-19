==In linear algebra and graph theory, a degree matrix is a diagonal matrix that represents the degree of each vertex in a graph. Given an undirected graph $G$ with $n$ vertices, the degree matrix $D$ is an $n \times n$ diagonal matrix defined as follows:==

$D_{ii} = \text{degree of vertex } i$
$D_{ij} = 0, \text{ for } i \neq j$

==Each diagonal entry $D_{ii}$ corresponds to the degree (number of edges incident to) the vertex $i$, and all off-diagonal entries are zero. The degree matrix is often denoted as $D = \text{diag}(d_1, d_2, \ldots, d_n)$, where $d_i$ is the degree of vertex $i$.==

==The degree matrix is commonly used in the construction of the Laplacian matrix, where it plays a crucial role. The Laplacian matrix is defined as the difference between the degree matrix and the adjacency matrix of a graph. Degree matrices are essential in various applications, including spectral graph theory, network analysis, and algorithms related to graph structures. They provide a concise representation of vertex degrees, facilitating computations related to graph properties and dynamics.==