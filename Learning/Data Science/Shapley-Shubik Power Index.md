Shapley values are a concept from cooperative game theory and are used to fairly distribute the value or contribution of each player within a cooperative game or system. Shapley values were introduced by the economist Lloyd Shapley in the early 1950s and have since found applications in various fields, including machine learning, economics, and multi-agent systems.

In the context of cooperative games, here's how Shapley values work:

1. **Cooperative Game:** A cooperative game involves a group of players who work together to achieve a common goal or outcome. Each player can contribute to the overall value or payoff of the game in some way. The goal is to fairly distribute the total value among the players based on their individual contributions.

2. **Shapley Value Calculation:** Shapley values provide a systematic and fair way to allocate the total value among the players. The calculation of Shapley values involves considering all possible permutations of the players (i.e., all possible orders in which they can join the game) and determining how much each player contributes on average as they are added to the coalition.

3. **Marginal Contribution:** At each step of the permutation process, a player's marginal contribution is computed by considering the difference in the total value when the player is added compared to when the player is not added. In other words, it quantifies the additional value that the player brings to the coalition.

4. **Average Contribution:** The Shapley value for each player is the average of their marginal contributions over all possible permutations. This average accounts for the different orders in which players can join and ensures that each player is fairly compensated for their contribution.

Key properties and characteristics of Shapley values:

- **Efficiency:** Shapley values satisfy the property of efficiency, meaning that the sum of the Shapley values for all players equals the total value of the game.

- **Symmetry:** Shapley values are symmetric, meaning that players with the same contributions receive the same Shapley value.

- **Linearity:** Shapley values are linear, which means that if a game can be broken down into subgames, the Shapley values of the subgames can be combined to obtain the Shapley values of the entire game.

Applications of Shapley values:

1. **Cooperative Game Theory:** Shapley values are widely used in cooperative game theory to fairly allocate costs, resources, or benefits among participants in a cooperative setting.

2. **Machine Learning:** In machine learning interpretability, Shapley values are used to explain the contribution of individual features to model predictions, helping to understand the importance of each feature in a prediction.

3. **Coalition Formation:** Shapley values are applied in coalition formation problems in multi-agent systems, such as in the allocation of tasks or resources among autonomous agents.

4. **Economics:** Shapley values have applications in cost allocation, pricing mechanisms, and resource allocation in economic contexts.

Overall, Shapley values provide a principled and fair way to distribute value or contributions among participants in cooperative settings, ensuring that each player receives a share that accurately reflects their individual impact on the outcome.