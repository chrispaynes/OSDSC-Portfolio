# Overview
Global Secondary Index (GSI) and Local Secondary Index (LSI) are two types of secondary indexes in Amazon DynamoDB, and they serve different purposes in query optimization. Here are the key differences between them:

1. **Scope**:
   - ==**Global Secondary Index (GSI)**: A GSI is an index that spans the entire DynamoDB table. It allows you to query the table using attributes that are not part of the table's primary key. GSIs are useful for scenarios where you want to perform queries that aren't covered by the table's primary key or local secondary indexes. GSIs can be created and deleted independently of the table.==
   - ==**Local Secondary Index (LSI)**: An LSI is an index that is created along with the table and has the same partition key as the table's primary key but a different sort key. LSIs are useful when you want to query the data with the same partition key but different sort keys. They are scoped to the table they are created in.==

2. **Creation Time**:
   - ==**Global Secondary Index (GSI)**: GSIs can be created or deleted at any time after the table is created. You can add multiple GSIs to a table, each designed for different query patterns.==
   - ==**Local Secondary Index (LSI)**: LSIs must be defined when creating the table. Once the table is created, you cannot add or remove LSIs. If you need to change the indexing pattern, you would need to recreate the table.==

3. **Attributes Covered**:
   - ==**Global Secondary Index (GSI)**: GSIs can cover attributes that are not part of the table's primary key. This makes them suitable for a wider range of query patterns.==
   - **Local Secondary Index (LSI)**: LSIs cover attributes that are part of the table's primary key. They are limited to queries within the same partition key as the table's primary key.

4. **Query Flexibility**:
   - ==**Global Secondary Index (GSI)**: GSIs provide more flexibility in query patterns because they can span multiple partition keys and sort keys. This allows you to perform queries that involve different attribute combinations.==
   - **Local Secondary Index (LSI)**: LSIs are more limited in terms of query flexibility because they are constrained to the same partition key as the table's primary key.

5. **Data Distribution**:
   - ==**Global Secondary Index (GSI)**: GSIs have their own partition and sort key design, and they distribute data independently from the table's primary key. This can lead to different data distribution patterns.==
   - ==**Local Secondary Index (LSI)**: LSIs share the same partition key as the table's primary key. They don't introduce additional data distribution considerations.==

When choosing between GSI and LSI, consider your specific query patterns and data access requirements. If you need to perform queries that involve different attributes, especially those not covered by the table's primary key, GSIs are the preferred choice. On the other hand, if your queries are mostly within the same partition key as the table's primary key and involve different sort keys, LSIs may be more appropriate.

Keep in mind that both GSIs and LSIs come with some additional cost and storage considerations, so it's essential to design your secondary indexes thoughtfully to optimize query performance while managing costs.

# Key Schema
==In Amazon DynamoDB, a Global Secondary Index (GSI) Key Schema defines the structure of the index key for a Global Secondary Index. It specifies the attributes that are used as the index's partition key and sort key (if applicable) in order to enable efficient querying of data based on those attributes.== The GSI Key Schema is a crucial component of creating a GSI and defining how data is indexed.

Here are the key components of a GSI Key Schema:

1. **Partition Key**:
   - ==The partition key is required and defines the attribute that is used as the primary means of distributing data across the index's partitions.==
   - ==It determines the partition in which an item will be stored within the GSI.==
   - ==Queries against the GSI can efficiently retrieve items based on this partition key.==
   - ==The partition key in a GSI can be different from the partition key in the base table's primary key.==

2. **Sort Key (Optional)**:
   - ==The sort key is optional and defines an attribute that is used for sorting and further organizing data within the same partition.==
   - ==When you perform queries on the GSI, you can use the sort key to perform range queries or to retrieve items in a specific order.==
   - ==If specified, the sort key must be used in combination with the partition key to uniquely identify items in the index.==
   - ==The sort key in a GSI can be different from the sort key in the base table's primary key.==

Here's an example of a GSI Key Schema:

Let's say you have a DynamoDB table storing information about books. The table's primary key consists of a hash key (ISBN) and a range key (PublicationDate). You want to create a GSI that allows you to query books by Author (AuthorName) efficiently.

- GSI Name: AuthorIndex
- GSI Key Schema:
  - Partition Key: AuthorName (This is the attribute used for partitioning the GSI.)
  - Sort Key: ISBN (This is an optional sort key that can be used for sorting books by ISBN within the same AuthorName partition.)

==With this GSI Key Schema, you can efficiently query books by AuthorName, and if needed, perform range queries or sorting on ISBN within each AuthorName partition.==

When defining a GSI Key Schema, it's important to consider the access patterns and query requirements of your application to ensure that the GSI efficiently supports the desired queries. DynamoDB allows you to create multiple GSIs for a table, each with its own unique Key Schema to cater to different query patterns.