![[Pasted image 20230916172408.png|500]]
The Poisson distribution is a probability distribution used in statistics and probability theory to model the number of events occurring within a fixed interval of time or space, given a known average rate of occurrence. It is named after the French mathematician Siméon Denis Poisson, who made significant contributions to probability theory.

The Poisson distribution is characterized by a single parameter, denoted as λ (lambda), which represents the average rate or average number of events occurring within the specified interval. The probability mass function (PMF) of the Poisson distribution is defined as follows:

\$$[P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}\$$]

Where:
- $(P(X = k)$) is the probability of observing exactly \(k\) events.
- $(e$) is the base of the natural logarithm (approximately 2.71828).
- $(\lambda$) is the average rate of occurrence of events within the interval.
- $(k$) is a non-negative integer $(0, 1, 2, 3, ...)$ representing the number of events you want to calculate the probability for.
- $(k!$) is the factorial of $(k$), which is the product of all positive integers from 1 to $(k$).

Key characteristics of the Poisson distribution:

1. **Memorylessness:** The Poisson distribution is memoryless, meaning that the probability of future events is independent of past events. In other words, the distribution describes events that occur randomly and independently over time or space.

2. **Discrete:** The Poisson distribution is a discrete probability distribution because it models countable events (e.g., the number of phone calls received in an hour).

3. **Mean and Variance:** The mean (expected value) and variance of the Poisson distribution are both equal to λ. This means that the average number of events and the spread of the distribution are determined by the same parameter.

Applications of the Poisson distribution:

- Modeling rare events: The Poisson distribution is commonly used to model rare and infrequent events, such as accidents, customer arrivals at a service center, or defects in a manufacturing process.

- Queueing theory: It is used in queueing models to analyze the arrival and service rates of customers in systems like call centers, traffic networks, and service centers.

- Biology: The Poisson distribution is applied to describe the distribution of rare mutations in a DNA sequence or the occurrence of rare diseases in a population.

- Finance: It can be used to model the number of financial market orders within a given time frame.

Overall, the Poisson distribution is a useful tool for modeling events that occur randomly and infrequently, making it applicable in various fields to analyze and predict occurrences of rare events within fixed intervals.