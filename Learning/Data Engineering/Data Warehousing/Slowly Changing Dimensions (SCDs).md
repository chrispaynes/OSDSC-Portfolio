In data warehousing and data management, ==Slowly Changing Dimensions (SCDs) refer to the types of changes that occur in the attributes of a dimension over time. Dimensions are used to describe and categorize data in a data warehouse, and SCDs help manage how changes to dimension attributes are handled and stored. There are several types of Slowly Changing Dimensions, commonly referred to as SCD types==. The most common SCD types are:

1. **Type 1 - No History**: In a Type 1 SCD, ==changes to dimension attributes are not preserved in the data warehouse. When an attribute value changes, the old value is simply overwritten with the new one. This approach is suitable when historical data is not needed, and you only want to store the current state of the dimension.==

2. **Type 2 - ==Historical Tracking**: In a Type 2 SCD, historical changes to dimension attributes are tracked by creating a new row for each change. This allows you to maintain a history of attribute values over time. Each row typically has an effective date range indicating when the attribute values were valid. This approach is useful when you need to maintain a complete history of dimension changes.==
	![[Pasted image 20231006141801.png]]

4. **Type 3 - ==Previous Value**: In a Type 3 SCD, a limited history of attribute changes is stored. Instead of creating multiple rows, only selected attributes have their historical values preserved. Typically, this involves having columns to store the previous and current values for a subset of attributes. This approach is useful when you have limited storage capacity and only need to track changes for specific attributes.==
	![[Pasted image 20231006141827.png]]

6. **Type 4 - ==Outrigger Table or Mini-Dimension**: In a Type 4 SCD, historical changes are tracked by creating an associated "outrigger" or "mini-dimension" table. The main dimension table stores the current dimension data, while the outrigger table stores historical changes. This approach helps maintain a history of dimension changes without bloating the main dimension table.==
	![[Pasted image 20231006141904.png]]

8. **Type 6 - ==Hybrid**: Type 6 SCDs combine features of multiple SCD types. For example, you might use Type 1 for certain attributes, Type 2 for others, and Type 3 for a few more. This approach allows you to tailor the SCD handling to specific attributes within the same dimension.==

The choice of which SCD type to use depends on the specific requirements of your data warehousing and reporting needs. Factors to consider include data volume, storage capacity, the need for historical analysis, and the complexity of queries. Different SCD types strike a balance between retaining historical data and managing storage costs.

Additionally, there are variations and extensions of these common SCD types, and you can customize your SCD implementation to fit your organization's unique data management requirements.