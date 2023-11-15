# Overview
==Fivetran is a data integration platform that specializes in simplifying data pipeline orchestration and data syncing between various sources and destinations. It is designed to streamline the process of collecting, transforming, and loading data (commonly known as ETL) into a centralized data warehouse or data lake.==

Key features and aspects of Fivetran include:

1. ==**Automated Data Integration**: Fivetran automates the process of data integration, allowing users to set up data pipelines without writing custom code. ==This automation reduces the time and effort required for data integration.

2. ==**Connectors**: Fivetran provides pre-built connectors for a wide range of data sources, including databases, SaaS applications, marketing platforms, analytics tools, and more. These connectors simplify the process of extracting data from source systems.==

3. ==**Data Transformation**: While Fivetran focuses primarily on data extraction and loading (EL), it also offers basic data transformation capabilities, such as data type conversions and filtering, to prepare data for analytics.==

4. **Cloud-Based**: Fivetran is a cloud-based service, which means it can be deployed and managed in the cloud. It supports popular cloud data warehouses and storage platforms like Snowflake, BigQuery, Redshift, and more.

5. ==**Scheduling and Monitoring**: Users can schedule data syncs to occur at specific intervals and monitor the status and performance of their data pipelines through the Fivetran dashboard.==

6. **Schema Evolution**: Fivetran handles changes in source schemas, such as new columns or modifications to existing columns, without requiring manual adjustments.

7. **Security and Compliance**: Fivetran provides security features, encryption, and compliance with industry standards to ensure the security and privacy of data during transit and storage.

8. ==**Data Validation**: Fivetran includes data validation and error handling mechanisms to detect and report data synchronization issues.==

9. **Data Replication**: Fivetran uses log-based replication for certain databases, which allows it to capture changes to data in near real-time, ensuring that the destination remains up-to-date.

10. **Extensibility**: While Fivetran offers a wide range of connectors, it also supports custom connectors and API integrations for unique data sources.

Fivetran is commonly used by data engineers, data analysts, and data scientists to simplify the process of data ingestion, making it easier to centralize data from various sources into a data warehouse or data lake. This centralized data can then be used for analytics, reporting, and business intelligence purposes.


# Setup Demo
- https://youtu.be/z7AwXj-iP9c?feature=shared
- can connect to google sheet, google analytics, hubspot

![[Pasted image 20231109092209.png]]
![[Pasted image 20231109092118.png]]
	- can set a keypair
![[Pasted image 20231109092252.png]]
![[Pasted image 20231109092319.png]]
![[Pasted image 20231109092534.png]]
![[Pasted image 20231109092616.png]]
![[Pasted image 20231109092700.png]]
![[Pasted image 20231109092732.png]]
![[Pasted image 20231109092806.png]]
![[Pasted image 20231109092925.png]]
![[Pasted image 20231109092959.png]]
![[Pasted image 20231109093021.png]]
![[Pasted image 20231109093032.png]]

# FiveTran Product Demo 
![[Pasted image 20231109093212.png]]
- https://www.fivetran.com/connectors/hubspot

![[Pasted image 20231109093437.png]]
![[Pasted image 20231109093514.png]]
![[Pasted image 20231109093542.png]]
![[Pasted image 20231109093557.png]]
	- could use to automate S3 loads into snowflake
	- can build your own connector

![[Pasted image 20231109093916.png]]
![[Pasted image 20231109094000.png]]
- will normalize denormalized (JSON data) into table structure
![[Pasted image 20231109094125.png]]
	- auto creates ERDs

![[Pasted image 20231109094209.png]]
- will auto update destination when the source changes
- fivetran generally does not delete columns, will stop writing to it

![[Pasted image 20231109094257.png]]
- has Type II slowly changing dimensions
	- won't delete records, settings delete column to TRUE
![[Pasted image 20231109094439.png]]
