In Amazon DynamoDB, the terms "hash key" and "range key" are associated with the concept of composite primary keys, which are used to uniquely identify items within a DynamoDB table. Here's an explanation of the differences between a hash key and a range key:

1. **Hash Key (Partition Key)**:

   - **Purpose**: ==The hash key, also known as the partition key, is the primary means of distributing data across multiple partitions in DynamoDB.== It determines the partition in which an item will be stored.
   
   - **Uniqueness**: ==Hash keys must be unique within the table.== Each item in the table must have a unique hash key value.

   - **Access**: When you perform a query or read operation on a DynamoDB table, you can use the hash key to look up a specific item or a range of items within a single partition.

   - **Example**: If you have a table of customer data, the customer ID could be a suitable hash key. ==Items with the same customer ID will be stored together in the same partition.==

2. **Range Key (Sort Key)**:

   - **Purpose**: ==The range key, also known as the sort key, is used to further organize data within a partition. It allows you to perform range queries and ordering operations on items within the same partition.==

   - **Uniqueness**: ==Range keys are not required to be unique within the table. Multiple items within the same partition can have the same range key value.==

   - **Access**: ==When you query or scan a DynamoDB table, you can use the range key to specify a range of values to retrieve==. This allows you to efficiently query data within a specific partition.

   - **Example**: In the customer data table example, if you want to store purchase orders for each customer and perform queries based on order date, you could use the order date as the range key. This allows you to retrieve orders for a specific customer within a given date range.

Here's a visual representation of how composite primary keys work in DynamoDB:

```
+----------------+--------------+
|   Hash Key     |   Range Key  |
+----------------+--------------+
|   Partition 1  |   Item 1     |
|   Partition 1  |   Item 2     |
|   Partition 2  |   Item 3     |
|   Partition 2  |   Item 4     |
|   Partition 3  |   Item 5     |
|   Partition 3  |   Item 6     |
+----------------+--------------+
```

- In this example, items are distributed across multiple partitions based on the hash key values (Partition 1, Partition 2, etc.).
- Within each partition, items can be organized and accessed based on the range key (Sort Key) values.

By using hash and range keys, DynamoDB offers efficient data distribution and querying capabilities. The choice of hash key and range key design depends on the specific access patterns and query requirements of your application.