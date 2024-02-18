Logarithmic Loss, commonly known as Log-Loss or log loss, is ==a measure used to evaluate the performance of a classification model, especially in the context of probabilistic predictions. It is a popular metric when dealing with models that provide probability estimates for each class rather than discrete predictions.==

For a binary classification problem with two classes (0 and 1), the formula for log loss is:

$\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} \left( y_i \log(p_i) + (1 - y_i) \log(1 - p_i) \right)$

where:
- $N$ is the number of instances or observations in the dataset.
- $y_i$ is the actual binary outcome for the $i$-th instance (0 or 1).
- $p_i$ is the predicted probability that the instance belongs to class 1.

For multiclass classification problems, the formula is a generalization of the binary case:

$\text{Log Loss} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{j=1}^{M} y_{ij} \log(p_{ij})$

where:
- $M$ is the number of classes.
- $y_{ij}$ is a binary indicator of whether the true class of the $i$-th instance is $j$.
- $p_{ij}$ is the predicted probability that the $i$-th instance belongs to class $j$.

==Log Loss penalizes models more severely for confident yet incorrect predictions. It captures the uncertainty associated with probabilistic predictions, rewarding models for being both accurate and confident. ==

==A lower log loss indicates better model performance.==

It's worth noting that log loss is a continuous and differentiable metric, making it suitable for optimization during the training of probabilistic models.