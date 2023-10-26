# Window Function
SQL Window Functions, also known as windowed or analytic functions, are a powerful feature in SQL that ==allow you to perform calculations across a set of rows related to the current row within the result set. These functions operate within a "window" of rows defined by an OVER() clause, and they can be used to perform complex calculations and aggregations without grouping or subqueries.==

Key characteristics of SQL Window Functions:

1. **Window Specification**: A window function is always associated with a window specification that defines the set of rows over which the function operates. This specification is provided using the `OVER()` clause.

2. ==**Partitioning**: You can partition the result set into subsets or "partitions" of rows based on one or more column values. The window function operates within these partitions independently.==

3. **Ordering**: You can define an ordering of rows within each partition. The window function uses this ordering to determine the window frame of rows over which it operates. Commonly used ordering functions include `ORDER BY`.

4. ==**Window Frame**: The window frame represents the set of rows within each partition that the window function processes. It can be defined using clauses like `ROWS BETWEEN`, `RANGE BETWEEN`, or `UNBOUNDED PRECEDING` to specify the range of rows in the frame.==

5. ==**Aggregate and Analytic Functions**: Window functions include both aggregate functions (e.g., SUM, AVG, COUNT) and analytic functions (e.g., RANK, DENSE_RANK, LAG, LEAD). Analytic functions operate on each row within the window frame and return a value for that row based on the values in the frame.==

Common use cases for SQL Window Functions include:

- ==**Ranking and Percentiles**: Determining the ranking of rows within a partition or calculating percentiles.==

- ==**Running Totals and Moving Averages**: Calculating cumulative sums, averages, or other aggregations within partitions or over a range of rows.==

- ==**Comparing Rows**: Comparing values of the current row with those in other rows within the same partition.==

- ==**Top-N and Bottom-N Queries**: Selecting the top or bottom rows within each partition based on a specific column or metric.==

- **Time Series Analysis**: Analyzing time-series data to identify trends and patterns.

Here's an example of a simple SQL query using a window function to calculate the row number within each partition:

```sql
SELECT
  department,
  employee_name,
  salary,
  ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS rank_within_department
FROM
  employees;
```

In this query, `ROW_NUMBER()` is a window function that assigns a unique row number to each employee within their respective department, based on their salary in descending order.

SQL Window Functions are a valuable tool for performing complex analytical operations and reporting within SQL queries, and they can significantly simplify queries that would otherwise require subqueries or complex joins. They are supported by most modern relational database systems, including PostgreSQL, MySQL, SQL Server, and Oracle Database.

SQL Window Functions provide a powerful way to perform various calculations and analyses within a result set. Here are some common SQL Window Functions that you should know:

1. **ROW_NUMBER()**: Assigns a unique integer to each row within a partition. It is often used for ranking or identifying rows.

   ```sql
   ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_within_department
   ```

2. ==**RANK() and DENSE_RANK()**: Assigns a ranking to each row within a partition, handling ties differently. `RANK()` leaves gaps in case of ties, while `DENSE_RANK()` assigns the same rank to tied rows.==

   ```sql
   RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_within_department
   DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank_within_department
   ```

3. ==**NTILE()**: Divides the result set into a specified number of approximately equal parts (tiles) and assigns each row to a tile.==

   ```sql
   NTILE(4) OVER (ORDER BY score) AS quartile
   ```

4. ==**LEAD() and LAG()**: Accesses data from subsequent or preceding rows within the same partition based on an ordering column.==

   ```sql
   LAG(sales, 1) OVER (PARTITION BY department ORDER BY date) AS previous_month_sales
   LEAD(sales, 1) OVER (PARTITION BY department ORDER BY date) AS next_month_sales
   ```

5. ==**FIRST_VALUE() and LAST_VALUE()**: Retrieve the first or last value in a window frame, respectively.==

   ```sql
   FIRST_VALUE(product_name) OVER (PARTITION BY category ORDER BY sales DESC) AS best_selling_product
   LAST_VALUE(product_name) OVER (PARTITION BY category ORDER BY sales DESC) AS worst_selling_product
   ```

6. ==**SUM(), AVG(), MIN(), and MAX()**: These aggregate functions can be used as window functions by applying them over a specified window frame. They calculate running totals, averages, or other aggregates within the window frame.==

   ```sql
   SUM(sales) OVER (PARTITION BY department ORDER BY date) AS running_total_sales
   AVG(salary) OVER (PARTITION BY department) AS average_salary
   ```

7. ==**COUNT()**: Calculates the count of rows within a window frame. Useful for counting rows within partitions or over a range.==

   ```sql
   COUNT(*) OVER (PARTITION BY category) AS category_row_count
   ```

8. ==**PERCENT_RANK() and CUME_DIST()**: Calculate the relative rank of a row within a window frame. `PERCENT_RANK()` returns a value between 0 and 1, while `CUME_DIST()` returns a value between 0 and 1, inclusive.==

   ```sql
   PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) AS percent_rank_salary
   CUME_DIST() OVER (PARTITION BY department ORDER BY salary) AS cumulative_distribution_salary
   ```

9. ==**NTH_VALUE()**: Retrieves the value of a specified expression from the nth row in the window frame.==

   ```sql
   NTH_VALUE(product_name, 3) OVER (PARTITION BY category ORDER BY sales DESC) AS third_best_selling_product
   ```

