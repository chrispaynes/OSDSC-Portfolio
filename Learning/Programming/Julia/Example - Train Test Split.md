In Julia, you can perform train-test splitting using the `DataFrames` and `MLJ` packages. Here's a step-by-step guide:

1. **Install Packages:**
   If you haven't installed the `DataFrames` and `MLJ` packages, you can do so by running the following commands in the Julia REPL:

   ```julia
   using Pkg
   Pkg.add("DataFrames")
   Pkg.add("MLJ")
   ```

2. **Load Packages:**
   Load the necessary packages:

   ```julia
   using DataFrames
   using MLJ
   ```

3. **Create Data:**
   Generate or load your dataset. For this example, let's create a simple DataFrame with two columns, `x` and `y`:

   ```julia
   df = DataFrame(x = 1:100, y = 2 .+ 3 .* randn(100))
   ```

4. **Split Data:**
   Use the `train_test_split` function from the `MLJ` package to split the data into training and testing sets:

   ```julia
   # Define features and target
   X = select(df, Not(:y))
   y = df.y

   # Split the data (e.g., 80% train, 20% test)
   split = partition(eachindex(y), 0.8, shuffle=true)

   # Create training and testing sets
   train_X, train_y = X[split[1]], y[split[1]]
   test_X, test_y = X[split[2]], y[split[2]]
   ```

   This example uses an 80-20 split, but you can adjust the proportion as needed.

Now, `train_X`, `train_y`, `test_X`, and `test_y` contain the feature and target variables for the training and testing sets, respectively.

Remember that the `MLJ` package provides a range of machine learning functionality, so you might find it useful for other aspects of your modeling process. Adjust the code accordingly based on your specific dataset and requirements.