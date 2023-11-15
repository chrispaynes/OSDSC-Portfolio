### Scheduled in Fivetran[link](https://fivetran.com/docs/transformations/dbt#scheduledinfivetran)

Fivetran connects to your Git provider and runs your dbt models in your destination according to the schedule that you choose in the Fivetran dashboard. We sync your dbt models from your Git provider every few minutes to ensure that we are up to date.


You create a transformation in the Fivetran dashboard for each dbt model that you want Fivetran to run. Each transformation consists of the following elements:

- ==**Output model**: A dbt model that transforms your data so it’s ready for analytics.==
- **Output model lineage**: All upstream models that are needed to produce the output model, starting from your source table references in dbt Core.
- **Schedule**: A customizable schedule that determines how often Fivetran runs your transformation.

> IMPORTANT: Each transformation references a single output model but executes all upstream models during each run.

By default, new transformations have the same schedule as their associated connectors, also known as a fully integrated schedule.


Fivetran pipelines use the following elements:

- The **start** is the interval that initiates the pipeline.
	- Each start node defines its own data pipeline.
- A **connector** updates source tables in the destination.
- A **junction** waits for multiple connectors to finish syncing before it triggers a dbt transformation.
- A **transformation** is a model or a collection of models that updates downstream tables in the destination.
- An **output model** generates an analytics-ready table. It is typically a leaf node on your data lineage graph.
- A **test** is an assertion that you make about the models in your dbt project. A test may succeed or fail independently of model execution.

![[Pasted image 20231114123846.png]]
Fivetran comes with a fixed set of start nodes corresponding to different sync frequencies. When you select a frequency in the dashboard, the pipelines that activate those syncs are aware of overlaps and automatically adjust to them. 

![[Pasted image 20231114124239.png]]