The dbt Semantic Layer allows your data teams to centrally define essential business metrics like `revenue`, `customer`, and `churn` in the modeling layer (your dbt project) for consistent self-service within downstream data tools like BI and metadata management solutions. The dbt Semantic Layer provides the flexibility to define metrics on top of your existing models and then query those metrics and models in your analysis tools of choice.

Resulting in less duplicate coding for data teams and more consistency for data consumers.

The dbt Semantic Layer has these main parts:

- Define your metrics in version-controlled dbt project code using [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow)
    - dbt_metrics is now deprecated
- Import your metric definitions using the [Discovery API](https://docs.getdbt.com/docs/dbt-cloud-apis/discovery-api)
- Query your metric data with the dbt Proxy Server
- Explore and analyze dbt metrics in downstream tools

### What makes the dbt Semantic Layer different?

==The dbt Semantic Layer reduces code duplication and inconsistency regarding your business metrics. By moving metric definitions out of the BI layer and into the modeling layer, your data teams can feel confident that different business units are working from the same metric definitions, regardless of their tool of choice. If a metric definition changes in dbt, it’s refreshed everywhere it’s invoked and creates consistency across all applications. You can also use the dbt Semantic Layer to query models and use macros.==