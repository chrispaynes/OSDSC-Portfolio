SQL aggregation functions, also known as aggregate functions, are used to perform calculations on sets of values and return a single result. These functions are often used with the `SELECT` statement in SQL to summarize and analyze data in a database. Here are some common SQL aggregation functions:

1. **COUNT()**: Counts the number of rows in a specified column. It can be used with `*` to count all rows.

   Example:
   ```sql
   SELECT COUNT(*) FROM orders;
   ```

2. **SUM()**: Calculates the sum of values in a specified column.

   Example:
   ```sql
   SELECT SUM(total_price) FROM sales;
   ```

3. **AVG()**: Computes the average of values in a specified column.

   Example:
   ```sql
   SELECT AVG(age) FROM employees;
   ```

4. **MAX()**: Returns the maximum (largest) value in a specified column.

   Example:
   ```sql
   SELECT MAX(score) FROM student_scores;
   ```

5. **MIN()**: Retrieves the minimum (smallest) value in a specified column.

   Example:
   ```sql
   SELECT MIN(price) FROM products;
   ```

6. **GROUP_CONCAT()** (or equivalent functions like STRING_AGG in SQL Server): Concatenates values from multiple rows into a single string, often used in combination with the `GROUP BY` clause.

   Example:
   ```sql
   SELECT department, GROUP_CONCAT(employee_name) FROM employees GROUP BY department;
   ```

7. **GROUPING SETS()**: Allows you to perform multiple GROUP BY operations in a single query, aggregating data in various ways.

   Example:
   ```sql
   SELECT department, AVG(salary) FROM employees
   GROUP BY GROUPING SETS (department, ());
   ```

8. **HAVING**: Used in combination with the `GROUP BY` clause to filter groups of rows based on a specified condition.

   Example:
   ```sql
   SELECT department, AVG(salary) FROM employees
   GROUP BY department
   HAVING AVG(salary) > 50000;
   ```

These aggregation functions are essential for summarizing and analyzing data within SQL databases. They allow you to perform calculations on columns and generate meaningful insights from your data. Depending on the database system you are using, there might be additional aggregate functions specific to that system.