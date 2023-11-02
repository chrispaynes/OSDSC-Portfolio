## Definition

An optional configuration for grouping models, analysis, snapshots, tests, and metrics. When a resource is grouped, dbt will allow it to reference private models within the same group.

For more details on reference access between resources in groups, check out [model access](https://docs.getdbt.com/docs/collaborate/govern/model-access#groups).

## Examples

### Prevent a 'marketing' group model from referencing a private 'finance' group model

This is useful if you want to prevent other groups from building on top of models that are rapidly changing, experimental, or otherwise internal to a group or team.

models/schema.yml

```
models:  - name: finance_model    access: private    group: finance  - name: marketing_model    group: marketing
```

models/marketing_model.sql

```
select * from {{ ref('finance_model') }}
```

```
$ dbt run -s marketing_model...dbt.exceptions.DbtReferenceError: Parsing Error  Node model.jaffle_shop.marketing_model attempted to reference node model.jaffle_shop.finance_model,   which is not allowed because the referenced node is private to the finance group.
```

# Add groups to your DAG

New functionality

This functionality is new in v1.5.

## Related docs

- [Model Access](https://docs.getdbt.com/docs/collaborate/govern/model-access#groups)
- [Group configuration](https://docs.getdbt.com/reference/resource-configs/group)
- [Group selection](https://docs.getdbt.com/reference/node-selection/methods#the-group-method)

## About groups

A group is a collection of nodes within a dbt DAG. Groups are named, and every group has an `owner`. They enable intentional collaboration within and across teams by restricting [access to private](https://docs.getdbt.com/reference/resource-configs/access) models.

Group members may include models, tests, seeds, snapshots, analyses, and metrics. (Not included: sources and exposures.) Each node may belong to only one group.

### Declaring a group

Groups are defined in `.yml` files, nested under a `groups:` key.

models/marts/finance/finance.yml

```
groups:  - name: finance    owner:      # 'name' or 'email' is required; additional properties allowed      email: finance@jaffleshop.com      slack: finance-data      github: finance-data-team
```

### Adding a model to a group

Use the `group` configuration to add one or more models to a group.

- Project-level
- Model-level
- In-file

dbt_project.yml

```
models:  marts:    finance:      +group: finance
```

### Referencing a model in a group

By default, all models within a group have the `protected` [access modifier](https://docs.getdbt.com/reference/resource-configs/access). This means they can be referenced by downstream resources in _any_ group in the same project, using the [`ref`](https://docs.getdbt.com/reference/dbt-jinja-functions/ref) function. If a grouped model's `access` property is set to `private`, only resources within its group can reference it.

*models/schema.yml*
``` yaml
models:
  - name: finance_private_model
    access: private
    config:
      group: finance

  # in a different group!
  - name: marketing_model
    config:
      group: marketing
```


```

models/marketing_model.sql

```
select * from {{ ref('finance_model') }}
```

```
$ dbt run -s marketing_model...dbt.exceptions.DbtReferenceError: Parsing Error  Node model.jaffle_shop.marketing_model attempted to reference node model.jaffle_shop.finance_model,   which is not allowed because the referenced node is private to the finance group.
```

[](https://github.com/dbt-labs/docs.getdbt.com/edit/current/website/docs/docs/build/groups.md)

```

*dbt_project.yml*
``` yaml
models:
  my_project_name:
    marts:
      customers:
        +group: customer_success
      finance:
        +group: finance
```


*models/marts/customers.yml*
``` yaml
# First, define the group and owner
groups:
  - name: customer_success
    owner:
      name: Customer Success Team
      email: cx@jaffle.shop

# Then, add 'group' + 'access' modifier to specific models
models:
  # This is a public model -- it's a stable & mature interface for other teams/projects
  - name: dim_customers
    group: customer_success
    access: public
    
  # This is a private model -- it's an intermediate transformation intended for use in this context *only*
  - name: int_customer_history_rollup
    group: customer_success
    access: private
    
  # This is a protected model -- it might be useful elsewhere in *this* project,
  # but it shouldn't be exposed elsewhere
  - name: stg_customer__survey_results
    group: customer_success
    access: protected
```