SQL subqueries and correlated subqueries are two types of subqueries used to retrieve data from a database. While both involve nested queries, they serve different purposes and have distinct characteristics:

**1. Subquery (Non-correlated Subquery):**
   - A subquery, also known as a non-correlated subquery or scalar subquery, is a query nested within another query.
   - ==It is independent of the outer query and is executed only once before the main query runs.==
   - ==The result of the subquery is a single value or a single row.==
   - ==Subqueries can be used in various parts of a query, such as the `SELECT`, `FROM`, or `WHERE` clauses, depending on the specific use case.==
   - ==A non-correlated subquery typically returns a value or a set of values that are then used in the main query to filter or compare data.==

   Example of a non-correlated subquery in the `WHERE` clause:
   ```sql
   SELECT product_name
   FROM products
   WHERE price > (SELECT AVG(price) FROM products);
   ```

**2. Correlated Subquery:**
   - ==A correlated subquery is a type of subquery in which the inner query references columns from the outer query.==
   - ==It is executed for each row in the result set of the outer query. The result of the subquery can be different for each row of the main query, as it depends on the values of the current row in the outer query.==
   - ==Correlated subqueries are often used to perform row-by-row comparisons or calculations and are typically found in the `WHERE` or `SELECT` clauses.==

   Example of a correlated subquery in the `WHERE` clause:
   ```sql
   SELECT employee_name
   FROM employees e
   WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);
   ```

In the correlated subquery example, the subquery calculates the average salary for employees in the same department as the current row of the outer query (e). ==The subquery is correlated because it refers to the department_id of the current row from the outer query.==

In summary, the main difference between subqueries and correlated subqueries is their interaction with the outer query. Subqueries are independent and execute once, providing a single value or result set used in the outer query, while correlated subqueries execute once for each row of the outer query and can reference columns from the outer query. Correlated subqueries are especially useful when you need to perform row-level comparisons or calculations.