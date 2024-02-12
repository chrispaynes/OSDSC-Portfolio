> If it's being built on, it probably shouldn't be a mart. If it's being externally used, it probably shouldn't be intermediate. So you're looking for another layer meant for both. That's what the Medallion architecture is for (an alternative to staging/intermediate/mart). It instead separates models being consumed from into 2 layers, a silver and a gold layer. The silver layer is optimized for usability, whether in DBT or another tool. The gold layer is optimized for consumption. You probably want to take your model and split it into 2 models, with 1 that provides the most usability e.g. provides all possible keys to join onto, and 1 that is built specifically for whatever it was originally meant for. That way you won't run into problems like new stuff using this model needs something added onto it that would break the other thing.

```
**Option 1** **![:one:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0031-fe0f-20e3@2x.png)**  
**Databases > Schemas:**  

- "RAW"

- 1 schema per source

- "STAGING"

- 1 schema per source

- "MART_DEV"

- INTERMEDIATE (intermediate models)
- CORE (fact, dimension & mart tables for Analytics)

- "MART_PROD"

- INTERMEDIATE (intermediate models)
- CORE (fact, dimension & mart tables for Analytics)
```

```
Callum O'Connor  [6 months ago](https://getdbt.slack.com/archives/CBSQTAPLG/p1683733678609119?thread_ts=1683730206.699849&cid=CBSQTAPLG)  

It looks like you’re basically deciding if prod/dev data should be distinguished at the database level or the schema level right? And then based off of that you’d have different naming conventions and architecture for your data marts.In my opinion I think it’s usually prudent to have your prod/dev data in different databases (Option ![:one:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0031-fe0f-20e3@2x.png)). This makes it way easier to distinguish between the two types of data and a big plus is that permissions in Snowflake are generally easier to work on at the database level.![:lock:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f512@2x.png)  You want to protect your production data at all costs, so putting strict restrictions on prod databases is safer and scalable than prod schemas across multiple databases. If you add a prod schema to a ‘CORE’ database for example, you’ll have to remember to safeguard that schema as well with permissions. Whereas if you add a new schema to a prod database it’ll automatically inherit the permissions you set at the database level.Also I noticed on Option ![:two:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0032-fe0f-20e3@2x.png)  you separated ‘STAGING’ into prod and dev, but not in Option ![:one:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/0031-fe0f-20e3@2x.png)  - I’d actually make sure to do this as well; having both prod and dev data in staging models is so so important for testing new concepts, debugging and generally protecting downstream models from development issues.
```

https://discourse.getdbt.com/t/how-we-used-to-structure-our-dbt-projects/355
- In comparison, the (recently updated) [best practices 3.7k](https://docs.getdbt.com/docs/best-practices) reflect principles that we believe to be true for any dbt project. Of course, these two documents go hand in hand – our projects are structured in such a way that makes the those principles easy to observe, in particular:

- Limit references to raw data
- Rename and recast fields once
- Group your models in directories
- Add tests to your models
- Consider the information architecture of your data warehouse
- Separate source-centric and business-centric transformations

> Of note here is that there is a distinct change that occurs between the staging and marts checkpoints – sources and staging models are source-centric, whereas marts models are business-centric.

This layer of modeling is considerably more complex than creating staging models, and the models we _design_ are highly tailored to the analytical needs of an organization. As such, we have far less convention when it comes to these models. Some patterns we’ve found to be useful are:

- `fct_` and `dim_` models should be materialized as tables within a warehouse to improve query performance. As a default, we use the table materialization, and where performance requires it, we use the incremental materialization.
- Intermediate transformations required to get to a fact or dimension model are placed in a nested `marts/<mart>/intermediate` directory. They are named `<useful_name>__<transformation_in_past_tense>.sql`. The lack of prefix and use of double underscores indicates that these are intermediate models, not to be trusted, however, it may also be worth hiding these in a different [schema 568](https://docs.getdbt.com/docs/using-custom-schemas).
- Models are tested and documented in a `<dir_name>.yml` file in the same directory as the models.
- Any extra documentation in a [docs block 199](https://docs.getdbt.com/reference#doc) is placed in a `<dir_name>.md` file in the same directory.