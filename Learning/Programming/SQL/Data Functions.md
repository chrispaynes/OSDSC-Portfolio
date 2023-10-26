SQL data functions, sometimes referred to as data manipulation functions or string functions, are used to perform operations on data values stored in the database, especially text and date values. These functions allow you to transform and manipulate data in various ways. Here are some common SQL data functions:

1. **CONCAT() or ||**: Concatenates two or more strings together.

   Example:
   ```sql
   SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
   ```

2. **UPPER()**: Converts a string to uppercase.

   Example:
   ```sql
   SELECT UPPER(product_name) AS product_name FROM products;
   ```

3. **LOWER()**: Converts a string to lowercase.

   Example:
   ```sql
   SELECT LOWER(city) AS city FROM customers;
   ```

4. **SUBSTRING() or SUBSTR()**: Extracts a substring from a given string.

   Example:
   ```sql
   SELECT SUBSTRING(description, 1, 50) AS short_description FROM products;
   ```

5. **LENGTH() or LEN()**: Returns the length (number of characters) of a string.

   Example:
   ```sql
   SELECT LENGTH(product_name) AS name_length FROM products;
   ```

6. **TRIM()**: Removes leading and trailing spaces or specified characters from a string.

   Example:
   ```sql
   SELECT TRIM(' ' FROM product_name) AS trimmed_name FROM products;
   ```

7. **REPLACE()**: Replaces occurrences of a specified substring in a string with another substring.

   Example:
   ```sql
   SELECT REPLACE(notes, 'old_text', 'new_text') AS updated_notes FROM orders;
   ```

8. **COALESCE()**: Returns the first non-null value in a list of expressions.

   Example:
   ```sql
   SELECT COALESCE(preferred_address, alternate_address, billing_address) AS final_address FROM customers;
   ```

9. **CONVERT() or CAST()**: Converts data from one data type to another. This is particularly useful for changing date formats or converting between data types.

   Example:
   ```sql
   SELECT CONVERT(date, '2023-09-30', 102) AS formatted_date;
   ```

10. **DATE FUNCTIONS**:
    - **DATE()**: Extracts the date part from a datetime value.
    - **TIME()**: Extracts the time part from a datetime value.
    - **YEAR()**: Extracts the year from a date or datetime value.
    - **MONTH()**: Extracts the month from a date or datetime value.
    - **DAY()**: Extracts the day of the month from a date or datetime value.
    
    Example:
    ```sql
    SELECT DATE(birthdate) AS birth_date FROM employees;
    ```

11. **CONCAT_WS()**: Concatenates strings with a specified separator.

   Example:
   ```sql
   SELECT CONCAT_WS(', ', first_name, last_name) AS full_name FROM employees;
   ```

12. **LEFT()**: Extracts a specified number of characters from the beginning of a string.

   Example:
   ```sql
   SELECT LEFT(description, 30) AS short_description FROM products;
   ```

These SQL data functions are useful for manipulating and transforming data values in various ways, making it easier to retrieve and present data in a desired format. The availability of these functions may vary depending on the database system you are using, so consult your database's documentation for system-specific variations and additional functions.

# String Functions
SQL character functions, also known as string functions or text functions, are used to manipulate and modify character or text data within SQL queries. These functions help you perform operations on text values stored in a database. Here are some common SQL character functions:

1. **CONCAT() or ||**: Concatenates two or more strings together.

   Example:
   ```sql
   SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
   ```

2. **UPPER()**: Converts a string to uppercase.

   Example:
   ```sql
   SELECT UPPER(product_name) AS product_name FROM products;
   ```

3. **LOWER()**: Converts a string to lowercase.

   Example:
   ```sql
   SELECT LOWER(city) AS city FROM customers;
   ```

4. **SUBSTRING() or SUBSTR()**: Extracts a substring from a given string.

   Example:
   ```sql
   SELECT SUBSTRING(description, 1, 50) AS short_description FROM products;
   ```

5. **LENGTH() or LEN()**: Returns the length (number of characters) of a string.

   Example:
   ```sql
   SELECT LENGTH(product_name) AS name_length FROM products;
   ```

6. **TRIM()**: Removes leading and trailing spaces or specified characters from a string.

   Example:
   ```sql
   SELECT TRIM(' ' FROM product_name) AS trimmed_name FROM products;
   ```

7. **REPLACE()**: Replaces occurrences of a specified substring in a string with another substring.

   Example:
   ```sql
   SELECT REPLACE(notes, 'old_text', 'new_text') AS updated_notes FROM orders;
   ```

8. **COALESCE()**: Returns the first non-null value in a list of expressions. While it is typically used with non-string data, it can be used with strings as well.

   Example:
   ```sql
   SELECT COALESCE(preferred_address, alternate_address, billing_address) AS final_address FROM customers;
   ```

9. **CONCAT_WS()**: Concatenates strings with a specified separator.

   Example:
   ```sql
   SELECT CONCAT_WS(', ', first_name, last_name) AS full_name FROM employees;
   ```

10. **LEFT()**: Extracts a specified number of characters from the beginning of a string.

   Example:
   ```sql
   SELECT LEFT(description, 30) AS short_description FROM products;
   ```

11. **RIGHT()**: Extracts a specified number of characters from the end of a string.

   Example:
   ```sql
   SELECT RIGHT(phone_number, 4) AS last_four_digits FROM customers;
   ```

12. **INITCAP()**: Converts the first character of each word in a string to uppercase.

   Example:
   ```sql
   SELECT INITCAP(product_name) AS formatted_name FROM products;
   ```

13. **REVERSE()**: Reverses the characters in a string.

   Example:
   ```sql
   SELECT REVERSE("hello") AS reversed_text; -- Returns "olleh"
   ```

These SQL character functions are essential for working with text data in your database, allowing you to transform and manipulate strings to meet your specific needs. The availability and behavior of these functions may vary depending on the database system you are using, so be sure to consult your database's documentation for any system-specific variations and additional functions.