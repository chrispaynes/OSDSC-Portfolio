Big O notation is a ==mathematical notation used in computer science to describe the upper bound or worst-case complexity of an algorithm in terms of time or space. It provides a way to express the efficiency of an algorithm by characterizing its growth rate relative to the input size. Big O notation is particularly useful for analyzing algorithms as it abstracts away constant factors and focuses on the dominant term that most significantly influences the algorithm's performance as the input size increases.==

The formal definition of Big O notation is as follows:

Let $f(n)$ and $g(n)$ be two functions defined on the positive integers. We say $f(n)$ is $O(g(n))$ (read as "big O of g of n") if there exist constants $C > 0$ and $n_0$ such that $0 \leq f(n) \leq C \cdot g(n)$ for all $n \geq n_0$.

In simpler terms, if $f(n)$ is $O(g(n))$, it means that for sufficiently large values of $n$, the growth rate of $f(n)$ is upper-bounded by a constant multiple of the growth rate of $g(n)$.

Common Big O notations include:

1. **O(1):** Constant time complexity. The algorithm's performance is constant, regardless of the input size.
  
2. **O(log n):** Logarithmic time complexity. Common in algorithms that divide the input into smaller parts.

3. **O(n):** Linear time complexity. The running time grows linearly with the size of the input.

4. **O(n log n):** Linearithmic time complexity. Common in efficient sorting algorithms like Merge Sort and Heap Sort.

5. **O(n^2):** Quadratic time complexity. Common in algorithms with nested loops.

6. **O(2^n):** Exponential time complexity. Common in algorithms with recursive branching.

7. **O(n!):** Factorial time complexity. Common in brute-force algorithms that try all possible solutions.

The goal is generally to design algorithms with lower Big O complexities to ensure efficient performance as the input size increases. However, it's important to note that Big O notation provides an upper bound, and the actual performance may vary based on factors like constant factors, lower-order terms, and hardware considerations.