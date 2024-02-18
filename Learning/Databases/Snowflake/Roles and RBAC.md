https://www.analytics.today/blog/introducing-snowflake-rbac
https://www.analytics.today/blog/snowflake-system-defined-roles-best-practice
https://www.analytics.today/blog/designing-snowflake-role-based-access-solutions
https://aws.amazon.com/blogs/database/amazon-aurora-postgresql-database-authorization-using-role-based-access-control/
https://medium.com/slalom-technology/snowflake-role-based-access-control-rbac-approach-196e6afc699f
- create separate USER admin role
![[Pasted image 20240124154711.png]]

![[Pasted image 20240124163304.png]]


| Role Name | Purpose | RoleType |
| ---- | ---- | ---- |
| TRANSFORMER_FR | Transforms Raw data into Production | Functional |
| LOADER_FR | Loads Data into Raw | Functional |
| Reporter / User?<br>REPORTER_FR | ? | Functional |
| ENGINEER_FR | Engineers models | Functional |
| DATA_SCIENTIST_FR |  |  |
| DEV | can see account admin schema |  |
| Service/injester/reader/reporter? |  |  |
| GLOBAL_ENGINEER | R/W Dev, R staging, R prod |  |
| DEV\|STAGE\|PROD_DataScientist |  | Functional |
| DEV\|STAGE\|PROD_BI_ANALYST |  | Functional |
| DEV\|STAGE\|PROD_SysAdmin |  | Environment Admin |
| DEV\|STAGE\|PROD_SecurityAdmin |  | Environment Admin |
| DEV\|STAGE\|PROD_Read | This role has access to read the data in the database. An example of users that need a read-only role are the users who generate the reports or need to query the data on an ad hoc basis for troubleshooting business tickets. | Security Role |
| DEV\|STAGE\|PROD_Read/Write | This role can read as well as write and modify the data in the database. For example, the read/write role is granted to application users that are defined in the application code to connect to the database to perform the transactions in the tables. | Security Role |
| DEV\|STAGE\|PROD_DDL/ALTER | This role can read, write, and modify the data, and also alter the schema by making structural changes to the database objects. For example, the DDL role is granted to the users (or developers) who are deploying new code that requires schema changes in the database. | Security Role |
| `<USER DEPT>_FULL_DB_AR_RWC`<br>FIN_FULL_DB_AR_RWC<br>HR_SCHEMA1_AR_RWC | R (READ), W (WRITE, UPDATE, INSERT, DELETE), C (CONTROL) |  |
|  |  |  |
![[Pasted image 20240124154242.png]]

| Env |  |
| ---- | ---- |
| Development |  |
| QA / Stage |  |
| Production |  |

| RBAC Layer | Description |
| ---- | ---- |
| **Database Objects**  | At the lowest level is one or more databases containing schemas and database objects which must be secured. |
| **Security Roles**  | These are the first layer in role-based access and provide a predefined set of access controls. <br><br>Each role defines (and simplifies) the access to a given database and schema and provides **Read**, **Write**, **Execute** or **Full** access to the underlying schema objects.<br><br>These roles use Future Grants to automatically provide Select, Insert, Update, Delete or Execute access to underlying data. <br><br>_Full Access_ grants ownership access, and in the above example, the PROD_DATA_SCIENTIST role can create or drop tables in the SANDBOX schema.<br> |
| **Functional Roles**  | Are the second layer of role-based access and these roles are granted to individual users to perform a task. <br><br>Unlike the other roles in the account, these are named to indicate the task assigned the individual, for example PROD_BI_ANALYST or DEV_ENGINEER.<br> |
| **Environment Admin Roles:** <br>        <br> | Are the first layer of account control, and these give the ability to delegate admin responsibility for an _Environment._ <br><br>A Snowflake Environment is not a physical object, but an arbitrary collection of Roles, Virtual Warehouses and Databases which are managed as a single unit. This could be used, (for example), to provide access to a UAT, TEST or PROD environment. The roles at this level are:<br>    <br>- **PROD_SECURITY_ADMIN:** Which is used to create and own all the roles in the environment. This role performs a similar role to USERADMIN but for a given environment. This role has the privilege to CREATE ROLES, but can only manage the roles it owns within it’s own environment.<br>        <br> - **PROD_SYSADMIN:** Which is used to create and own the Database and Schemas in the environment. This role performs a similar role to SYSADMIN but for a given environment. This role has the privilege to CREATE DATABASEs. |
| **Account Admin Roles:**  | Unlike the Environment Admin roles which are limited to a single environment, these roles have control over every Virtual Warehouse, Role, Database and Schema in the entire Snowflake account. As defined in the [RBAC Best Practices](https://www.analytics.today/blog/snowflake-system-defined-roles-best-practice), these roles inherit privileges from the underlying Environment Admin Roles which maintains a consistent RBAC hierarchy. |


https://community.snowflake.com/s/question/0D5Do00000gWW3ZKAW/what-is-the-difference-between-ownership-and-usageif-i-have-ownership-is-it-the-same-as-having-usage
No. Ownership and usage privileges are two different types of privileges with distinct purposes.

Granting ownership privilege to a role gives it administrative control over the object, such as the ability to modify the object's structure, grant/revoke privileges on the object, and delete the object. **_It does not automatically grant the ability to use or interact with the object._**

To allow a role to use and perform actions on the object, such as querying data or modifying records, you need to grant **usage privilege separately**. This ensures that the role has both administrative control (ownership privilege) and the necessary permissions to use the object (usage privilege).

![[Pasted image 20240125211909.png|1000]]
![[Pasted image 20240125211856.png|1000]]
![[Pasted image 20240125214912.png]]
![[Pasted image 20240125211758.png]]
![[Pasted image 20240125211734.png]]
![[Pasted image 20240125213844.png]]
![[Pasted image 20240125211942.png]]
![[Pasted image 20240125213511.png]]
![[Pasted image 20240125211712.png]]

![[Pasted image 20240125212109.png]]


![[Pasted image 20240125212204.png]]
![[Pasted image 20240125212221.png]]
![[Pasted image 20240125212237.png]]
![[Pasted image 20240125212256.png]]
![[Pasted image 20240125212309.png]]

https://docs.snowflake.com/en/user-guide/security-access-control-privileges