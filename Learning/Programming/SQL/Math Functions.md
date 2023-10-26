SQL provides several mathematical functions that allow you to perform mathematical operations on numeric data within your database. These functions are useful for calculations, transformations, and data manipulation. Here are some common SQL mathematical functions:

1. **ABS()**: Returns the absolute (positive) value of a number.

   Example:
   ```sql
   SELECT ABS(-10) AS absolute_value;
   ```

2. **ROUND()**: Rounds a numeric value to a specified number of decimal places.

   Example:
   ```sql
   SELECT ROUND(5.678, 2) AS rounded_value; -- Returns 5.68
   ```

3. **CEIL() or CEILING()**: Rounds a number up to the nearest integer greater than or equal to the original value.

   Example:
   ```sql
   SELECT CEIL(4.3) AS rounded_up; -- Returns 5
   ```

4. **FLOOR()**: Rounds a number down to the nearest integer less than or equal to the original value.

   Example:
   ```sql
   SELECT FLOOR(4.9) AS rounded_down; -- Returns 4
   ```

5. **SQRT()**: Calculates the square root of a number.

   Example:
   ```sql
   SELECT SQRT(25) AS square_root; -- Returns 5
   ```

6. **POWER() or POW()**: Raises a number to a specified power.

   Example:
   ```sql
   SELECT POWER(2, 3) AS result; -- Returns 8
   ```

7. **EXP()**: Returns the exponential value of a number (e^x).

   Example:
   ```sql
   SELECT EXP(1) AS exponential_value; -- Returns approximately 2.71828
   ```

8. **LOG()**: Calculates the natural logarithm of a number.

   Example:
   ```sql
   SELECT LOG(10) AS natural_logarithm; -- Returns approximately 2.30259
   ```

9. **LOG10()**: Calculates the base-10 logarithm of a number.

   Example:
   ```sql
   SELECT LOG10(100) AS base_10_logarithm; -- Returns 2
   ```

10. **MOD()**: Returns the remainder of a division operation (modulo).

   Example:
   ```sql
   SELECT MOD(10, 3) AS remainder; -- Returns 1
   ```

11. **RAND() or RANDOM()**: Generates a random decimal value between 0 and 1. The behavior of this function may vary between database systems.

   Example:
   ```sql
   SELECT RAND() AS random_value;
   ```

12. **TRUNCATE()**: Truncates a number to a specified number of decimal places without rounding.

   Example:
   ```sql
   SELECT TRUNCATE(5.678, 1) AS truncated_value; -- Returns 5.6
   ```

These SQL mathematical functions are essential for performing calculations on numeric data in your database. The specific functions available may vary depending on the database system you are using, so be sure to consult your database's documentation for the full list of supported functions and any system-specific variations.