## List of type definitions

|Type|Category|Description|
|---|---|---|
|[`average`](https://cloud.google.com/looker/docs/reference/param-measure-types#average)|Aggregate|Generates an average (mean) of values within a column|
|[`average_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#average_distinct)|Aggregate|Properly generates an average (mean) of values when using denormalized data. _See the definition below for a complete description._|
|[`count`](https://cloud.google.com/looker/docs/reference/param-measure-types#count)|Aggregate|Generates a count of rows|
|[`count_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#count_distinct)|Aggregate|Generates a count of unique values within a column|
|[`date`](https://cloud.google.com/looker/docs/reference/param-measure-types#date)|Non-aggregate|For measures that contain dates|
|[`list`](https://cloud.google.com/looker/docs/reference/param-measure-types#list)|Aggregate|Generates a list of the unique values within a column|
|[`max`](https://cloud.google.com/looker/docs/reference/param-measure-types#max)|Aggregate|Generates the maximum value within a column|
|[`median`](https://cloud.google.com/looker/docs/reference/param-measure-types#median)|Aggregate|Generates the median (midpoint value) of values within a column|
|[`median_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#median_distinct)|Aggregate|Properly generates a median (midpoint value) of the values when a join causes a fanout. _See the definition below for a complete description._|
|[`min`](https://cloud.google.com/looker/docs/reference/param-measure-types#min)|Aggregate|Generates the minimum value within a column|
|[`number`](https://cloud.google.com/looker/docs/reference/param-measure-types#number)|Non-aggregate|For measures that contain numbers|
|[`percent_of_previous`](https://cloud.google.com/looker/docs/reference/param-measure-types#percent_of_previous)|Post-SQL|Generates the percent difference between displayed rows|
|[`percent_of_total`](https://cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total)|Post-SQL|Generates the percent of total for each displayed row|
|[`percentile`](https://cloud.google.com/looker/docs/reference/param-measure-types#percentile)|Aggregate|Generates the value at the specified percentile within a column|
|[`percentile_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct)|Aggregate|Properly generates the value at the specified percentile when a join causes a fanout. _See the definition below for a complete description._|
|[`running_total`](https://cloud.google.com/looker/docs/reference/param-measure-types#running_total)|Post-SQL|Generates the running total for each displayed row|
|[`string`](https://cloud.google.com/looker/docs/reference/param-measure-types#string)|Non-aggregate|For measures that contain letters or special characters (as with MySQL's `GROUP_CONCAT` function)|
|[`sum`](https://cloud.google.com/looker/docs/reference/param-measure-types#sum)|Aggregate|Generates a sum of values within a column|
|[`sum_distinct`](https://cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct)|Aggregate|Properly generates a sum of values when using denormalized data.<br><br>_See the definition below for a complete description._|
|[`yesno`](https://cloud.google.com/looker/docs/reference/param-measure-types#yesno)|Non-aggregate|For fields that will show if something is true or false|
|`int`|Non-aggregate|REMOVED 5.4 Replaced by [`type: number`](https://cloud.google.com/looker/docs/reference/param-measure-types#number)|