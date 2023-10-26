SQL filter clauses are used to restrict the result set of a SQL query by specifying conditions that must be met for a row to be included in the output. These clauses are essential for retrieving specific data from a database table. The most commonly used filter clauses in SQL are:

1. **WHERE Clause**:
   - The `WHERE` clause is used to filter rows based on a specified condition. Rows that meet the condition are included in the result set.
   - Example:
     ```sql
     SELECT * FROM products WHERE category = 'Electronics';
     ```

2. **AND Operator**:
   - The `AND` operator is used in the `WHERE` clause to combine multiple conditions. It requires all conditions to be true for a row to be included in the result set.
   - Example:
     ```sql
     SELECT * FROM customers WHERE age >= 25 AND city = 'New York';
     ```

3. **OR Operator**:
   - The `OR` operator is used in the `WHERE` clause to combine multiple conditions. It requires at least one of the conditions to be true for a row to be included in the result set.
   - Example:
     ```sql
     SELECT * FROM orders WHERE status = 'Shipped' OR status = 'Delivered';
     ```

4. **NOT Operator**:
   - The `NOT` operator is used to negate a condition in the `WHERE` clause. It returns rows that do not meet the specified condition.
   - Example:
     ```sql
     SELECT * FROM employees WHERE NOT department = 'HR';
     ```

5. **IN Operator**:
   - The `IN` operator is used to filter rows where a column's value matches any value in a specified list.
   - Example:
     ```sql
     SELECT * FROM products WHERE category IN ('Electronics', 'Appliances', 'Home & Garden');
     ```

6. **BETWEEN Operator**:
   - The `BETWEEN` operator is used to filter rows where a column's value falls within a specified range.
   - Example:
     ```sql
     SELECT * FROM sales WHERE order_date BETWEEN '2023-01-01' AND '2023-03-31';
     ```

7. **LIKE Operator**:
   - The `LIKE` operator is used for pattern matching with wildcard characters.
   - `%` represents any number of characters, and `_` represents a single character.
   - Example:
     ```sql
     SELECT * FROM products WHERE product_name LIKE 'Laptop%';
     ```

8. **IS NULL Operator**:
   - The `IS NULL` operator is used to filter rows where a column's value is NULL.
   - Example:
     ```sql
     SELECT * FROM customers WHERE email IS NULL;
     ```

9. **IS NOT NULL Operator**:
   - The `IS NOT NULL` operator is used to filter rows where a column's value is not NULL.
   - Example:
     ```sql
     SELECT * FROM employees WHERE hire_date IS NOT NULL;
     ```

10. **Comparison Operators**:
   - These operators are used to compare values and are often used in `WHERE` conditions.

   - `=`: Equal to
   - `!=` or `<>`: Not equal to
   - `<`: Less than
   - `<=`: Less than or equal to
   - `>`: Greater than
   - `>=`: Greater than or equal to

   Example:
   ```sql
   SELECT * FROM products WHERE price > 100;
   ```

These filter clauses are used in combination with the `SELECT` statement to retrieve specific data from database tables. The choice of which filter clauses to use depends on the desired criteria and conditions for extracting data.

# WHERE EXISTS
The `WHERE EXISTS` operator in SQL is used to filter rows in a query based on the existence of rows in a correlated subquery. It is primarily used to check for the existence of related data in another table and conditionally include rows in the result set based on the result of the subquery.

The syntax for the `WHERE EXISTS` operator is as follows:

```sql
SELECT column1, column2, ...
FROM table1
WHERE EXISTS (subquery);
```

- The main query, which may involve multiple tables, retrieves rows from `table1` based on the conditions specified in the `WHERE` clause.

- The subquery is enclosed within parentheses and provides a condition that determines whether the `EXISTS` operator evaluates to true or false. The subquery is typically correlated with the main query, meaning it references columns from the outer query. If the subquery returns at least one row, the `EXISTS` condition is true, and the corresponding row from `table1` is included in the result set.

Here's an example to illustrate how the `WHERE EXISTS` operator works:

Suppose you have two tables, `orders` and `customers`, and you want to retrieve a list of customers who have placed at least one order. You can use the `WHERE EXISTS` operator to achieve this:

```sql
SELECT customer_id, first_name, last_name
FROM customers
WHERE EXISTS (
  SELECT 1
  FROM orders
  WHERE customers.customer_id = orders.customer_id
);
```

In this example, the main query retrieves customer information from the `customers` table, and the subquery checks whether there is at least one order for each customer in the `orders` table. If there's at least one matching row in the subquery for a customer, that customer's information is included in the result set.

The `WHERE EXISTS` operator is particularly useful when you need to filter rows based on the presence of related data and is commonly used in situations where you want to perform a correlated subquery to find records with specific characteristics in one table based on conditions in another table.