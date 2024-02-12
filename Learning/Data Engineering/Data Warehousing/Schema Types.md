https://streamsets.com/blog/schemas-data-warehouses-star-galaxy-snowflake/
- Data warehouse schema is a description, represented by objects such as tables and indexes, of how data relates logically within a data warehouse. Star, galaxy, and snowflake schema are types of warehouse schema that describe different logical arrangements of data.  Also known as multi-dimension schemas, these schemas define rules for how these data warehouses manage the names, descriptions, associated data items, and aggregates within a data warehouse. 
- ## What is a Data Warehouse Schema?
	- The basic components of all data warehouse schemas are fact and dimension tables. The different combination of these two central elements compose almost the entirety of all data warehouse schema designs.
	- Fact Table
		- A fact table aggregates metrics, measurements, or facts about business processes. In this example, fact tables are connected to dimension tables to form a schema architecture representing how data relates within the data warehouse. Fact tables store primary keys of dimension tables as foreign keys within the fact table. 
	- Dimension Table
		- Dimension tables are non-denormalized tables used to store data attributes or dimensions. As mentioned above, the primary key of a dimension table is stored as a foreign key in the fact table. Dimension tables are not joined together. Instead, they are joined via association through the central fact table.
- ## 3 Types of Schema Used in Data Warehouses
### Star Schema
The star schema in a data warehouse is historically one of the most straightforward designs. This schema follows some distinct design parameters, such as only permitting one central table and a handful of single-dimension tables joined to the table. In following these design constraints, star schema can resemble a star with one central table, and five dimension tables joined (thus where the star schema got its name). 

Star Schema is known to create denormalized dimension tables – a database structuring strategy that organizes tables to introduce redundancy for improved performance. Denormalization intends to introduce redundancy in additional dimensions so long as it improves query performance.

![[Pasted image 20231120121801.png]]
#### Characteristics of the Star Schema: 
- Star data warehouse schemas create a denormalized database that enables quick querying responses
- The primary key in the dimension table is joined to the fact table by the foreign key
- Each dimension in the star schema maps to one dimension table
- Dimension tables within a star scheme are not to be connected directly
- Star schema creates denormalized dimension tables
### Snowflake Schema
- The Snowflake Schema is a data warehouse schema that encompasses a logical arrangement of dimension tables. This data warehouse schema builds on the star schema by adding additional sub-dimension tables that relate to first-order dimension tables joined to the fact table. 
- Just like the relationship between the foreign key in the fact table and the primary key in the dimension table, with the snowflake schema approach, a primary key in a sub-dimension table will relate to a foreign key within the higher order dimension table. 
- Snowflake schema creates normalized dimension tables – a database structuring strategy that organizes tables to reduce redundancy. The purpose of normalization is to eliminate any redundant data to reduce overhead. 
![[Pasted image 20231120121841.png]]
#### Characteristics of the Snowflake Schema:  
- Snowflake Schema are permitted to have dimension tables joined to other dimension tables
- Snowflake Schema are to have one fact table only
- Snowflake Schema create normalized dimension tables
- The normalized schema reduces required disk space for running and managing this data warehouse
- Snowflake Scheme offer an easier way to implement a dimension
### Galaxy Schema / Fact-Constellation
The Galaxy Data Warehouse Schema, also known as a Fact Constellation Schema, acts as the next iteration of the data warehouse schema. Unlike the Star Schema and Snowflake Schema, the Galaxy Schema uses multiple fact tables connected with shared normalized dimension tables. Galaxy Schema can be thought of as star schema interlinked and completely normalized, avoiding any kind of redundancy or inconsistency of data.

![[Pasted image 20231120121941.png]]
#### ![galaxy schema visual example](https://streamsets.b-cdn.net/wp-content/uploads/Galaxy-Schema.png)

#### Characteristics of the Galaxy Schema:  

- Galaxy Schema is multidimensional acting as a strong design consideration for complex database systems
- Galaxy Schema reduces redundancy to near zero redundancy as a result of normalization
- Galaxy Schema is known for high data quality and accuracy and lends to effective reporting and analytics

![[Pasted image 20231120122024.png]]

- ## What is a Star Schema in a Data Warehouse?
- ## What is a Snowflake Schema?
- ## What is a Galaxy Schema?
- ## Key Differences Between Star, Snowflake, and Galaxy schema


https://www.educba.com/galaxy-schema/
- Usually, the Schema type is chosen based on multiple parameters that are thought to be important for any given Project, by the Project Management team. Here are the basic characteristics of the Galaxy Schema that can help in making the choice,

- This model can involve more than one fact table and many dimension tables
- All the dimension tables are normalized until there is no more space for further normalization.
- Galaxy Schema makes it possible for the data in the Database to be more distinct, in contrast to star schema but similar to snowflake schema.
- The Fact Table will have all the facts/ measures, while the Dimension Tables will have foreign keys to connect with the Fact Table.
- Galaxy Schema allows the Dimension Tables to be linked to other Dimension tables, including the Dimension Tables in the first level.
- This Multidimensional nature makes it easy to implement on complex Relational Database systems, thus resulting in effective Analysis & Reporting processes.
- In terms of Accessibility, Complex multiple levels of Join queries are required to fetch aggregated data from the center fact table, using the foreign keys to access all the required Dimension tables, as the system itself is more complex.
- Multiple Dimension tables, which are created as a result of normalization, serve as lookup tables when querying with complex multi-level Join queries.
- The process of breaking down all the Dimension tables into multiple small Dimensions until it is completely normalized takes up a lot of storage space compared to other schemas.
- As the system and querying process is multifaceted, the speed of Data Retrieval from the database systems is by very slow.
- Different fact tables are explicitly assigned to each of the dimensions available. This is advantageous for facts associated with the given dimension table, and also for other facts that can have a deeper dimension level.
