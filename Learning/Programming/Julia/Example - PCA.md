Yes, you can perform Principal Component Analysis (PCA) in Julia using the `MultivariateStats` package. Here's a simple example:

1. **Install Package:**
   If you haven't installed the `MultivariateStats` package, you can do so by running the following command in the Julia REPL:

   ```julia
   using Pkg
   Pkg.add("MultivariateStats")
   ```

2. **Load Libraries:**
   Load the necessary libraries:

   ```julia
   using MultivariateStats
   ```

3. **Create Data:**
   Generate or load your dataset. For this example, let's create a simple matrix `X`:

   ```julia
   X = randn(100, 5)
   ```

   This creates a matrix with 100 samples and 5 features.

4. **Perform PCA:**
   Apply PCA to the data:

   ```julia
   pca_result = fit(PCA, X; maxoutdim=2)
   ```

   In this example, `maxoutdim=2` specifies that we want to reduce the dimensionality to 2 principal components. You can adjust this parameter based on your specific needs.

5. **Transform Data:**
   Transform the original data using the computed PCA model:

   ```julia
   transformed_data = transform(pca_result, X)
   ```

   `transformed_data` now contains the data projected onto the principal components.

The `MultivariateStats` package provides additional functionalities for PCA, such as obtaining the principal components, explained variance ratio, and more. Feel free to explore the documentation for more details: [MultivariateStats.jl](https://multivariatestatsjl.readthedocs.io/en/stable/). Adjust the code according to your specific dataset and requirements.