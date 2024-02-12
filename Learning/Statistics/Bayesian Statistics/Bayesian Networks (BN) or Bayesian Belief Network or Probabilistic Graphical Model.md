A Bayesian Network (BN), also known as a Bayesian Belief Network or a Probabilistic Graphical Model, is a graphical representation of probabilistic relationships among a set of variables. Bayesian Networks are used to model and represent the conditional dependencies and uncertainties between variables in a system. They provide a compact and intuitive way to express complex probabilistic relationships.

Key features of Bayesian Networks:

1. **Graphical Structure**: A Bayesian Network is represented as a directed acyclic graph (DAG), where nodes represent variables, and directed edges represent probabilistic dependencies between variables. The absence of a direct edge between two nodes indicates conditional independence.

2. **Nodes (Variables)**: Each node in the Bayesian Network corresponds to a random variable. The state of a node represents the possible values that the variable can take.

3. **Conditional Probability Tables (CPTs)**: Associated with each node is a Conditional Probability Table, which specifies the probability distribution of the node given its parents in the graph. The CPT quantifies the conditional dependence between a node and its parent nodes.

4. **Directed Edges and Dependencies**: The direction of edges in the graph indicates the direction of dependence. For example, if there is an edge from variable A to variable B, it implies that B is dependent on A. The absence of an edge indicates conditional independence.

5. **D-Separation**: Bayesian Networks use the concept of D-Separation to determine conditional independence relationships between variables based on the graph structure.

6. **Inference and Prediction**: Bayesian Networks allow for efficient probabilistic inference and prediction. Given evidence (observed data or known variable values), Bayesian Networks can be used to update probability distributions for other variables in the system.

7. **Learning Structure and Parameters**: Bayesian Networks can be constructed manually based on domain knowledge or learned automatically from data. Learning involves estimating the structure (graph) and parameters (CPTs) of the network.

8. **Applications**: Bayesian Networks find applications in various fields, including medicine (diagnosis and prognosis), finance (risk assessment), artificial intelligence, and decision support systems.

Example of a simple Bayesian Network:

![Bayesian Network Example](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/SimpleBayesNetNodes.svg/500px-SimpleBayesNetNodes.svg.png)

In this example, "Rain" and "Sprinkler" are weather-related variables, and "Grass Wet" represents whether the grass is wet. The graph illustrates the conditional dependencies between these variables.

Bayesian Networks provide a powerful framework for representing and reasoning about uncertainty in complex systems, making them valuable for decision-making, risk analysis, and prediction tasks.