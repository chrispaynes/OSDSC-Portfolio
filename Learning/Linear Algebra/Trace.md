==In linear algebra, the trace of a square matrix is the sum of its diagonal elements.== 

Mathematically, if $A$ is an $n \times n$ matrix, the trace ($\text{Tr}$) is given by:

$\text{Tr}(A) = \sum_{i=1}^n A_{ii}$

In other words, it's the sum of the elements on the main diagonal of the matrix. The trace is defined for square matrices only, where the number of rows is equal to the number of columns.

The trace has several properties, including:

1. **Linearity:** For any scalars $a$ and $b$ and square matrices $A$ and $B$, $\text{Tr}(aA + bB) = a\text{Tr}(A) + b\text{Tr}(B)$.

2. **Cyclic Property:** For square matrices $A$ and $B$ such that $AB$ is defined (the number of columns in $A$ is equal to the number of rows in $B$), $\text{Tr}(AB) = \text{Tr}(BA)$.

3. **Invariance Under Similarity:** If $B = P^{-1}AP$ for an invertible matrix $P$, then $\text{Tr}(A) = \text{Tr}(B)$.

The trace is used in various areas of mathematics and physics. For example, it appears in the definition of the matrix exponential, and it plays a role in characterizing certain properties of linear transformations and quadratic forms.

Let **A** be a matrix, with

${\displaystyle \mathbf {A} ={\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}}={\begin{pmatrix}1&0&3\\11&5&2\\6&12&-5\end{pmatrix}}}]$

Then

$$tr ⁡ ( A ) = ∑ i = 1 3 a i i = a 11 + a 22 + a 33 = 1 + 5 + ( − 5 ) = 1$$

$${\displaystyle \operatorname {tr} (\mathbf {A} )=\sum _{i=1}^{3}a_{ii}=a_{11}+a_{22}+a_{33}=1+5+(-5)=1}$$

---

The trace of a square matrix has various applications and is used in different mathematical and scientific contexts. Here are a few scenarios where the trace of a square matrix is commonly employed:

1. **Linear Algebra Operations:**
   - **Similarity Transformations:** The trace is invariant under similarity transformations. If $B = P^{-1}AP$ for an invertible matrix $P$, then $\text{Tr}(A) = \text{Tr}(B)$. This property is useful in certain linear algebraic manipulations.
   - **Cyclic Property:** The cyclic property of the trace ($\text{Tr}(AB) = \text{Tr}(BA)$) is utilized in various algebraic proofs and computations.

2. **Matrix Analysis:**
   - **Matrix Exponential:** The trace is part of the formula for the matrix exponential. If $A$ is a square matrix, then the exponential of $A$ is given by the series $\exp(A) = \sum_{k=0}^\infty \frac{A^k}{k!}$, and the trace plays a role in this expression.

3. **Physics and Engineering:**
   - **Quantum Mechanics:** In quantum mechanics, the trace of a density matrix is related to the expectation value of an observable. It's a key concept in the study of quantum systems.
   - **Control Theory:** The trace is often used in the analysis of linear systems and control theory.

4. **Symmetric Matrices:**
   - **Quadratic Forms:** For a real symmetric matrix, the trace is related to the sum of the eigenvalues, and this sum appears in the expression of quadratic forms. The trace can be used to characterize properties of symmetric matrices.

5. **Algebraic Structures:**
   - **Group Theory:** In group representation theory, the trace is often used to define characters, which are crucial in the study of representations of groups.

Understanding the properties and applications of the trace is essential for a deeper understanding of linear algebra, matrix theory, and various mathematical and scientific disciplines.