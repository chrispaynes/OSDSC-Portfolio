![[node2vec.pdf]]

# Terminology
### network neighborhood
In graph analysis, the term "network neighborhood" refers to the local structure surrounding a specific node within a graph. It encompasses the set of nodes directly connected to the focal node and the edges that link them. The network neighborhood provides insights into the immediate relationships and connections of a particular node, offering a snapshot of its local influence and interactions within the larger network.

Understanding the network neighborhood is crucial for exploring the immediate context of a node, identifying its neighbors, and assessing the local patterns or communities in which it participates. Analyzing the network neighborhood aids in uncovering the connectivity patterns, influential nodes, and potential clusters within a specific region of the graph. This localized perspective is valuable for tasks such as identifying key players, assessing the flow of information, or detecting anomalies within the immediate vicinity of a given node in the graph.

### weighted vs unweighted network
The key distinction between a weighted and an unweighted graph lies in the assignment of numerical values, called weights, to the edges of the graph.

1. **Unweighted Graph:**
   - In an unweighted graph, all edges are considered equal, and no numerical values (weights) are associated with them. The edges simply represent the presence or absence of connections between nodes, with no additional information regarding the strength or cost of these connections. Unweighted graphs are often used when the relationships between nodes are binary, indicating only whether an edge exists or not.

2. **Weighted Graph:**
   - In a weighted graph, each edge is assigned a numerical weight that represents a quantitative measure associated with that edge. These weights can represent various attributes such as distance, cost, time, or any other relevant metric depending on the application. Weighted graphs are particularly useful when there is a need to model and analyze relationships with different levels of importance or significance.

**Example:**
Consider a graph representing cities as nodes and direct flights between cities as edges. In an unweighted graph, each edge would simply represent the existence of a flight, while in a weighted graph, the edges could be assigned weights corresponding to the distances between the cities, flight durations, or other factors.

The choice between using a weighted or unweighted graph depends on the specific characteristics of the system being modeled and the type of analysis or computations that need to be performed. Weighted graphs offer a more nuanced representation of relationships, allowing for richer analyses that take into account the strength or cost associated with connections.

### 2-hop redundancy in sampling

### 2nd order Markovian Chain
A 2nd order Markov chain, also known as a second-order Markov chain or a bivariate Markov chain, extends the concept of a Markov chain to incorporate information about the past two states rather than just the most recent state. In a standard (first-order) Markov chain, the probability of transitioning to a future state depends only on the current state. However, in a 2nd order Markov chain, the transition probabilities are determined by the two most recent states, providing a more intricate model for capturing dependencies and patterns in sequential data.

Mathematically, for a 2nd order Markov chain, the conditional probability of transitioning to a future state given the current and previous states is expressed as P(X_{t+1} | X_t, X_{t-1}), where X_t, X_{t-1}, and X_{t+1} are random variables representing the current, previous, and next states, respectively. The transition probabilities are often organized into a three-dimensional array, known as the transition tensor or second-order transition matrix, which specifies the probabilities for all possible state transitions.

2nd order Markov chains find applications in modeling sequential data with more complex dependencies, such as natural language processing, where the occurrence of a word may depend not only on the current word but also on the two preceding words. While they introduce additional complexity, these higher-order Markov chains offer a more nuanced representation of systems with intricate temporal dependencies.

### 2nd order random walk approach

### average degree of the graph

Can we analyze the traits of current/recent CXOs at peer/competitor companies to development a Collaborative Filtering Model that describes the high-level traits a client should consider when searching for a similar CXO role?

[[Data Science/Collaborative Filtering Model|Collaborative Filtering Model]]

[[Homophily]]

### IsoMap dimensionality reduction technique
Isomap, short for Isometric Mapping, is a dimensionality reduction technique used in machine learning and data analysis. It is particularly effective for capturing the intrinsic geometric structure of high-dimensional data by preserving the pairwise distances between data points. Isomap aims to overcome the limitations of traditional methods like Principal Component Analysis (PCA) when dealing with nonlinear structures.

The core idea of Isomap is to construct a low-dimensional representation of the data while preserving the geodesic distances on a manifold. It starts by building a neighborhood graph, where each data point is connected to its nearest neighbors. Then, it estimates the geodesic distances between points by computing the shortest paths along the edges of the graph. The geodesic distances are then used to create a lower-dimensional embedding of the data points. This embedding preserves the underlying geometry of the data, capturing nonlinear relationships and maintaining the local and global structure of the manifold.

One notable feature of Isomap is its ability to unfold and represent the data in a way that respects the intrinsic curvature of the underlying manifold. This makes Isomap particularly useful for tasks such as manifold learning, where understanding the intrinsic structure of the data is crucial. However, it is important to note that Isomap's performance may be sensitive to the choice of parameters, and it requires careful consideration of the neighborhood size to balance local and global structure preservation. Overall, Isomap is a valuable tool for visualizing high-dimensional data in a reduced-dimensional space while maintaining the essential relationships between data points.

### Laplacian and the adjacency matrices

### Laplacian matrix
The Laplacian matrix, often denoted as \(L\), is a square matrix derived from a graph. In the context of graph theory, a graph consists of nodes (vertices) and edges connecting pairs of nodes. The Laplacian matrix is a representation of the graph's topology and connectivity. It provides valuable insights into the structural properties of the graph and is widely used in various applications, including spectral graph theory, image segmentation, and network analysis.

For an undirected graph with \(n\) nodes, the Laplacian matrix \(L\) is defined as \(L = D - A\), where \(D\) is the degree matrix and \(A\) is the adjacency matrix. The degree matrix \(D\) is a diagonal matrix that contains the degrees (number of edges incident on each node) along its diagonal. The adjacency matrix \(A\) indicates the connections between nodes; its entries are 1 if two nodes are connected and 0 otherwise. The Laplacian matrix captures local and global properties of the graph, and its eigenvalues and eigenvectors are of particular interest in spectral graph theory.

The Laplacian matrix is employed in various algorithms and analyses. For example, spectral clustering uses the eigenvectors of the Laplacian matrix to partition a graph into clusters. The Laplacian matrix is also essential in understanding the connectivity and robustness of networks. Different variants of the Laplacian matrix exist, including the normalized Laplacian, which considers node degrees to normalize the entries, and the combinatorial Laplacian, which uses only the degrees without normalization.

### [[Macro-F1 scores and Micro-F1]]

### matrix factorization
Matrix factorization is a technique used in linear algebra and machine learning to decompose a matrix into the product of two or more lower-dimensional matrices. The goal of matrix factorization is to represent the original matrix in a way that captures its essential structure, allowing for more efficient storage, analysis, and reconstruction of the data. One common application of matrix factorization is collaborative filtering in recommendation systems, where it is used to discover latent factors underlying user-item interactions.

In collaborative filtering, the matrix typically represents user-item interactions, where rows correspond to users, columns correspond to items, and the entries represent user ratings or preferences. Matrix factorization aims to find two matrices, often referred to as the user matrix and the item matrix, whose product closely approximates the original matrix. The resulting factorized matrices capture latent features or factors that influence user preferences and item characteristics.

The factorization process involves iterative optimization techniques, such as gradient descent, to minimize the difference between the actual matrix entries and the entries predicted by the product of the factorized matrices. The latent factors discovered through matrix factorization can be interpreted as features that contribute to the observed interactions between users and items. Matrix factorization has wide applications beyond recommendation systems, including image compression, topic modeling, and data denoising, making it a versatile tool in various fields.

### maximum likelihood optimization problem
The maximum likelihood optimization problem is a fundamental concept in statistics and machine learning, particularly in the context of estimating parameters for a probabilistic model. The goal is to find the set of parameter values that maximize the likelihood function, which measures how well the model explains the observed data. The likelihood function quantifies the probability of observing the given data under different parameter settings, and maximizing it corresponds to selecting the parameter values that make the observed data most probable according to the model.

Mathematically, if we have a probabilistic model with parameters θ and observed data X, the likelihood function L(θ | X) is defined as the probability of observing X given the parameter values θ. The maximum likelihood estimation (MLE) problem is to find the values of θ that maximize this likelihood function. In practice, it is often more convenient to work with the log-likelihood function (log-likelihood) since it transforms the product of probabilities into a sum of logarithms, simplifying the optimization process.

Maximum likelihood estimation is widely used in various statistical and machine learning applications, including linear regression, logistic regression, and many other models. The estimated parameter values obtained through MLE provide a point estimate that is considered the most likely set of parameters given the observed data, assuming the model is correct. The approach is robust and asymptotically unbiased, making it a cornerstone in statistical modeling and inference.

### negative sampling
Negative sampling is a technique used in machine learning, particularly in the context of training neural network models for tasks such as word embeddings or recommendation systems. The objective of negative sampling is to improve the efficiency of training by selectively sampling negative examples, which are instances that are not relevant to the task at hand. This approach is often employed in scenarios where the number of negative examples (non-relevant instances) vastly exceeds the positive examples, making it computationally expensive to consider all possible negatives during training.

In the realm of word embeddings, where the goal is to learn vector representations for words, negative sampling is applied to the skip-gram model. In this context, the skip-gram model predicts the context words given a target word. Instead of considering all words in the vocabulary as negative samples, negative sampling randomly selects a small number of negative examples for each positive training example. This significantly reduces the computational cost associated with updating model parameters and accelerates the learning process.

Negative sampling is also prevalent in recommendation systems, particularly in collaborative filtering models. When training a recommendation system, the goal is to predict a user's preferences for items. Negative sampling is used to efficiently select non-interacted items as negative examples for each user, enabling the model to learn meaningful user-item interactions without having to consider all possible items as negatives. The technique strikes a balance between computational efficiency and model accuracy, making it widely employed in large-scale machine learning applications.

### normalizing constant

### objective function

### one-vs-rest logistic regression classifier

### perturbation study
A perturbation study involves systematically introducing small changes or perturbations to a system or model to analyze how these changes affect the system's behavior or the model's performance. The goal is to understand the sensitivity of the system or model to variations in input conditions or parameters. Perturbation studies are conducted across various scientific and engineering disciplines and can be applied to physical systems, mathematical models, algorithms, or simulations.

In the context of mathematical models and simulations, perturbation studies are often used to assess the robustness and stability of the model. Small changes in initial conditions, parameters, or inputs are introduced, and the resulting impact on the model's output is observed. This helps researchers and analysts identify critical factors that influence the system's behavior and gain insights into the model's sensitivity to different input variations.

In scientific experiments, perturbation studies can be employed to investigate the response of a physical system to external disturbances or changes in experimental conditions. The study of perturbations is fundamental in fields such as physics, biology, ecology, and climate science to understand how systems respond to disturbances and to make predictions about their future behavior.

Overall, perturbation studies provide a valuable tool for researchers and scientists to explore the dynamics, stability, and sensitivity of systems, models, or experiments, contributing to a deeper understanding of their behavior under different conditions.

### Skip-gram
Skip-gram is a natural language processing (NLP) model that belongs to the family of word embedding techniques. Developed as part of the Word2Vec framework, skip-gram is designed to learn distributed representations of words in a continuous vector space. The primary objective of skip-gram is to predict the context words given a target word, capturing the relationships and meanings of words based on their co-occurrence patterns in a given corpus.

In the skip-gram model, each word in a vocabulary is represented as a high-dimensional vector, and the training involves adjusting these vectors to maximize the likelihood of predicting the surrounding context words. The model essentially "skips" through the context words in a sequence to predict the probability distribution of words within a certain window around the target word. Skip-gram's effectiveness lies in its ability to generate dense and semantically meaningful representations of words, capturing semantic relationships and syntactic structures.

The skip-gram model is often contrasted with the continuous bag-of-words (CBOW) model, another Word2Vec variant. While CBOW predicts the target word based on its context, skip-gram does the reverse by predicting context words given the target word. Skip-gram is particularly useful in scenarios where capturing fine-grained semantic relationships and the meaning of words in different contexts is essential, making it a popular choice for word embedding applications in NLP.

### softmax probabilities
Softmax probabilities refer to a set of probabilities generated by the softmax function, which is commonly used in machine learning, particularly in the context of classification problems. The softmax function transforms a vector of real numbers into a probability distribution, ensuring that the output values are non-negative and sum to one. This makes it suitable for multiclass classification tasks where the goal is to assign an input to one of several possible classes.

Given a vector of raw scores or logits (unnormalized values) representing the output of a model, the softmax function calculates the probabilities for each class. The function exponentiates each element of the vector to make the values positive and then normalizes them by dividing by the sum of all exponentiated values. The resulting probabilities indicate the likelihood of the input belonging to each class, and the class with the highest probability is often predicted as the final output.

Softmax probabilities play a crucial role in the training and evaluation of neural network models, especially in the output layer of classification models. During training, the softmax probabilities are compared to the true class labels using a loss function, such as cross-entropy, to guide the learning process. In inference or prediction, the softmax probabilities help determine the predicted class for a given input. The use of softmax ensures that the model outputs meaningful and interpretable probability distributions, facilitating the decision-making process in classification tasks.

### softmax unit

### spectral clustering
Spectral clustering is a technique used in graph science and machine learning for partitioning a graph's nodes into distinct clusters based on the graph's spectral properties. Unlike traditional clustering methods that operate in the original data space, spectral clustering operates in the spectral domain by leveraging the eigenvalues and eigenvectors of the graph's Laplacian matrix. The Laplacian matrix captures the relationships and connectivity between nodes in the graph, and spectral clustering exploits its spectral decomposition to identify meaningful clusters.

The process of spectral clustering typically involves three main steps. First, the Laplacian matrix of the graph is computed. Second, the eigenvalues and corresponding eigenvectors of the Laplacian matrix are obtained. Third, a clustering algorithm is applied to the lower-dimensional representation of the graph obtained from the eigenvectors, with each eigenvector corresponding to a specific cluster. The resulting spectral clusters are often more accurate in capturing the underlying structure of the graph, especially in scenarios where the graph has a complex and non-convex shape.

Spectral clustering is advantageous for its ability to identify clusters in graphs with irregular shapes and non-uniform densities. It has applications in various fields, including image segmentation, community detection in social networks, and document clustering. Spectral clustering is effective in scenarios where traditional methods, such as k-means clustering, may struggle due to the intricate structure of the data represented as a graph.

### stochastic gradient ascent

### stochastic gradient descent (SGD)
Stochastic Gradient Descent (SGD) is a widely used optimization algorithm in machine learning, particularly for training models in large-scale datasets. It is an iterative optimization method designed to minimize the cost or loss function associated with a model by adjusting its parameters. SGD belongs to the broader family of gradient descent algorithms, but it introduces a stochastic element by updating the model's parameters based on a randomly selected subset (mini-batch) of the training data rather than the entire dataset.

In each iteration of SGD, a mini-batch of data is sampled randomly from the training set, and the model parameters are updated using the gradient of the loss function with respect to the parameters. This stochastic sampling helps accelerate the convergence of the optimization process, making SGD computationally efficient and well-suited for large datasets. The randomness introduced by the mini-batch selection also provides a form of regularization, helping the model generalize better to unseen data.

Despite its efficiency, SGD might exhibit some variability in its convergence due to the randomness in selecting mini-batches. Variants of SGD, such as Mini-Batch Gradient Descent, Batch Gradient Descent (using the entire dataset), and variants with adaptive learning rates (e.g., Adam, RMSprop), have been developed to address specific challenges and improve the stability and convergence speed of the optimization process. SGD is a foundational optimization technique and forms the basis for training a wide range of machine learning models.

### structural equivalence
Structural equivalence is a concept in graph theory and social network analysis that addresses the similarity in the connectivity patterns between nodes in a graph. Two nodes are considered structurally equivalent if they share similar relationships with other nodes in the network. Unlike regular equivalence, which is based on direct connections between nodes, structural equivalence looks at the broader connectivity context, considering not only direct ties but also the patterns of relationships with other nodes in the network.

In the context of social networks, structural equivalence implies that two individuals have similar roles or positions within the network, even if they are not directly connected. For example, in an organizational hierarchy, two employees might be structurally equivalent if they share similar relationships with other colleagues or have similar positions within the network, even if they are not directly linked.

Structural equivalence is often identified through techniques such as block modeling or matrix factorization, which reveal groups of nodes with similar connectivity patterns. The concept is fundamental for understanding the organization and dynamics of complex networks, shedding light on nodes that play equivalent roles in terms of their influence, position, or relationships within the broader network structure.

### symmetric effect over each other in feature space.

### (un)directed network

### transition probability
In graph science, transition probability is a concept used to quantify the likelihood or probability of moving from one state or node to another within a graph or Markov chain. It is particularly prevalent in the study of stochastic processes and random walks on graphs, where nodes represent states and edges represent possible transitions between states. Transition probability defines the chance of transitioning from one state to another in a single step, capturing the dynamics of the system's movement through the graph.

For a given directed graph, the transition probability from one node to another is often represented as a numerical value associated with the directed edge connecting the two nodes. These probabilities collectively form a transition matrix, where each row corresponds to the current state and each column corresponds to the possible next states. The sum of the probabilities in each row equals one, ensuring that the system will transition to one of the connected states in the next step.

Transition probabilities play a crucial role in various applications, including modeling random processes, analyzing the behavior of systems over time, and predicting future states in scenarios such as recommendation systems, search algorithms, or the study of molecular dynamics. They provide a probabilistic framework for understanding the dynamics and evolution of systems represented as graphs, enabling researchers to make predictions about the future state of a system based on its current state and the underlying transition probabilities.