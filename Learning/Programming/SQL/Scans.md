In SQL, "scans" typically refer to methods of reading and accessing data in database tables. There are several types of scans, each with its own characteristics and use cases. Here are the common types of scans in SQL:

1. **Table Scan (Full Table Scan)**:
   - A table scan, also known as a full table scan, involves reading every row in a table to fulfill a query. It is often used when no suitable indexes are available to accelerate data retrieval.
   - Table scans can be slow and resource-intensive, especially for large tables, as they require reading and processing every row.

2. **Index Scan**:
   - An index scan is the process of using an index structure to quickly locate and retrieve rows that match the conditions of a query.
   - Index scans are typically much faster than full table scans because they reduce the number of rows that need to be examined.

3. **Clustered Index Scan**:
   - A clustered index scan is a specific type of index scan used in databases that support clustered indexes (e.g., SQL Server). A clustered index determines the physical order of rows in a table.
   - A clustered index scan reads the data pages in the order specified by the clustered index key.

4. **Non-Clustered Index Scan**:
   - A non-clustered index scan uses a non-clustered index to locate rows that satisfy the query conditions. Unlike a clustered index, non-clustered indexes do not dictate the physical order of rows in the table.
   - Non-clustered index scans can be effective when searching for specific rows based on indexed columns.

5. **Index Seek**:
   - An index seek is an operation that efficiently locates and retrieves rows using an index. It is more efficient than a full index scan because it directly navigates to the desired rows.
   - Index seeks are particularly useful for point queries (i.e., queries that retrieve a specific row) and range queries (i.e., queries that retrieve a range of rows).

6. **Bitmap Scan**:
   - A bitmap scan is a technique used in some database systems to combine the results of multiple index scans using bitmaps. It is especially effective for complex queries with multiple conditions and can reduce the number of rows to scan.
   - Bitmap scans are typically used in data warehousing environments.

7. **Index Merge Scan**:
   - An index merge scan involves scanning multiple non-clustered indexes and merging the results to find the rows that satisfy the query. This can be more efficient than a full table scan for certain queries.

8. **Table Index Scan**:
   - A table index scan is a combination of a full table scan and an index scan. It occurs when the query can't be satisfied entirely by the index, so the database scans both the table and the index.

9. **Sequential Scan**:
   - A sequential scan is a synonym for a full table scan. It refers to reading rows in the order they appear in the table without regard to any specific index.

The choice of which scan to use depends on various factors, including the structure of the database, the query conditions, the presence of indexes, and the overall performance requirements. Query optimization and the use of appropriate indexes are key strategies to improve query performance and reduce the need for full table scans.