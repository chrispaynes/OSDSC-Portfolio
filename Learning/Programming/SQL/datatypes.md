ANSI SQL (American National Standards Institute Structured Query Language) defines a set of standard data types that are commonly supported by most relational database management systems (RDBMS). These standard data types provide consistency and portability across different database platforms. While individual databases may have additional data types specific to their systems, ANSI SQL data types form the core set of types that you can expect to find in most RDBMS.

Here is a list of some common ANSI SQL data types:

1. **INTEGER**: Represents a whole number. The size (number of bytes) of an `INTEGER` can vary depending on the database system, but it typically stores values within the range of -2,147,483,648 to 2,147,483,647.

2. **SMALLINT**: Similar to `INTEGER`, but with a smaller range. It typically stores values from -32,768 to 32,767.

3. **BIGINT**: Represents a large integer. It can store very large whole numbers, often in the range of -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

4. **DECIMAL(precision, scale)**: Also known as `NUMERIC`, it is used for fixed-point decimal numbers. `Precision` indicates the total number of digits, while `scale` represents the number of decimal places. For example, `DECIMAL(10, 2)` can store numbers like 12345.67.

5. **REAL**: Represents a single-precision floating-point number, typically a 4-byte approximation of a real number.

6. **DOUBLE PRECISION**: Represents a double-precision floating-point number, often an 8-byte approximation of a real number.

7. **CHAR(n)**: Fixed-length character string where `n` is the maximum number of characters it can store. For example, `CHAR(10)` can store up to 10 characters.

8. **VARCHAR(n)**: Variable-length character string where `n` is the maximum number of characters it can store. It uses only as much space as needed for the actual data.

9. **TEXT**: A variable-length character string with no predefined maximum length. It can store large amounts of text.

10. **DATE**: Stores date values in the format YYYY-MM-DD.

11. **TIME**: Stores time values in the format HH:MM:SS.

12. **TIMESTAMP**: Combines date and time information. It stores both date and time values with fractional seconds precision.

13. **BOOLEAN**: Represents true or false values.

14. **BINARY(n)**: Fixed-length binary data, where `n` is the number of bytes it can store.

15. **VARBINARY(n)**: Variable-length binary data, similar to `VARCHAR`, but for binary data.

16. **BLOB**: Binary Large Object, used for storing large binary data such as images or documents.

17. **CLOB**: Character Large Object, used for storing large text data.

These are some of the common ANSI SQL data types, but keep in mind that different database systems may have variations or extensions to this list. When working with a specific database system, it's essential to consult the documentation for that system to understand the precise data types and their characteristics.