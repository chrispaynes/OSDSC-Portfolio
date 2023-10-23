https://www.youtube.com/watch?v=5rNquRnNb4E&list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT

# Intro to Data Build Tool (dbt) // Create your first project!
- https://github.com/snowflakedb/snowflake-connector-python/issues/1679
- ![[Pasted image 20231006144717.png]]
- MOve snowflake profile in global cli profile config
- ![[Pasted image 20231006144820.png]]
	- have this profile use a non-admin non-elevated user role
- ![[Pasted image 20231006145811.png]]
	- tests if can connect using credentials
- ![[Pasted image 20231006145956.png]]
# 5 Tips to Improve Your dbt Project
1.  **TIP: Create a Staging Layer**
	1. ![[Pasted image 20231006150451.png]]
	2. cleaned up versions of raw tables
		1. rename columns
		2. data type casting
		3. simple conditionals
	3. each staging model should match 1:1 with each raw table
		1. the staging table should then be used downstream in DBT project instead of raw tables
2. **TIP: Use CTEs**
	![[Pasted image 20231006163336.png]]
	![[Pasted image 20231006163406.png]]
	1. use them as imports (referencing other tables) or just as a way to break apart large queries
	2. no negative implications of doing `select *` in a CTE. Query engine will figure out which column(s) to use when the CTE table is used in the query
	3. CTE's are pass-through
3. **TIP: Use Directories and Sub Directories**
	1. can set directory specific configuration options
	2. ![[Pasted image 20231006163604.png]]
	3. you can run models on a single dir
		1. `dbt run -m <directory>.*`
4. **TIP: Create a Style Guide **
	1. ensure consistency, easy reviews, easy onboarding
	2. conventions
		1. naming columns
	3. ![[Pasted image 20231006164531.png]]
	4. https://github.com/dbt-labs/corp
	5. https://docs.getdbt.com/guides/best-practices
5. **TIP: Don't Optimize for Fewer Lines**


# Add raw "sources" to your dbt project
https://www.youtube.com/watch?v=Y03CsVDK69Y&list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT&index=3

![[Pasted image 20231006170016.png]]

``` yaml
version: 2

sources:
  - name: <string> # required
    description: <markdown_string>
    database: <database_name>
    schema: <schema_name>
    loader: <string>
    loaded_at_field: <column_name>
    meta: {<dictionary>}
    tags: [<string>]
    
    # requires v1.1+
    config:
      <source_config>: <config_value>

    overrides: <string>

    freshness:
      warn_after:
        count: <positive_integer>
        period: minute | hour | day
      error_after:
        count: <positive_integer>
        period: minute | hour | day
      filter: <where-condition>

    quoting:
      database: true | false
      schema: true | false
      identifier: true | false

    tables:
      - name: <string> #required
        description: <markdown_string>
        meta: {<dictionary>}
        identifier: <table_name>
        loaded_at_field: <column_name>
        tests:
          - <test>
          - ... # declare additional tests
        tags: [<string>]
        freshness:
          warn_after:
            count: <positive_integer>
            period: minute | hour | day
          error_after:
            count: <positive_integer>
            period: minute | hour | day
          filter: <where-condition>

        quoting:
          database: true | false
          schema: true | false
          identifier: true | false
        external: {<dictionary>}
        columns:
          - name: <column_name> # required
            description: <markdown_string>
            meta: {<dictionary>}
            quote: true | false
            tests:
              - <test>
              - ... # declare additional tests
            tags: [<string>]
          - name: ... # declare properties of additional columns

      - name: ... # declare properties of additional source tables

  - name: ... # declare properties of additional sources
```

# How Does DBT Compile Queries
- every time DBT runs it will compile (templates, models, queries) and store query in Target directory
- ![[Pasted image 20231009090307.png]]

# Deploy a Custom Schema
- best practice is not to use public schema
- `Staging` schema is first layer that sits atop raw data sources
- ![[Pasted image 20231009090751.png]]
	- `config(...)` will override anything defined in project yaml
- ![[Pasted image 20231009090853.png]]
	- use the `+` prefix to add addl configs
	- DBT will create the schema if you haven't created it in the data base
- ![[Pasted image 20231009091019.png]]
	- default schema is a concatenation
- ![[Pasted image 20231009091432.png]]
	- override the default macro to change schema name with a custom one
	- filename should match macro name
# How to Test and Debug Models
![[Pasted image 20231009091650.png]]
![[Pasted image 20231009091713.png]]
![[Pasted image 20231009091727.png]]
![[Pasted image 20231009091849.png]]
![[Pasted image 20231009092106.png]]
- you can review the test cases in the `target` directory

# Change Materialization
![[Pasted image 20231009092306.png]]
![[Pasted image 20231009092353.png]]
- ![[Pasted image 20231009092558.png]]
- ![[Pasted image 20231009092658.png]]
	- change adjust in individual model file or in project file
# Package Management & DBT Hub
![[Pasted image 20231009092817.png]]
![[Pasted image 20231009092835.png]]
![[Pasted image 20231009093140.png]]
# DBT Docs
![[Pasted image 20231009093657.png]]
![[Pasted image 20231009093711.png]]
![[Pasted image 20231009093725.png]]
![[Pasted image 20231009093843.png]]
	- you can host this on a web server

# Using DBT Seeds with Static Data
![[Pasted image 20231009094127.png]]
![[Pasted image 20231009094257.png]]
![[Pasted image 20231009094323.png]]
![[Pasted image 20231009094358.png]]
![[Pasted image 20231009094433.png]]
![[Pasted image 20231009094543.png]]

# Create Custom Tests
![[Pasted image 20231009094710.png]]
- macro will essentially run `select count(*)` and consider any returned rows as validation errors
![[Pasted image 20231009095041.png]]
![[Pasted image 20231009142004.png]]
	- override existing test by moving test into macro and overwriting it with custom logic
# Add and Use DBT Project Variables
![[Pasted image 20231009142235.png|1000]]
![[Pasted image 20231009142608.png|1000]]
![[Pasted image 20231009142709.png|1000]]
# Use Hooks
![[Pasted image 20231009142828.png]]
![[Pasted image 20231009142903.png|1000]]
![[Pasted image 20231009143010.png|1000]]
![[Pasted image 20231009143416.png|1000]]
	- pre/post hooks are set on individual models

- can also run macros to keep project yaml cleaner
![[Pasted image 20231009143600.png|1000]]
![[Pasted image 20231009143734.png|1000]]
- hooks could be used to add seeds, grants, inserts
- https://hub.getdbt.com/brooklyn-data/dbt_artifacts/latest

Logging Package
# Docs Blocks
![[Pasted image 20231009144330.png]]
![[Pasted image 20231009144516.png]]
![[Pasted image 20231009144549.png|1000]]
![[Pasted image 20231009144647.png]]

**reduce duplication of definitions (consolidate)**
![[Pasted image 20231009144926.png]]
![[Pasted image 20231009145000.png]]
# Monitor Freshness in DBT
![[Pasted image 20231009152632.png]]
	- can add freshness to table or entire schema
	- - helps check if you're meeting SLAs
	- can check when a table is older than X
![[Pasted image 20231009152935.png]]
	- line 12 indicates which field/column to use to determine freshness
	- looks for all freshness blocks and runs as SQL like a test
![[Pasted image 20231009153019.png]]
	- need to validate that your timezones are running against correct/same timezone
	- don't want your DB's TZ to differ from DBT's TZ
![[Pasted image 20231009153855.png]]
![[Pasted image 20231010084646.png]]
	- add a where clause in test method to trim down data set
![[Pasted image 20231010084808.png]]
	- compiled output
# Using Snowflake query tags
![[Pasted image 20231010084919.png]]
![[Pasted image 20231010084959.png]]
	- can also set this at individual profile level to tag all of your queries
![[Pasted image 20231010085049.png]]
	- can set on all models or individual model
![[Pasted image 20231010085153.png]]
	- any action that is run will be logged with the query tag, helps with audit
# DBT state Method
![[Pasted image 20231010085425.png]]
	- comparing 2 manifests about a project

![[Pasted image 20231010085549.png]]
	- run `$ dbt compile` to create initial manifest stored in target dir
	- will need to copy or move manifest file to a new location so you can compare it with a newly compiled manifest
![[Pasted image 20231010085852.png]]

# Multi Repo Approach / Team Specific Repos + 1 Shared/Global Repo
![[Pasted image 20231010090044.png]]
	- shared repo has common packages and macros and get used by other repos
![[Pasted image 20231010090202.png]]
![[Pasted image 20231010090410.png]]
![[Pasted image 20231010090614.png]]
	- need to prefix the macro name with the name of the project
# Audit DB Runs
![[Pasted image 20231010090759.png]]
	- helpful for tracking stuff with a specific run
![[Pasted image 20231010090945.png]]
	- invocation ID is unique for per run, but the value is a globally shared between models
	- can use this ID to track which/when records were updated, inserted, etc. and then tie it back to an audit table
![[Pasted image 20231010091149.png]]
# Install DBT in Virtual Environment
- create DBT virtual env
- `pip install --upgrade dbt` or install dbt from source
- init or pull in your DBT project repo
# Cleaning DBT Project Files
![[Pasted image 20231010091749.png]]
# Run Tests and Models in Groups
![[Pasted image 20231010092105.png]]
![[Pasted image 20231010092205.png]]
![[Pasted image 20231010092138.png]]
![[Pasted image 20231010092343.png]]
![[Pasted image 20231010092418.png]]
	- can set multiple tags
	- can set on model, sources, seeds, snapshots and analyses ( example tag column as PII)
	- use tags to help select models to run
![[Pasted image 20231010092752.png]]
	- set tag on test
![[Pasted image 20231010093033.png]]
- excluding running using tags
# How do Ephemeral Models (CTEs) Work

![[Pasted image 20231010093244.png]]
	- 
![[Pasted image 20231010093346.png]]
- nothing is deployed for ephemeral mats
![[Pasted image 20231010093423.png]]
	- you can still ref CTE using `ref`
![[Pasted image 20231010093517.png]]
	- this will compile as transient table
# Handle JSON in Jinja and Macros
![[Pasted image 20231010105251.png]]
	- want this put into flat model
![[Pasted image 20231010105449.png]]
![[Pasted image 20231010105402.png]]
![[Pasted image 20231010105432.png]]
![[Pasted image 20231010105508.png]]
![[Pasted image 20231010105626.png]]
	- the end goal will be to get all column names from nested json and use array of col names to compile sql
![[Pasted image 20231010105753.png]]
	- jinja function for run query
	- `set` keyword is setting a variable for downstream use
![[Pasted image 20231010110229.png]]
![[Pasted image 20231010110351.png]]
![[Pasted image 20231010110711.png]]
	- use `{% if not loop.last %}` to prevent trailing commas in `SELECT` statement
	- remove `""` in value by casting to varchar `:varchar`
![[Pasted image 20231010110944.png]]
- create this as a macro
- this is hardcoding all as macros but we could dynamically infer data type
![[Pasted image 20231010111249.png]]
	- use CTE to save result set
# Use One DBT Project 
![[Pasted image 20231010121725.png]]
	- how DBT works
![[Pasted image 20231010121813.png]]
	- output holds different envs, `target` indicates default env
![[Pasted image 20231010121905.png]]
	- `dbt debug` output can use `dbt debug --target prod` to target another environment
	- you can change how your code is compiled based on the target/env in use
![[Pasted image 20231010123014.png]]
	- can use `target` value to change queries or sources
![[Pasted image 20231010123119.png]]
# Analyses Directory
- ephemeral ad-hoc SQL queries for analysis purposes with jinja templated or test
- used for reporting
- if you don't have permissions to deploy something
- use DBT functionality to compile code for your SQL
- can use macros, variables, etc
![[Pasted image 20231010123730.png]]
	- outcome is compiled to target dir
# 4 Step Process for Creating Models
![[Pasted image 20231010124205.png|1000]]
![[Pasted image 20231010124253.png|1000]]
![[Pasted image 20231010124404.png|1000]]
![[Pasted image 20231010124503.png|1000]]
1. **Step 1 - Imports / CTEs at the top**
	1. `select *` is fine for CTE because only the used columns will be pulled in
2. **Step 2 - CTEs and selects with custom logic**
3. **Step 3 - Final CTE**
	1. includes final columns as part of dataset
4. **Step 4 - `Select * from final`**
	1. return final CTE
# Managed Repos on DBT Cloud
### Create Project
### Create DB Connection
![[Pasted image 20231010124831.png]]
	- make sure to have a specific DBT User
![[Pasted image 20231010124949.png]]
### Add Repository
- DBT can temporarily host your Git repo
![[Pasted image 20231010130804.png]]
![[Pasted image 20231010130742.png]]
# Intro to DBT Cloud
![[Pasted image 20231010131220.png]]
![[Pasted image 20231010131109.png]]
	- different devs should have different schemas within the dev table to prevent overwriting other dev's change
![[Pasted image 20231010131256.png]]
![[Pasted image 20231010131310.png]]
![[Pasted image 20231010131334.png]]
![[Pasted image 20231010131611.png]]
![[Pasted image 20231010131627.png]]

![[Pasted image 20231010131637.png]]

- in DBT typically don't want to work, run from `master/main` branch
![[Pasted image 20231010131934.png|1000]]
	- can open PR's through DBT Cloud
![[Pasted image 20231010132054.png]]
- can run DBT jobs on a schedule directly from DBT cloud
- environments let's you manage diff envs
- data sources allows you to manage data sources, check freshness, etc
- - can host DBT docs on DBT cloud, but would require additional config
### settings
![[Pasted image 20231010132326.png]]

### environments (dev and deploy)
![[Pasted image 20231010132423.png]]
	- each user will have a separate dev environment
![[Pasted image 20231010132539.png]]
- typically want to run deploy env on `main/master` branch
- should also have a different user for service runs
![[Pasted image 20231010134323.png]]
	- can set the target to production
![[Pasted image 20231010134406.png]]
	- can change command to `dbt run`
![[Pasted image 20231010134450.png]]
	- can set on schedule
![[Pasted image 20231010134527.png]]
	- can call with webhooks
![[Pasted image 20231010134557.png]]
![[Pasted image 20231010134614.png]]
# Using Exposure
# Use DBT Operators for Dynamic Commands
# DBT Project Naming Conventions
# DBT Targets vs Environments
# DBT and Reverse ETL
# Intermediate Models
# Run Queries from Terminal
