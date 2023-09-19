# https://datameshlearning.com/?utm_source=rss&utm_medium=rss
# [Straining Your Data Lake Through A Data Mesh](https://www.dataengineeringpodcast.com/zhamak-dehghani-data-mesh-episode-90/)
- ## Data Lake is alternative to Data Warehouse
	- holds the raw data in the raw format so consumers can use it in the way they see fit or model it their way
	- lake would hold multiple raw data directly from the source — from all corners of the business
	- mostly used for analytical purposes
	- single location where pipelines can connect to
	- centralized, monolithic location, BI, ML, Analytics
	- **Data Warehouse** has pristine modeled data, strong schema, design and use case
	- this is a monolithic pattern
	- might be hard to version the datasets and decouple the data
	- using ELT instead of ETL
	- all data is co-lated so there is no latency combining data sets
		- but you do lose domain knowledge
	- oriented around a central team of data practitioners — can be hard to find these people
		- tech is always changing
		- job titles and requirements is changing
		- industry has not provided career paths or development or opportunities to evolve in the role
			- data engineers, siloed skill sets
			- software engineers are also left out of this domain and don't have the opportunity to add this to their toolbelt
		- hasn't integrated modern engineers practices
			- data versioning
			- continuous delivery
			- testing
			- growth
		- need the knowledge of all the tool
- Data Lake needs to account for diverse stakeholders, teams, users, data — who often have little/no direct incentive
- People often fail to scale diverse user cases and consumer patterns and changing bus. needs
- How do you actually use the data for business goals
- If data is only in one place (centralized), then typically a single team needs to manage that
	- that team becomes a bottleneck for other parts of the business
	- have a single infrastructure can limit the data and data use because the infrastructure might not work for all the data sources
	- also creates, silos, siloed skillsets based on technical skills — prefer to have individual teams own their infrastructure and domain
	- a centralized team likely can't understand the entire domain (and changes) of a different team's data sets, business initiatives
	- frustrating for the centralized teams and the consumers
- need to consider distributed systems architecture for data architectures
- businesses move fast and changes happen concurrently throughout multiple domains
	- having a monolith Data Lake can slow down the change
- one team to rule them all doesn't work — doesn't scale
	- forces the team to use pipelines, data marts, infrastructures, etc.
- build microservices around different domains so that the changes are localized to the different domains
- better to just embed into practitioners onto business teams
- data mesh data from different teams should still be joinable to other data sets
- one argument is that this is a lot of work required for teams to create this — how is this feasible
	- ETL pipelines
	- extract data
	- changes
	- docs
- this brings more cohesion between different data domains
- Data  Platform Team provides underlying resources to store, process and distribute the data
- need people embedded in all the different Data Product teams to provide education, information about how to leverage all the services
- there are parallels to how useful and ubiquitous the SRE role is to product development
- distributed ownership
- product and platform thinking
- large undertaking
- counter culture to the norms
	- today we don't argue about how normal it is for a platform team to have APIs
	- goal is to have the same for internal data
- currently data is siloed and teams are not incentivized to share or maintain their data
- lots of data needs to be unlocked and used in a meaningful way
- there are definitely tradeoffs
- data mesh doesn't mean starting over, can apply practices and learnings from data lakes, warehouses, etc.
- Data Mesh is meant to alleviate pain points with data pipelines, freshness, quality, iteration, scaling, etc. — if it's not broken, don't fix it
	- make sure this solves a problem your organization has
- data really needs open standardization and converge on an ecosystem of tools
	- similar to how engineering used Docker, Kubernetes, Version Control, Test Frameworks, CI/CD
## other areas worth bring to ML/Analytics/Data Engineering Teams
- continuous delivery — when data changes
- versioning (models, models)
- backward compatibility 
- testing (models)
- deployment
## start with this approach
- 1 physical data team that brings SMEs from different domains into the teams
- decouple domain data
- build this out 1 domain at a time
- find the business domains that go through frequent change — separate this one first
- create separate repos and pipeline for different domains
- separate backlogs, jira, etc
- on day 1 still working together under a single program with the same goal
- once this matures, branch out to autonomous domain teams
- this is a journey with mistakes
## How would you structure the Data Mesh?
### Principles
#### Data is Owned and Organized through individual business the Domains/teams
- data produced or constructed should be a first class asset — these are data products
- systems that are generating data
- these teams are responsible for providing data in a consumable way to the rest of the org
- ownership data now becomes distributed and in the hands of those who best know the data
- team doesn't and probably should consumer from the same DB/store their consumers consume from
- some data may be raw, others timeseries, aggregations, views, materialized views
- distributed data domain does not mean the physical storage of the data needs to remain distributed
####  Bring "product" thinking to the world of data aka "Domain Data Product"
- put all the appropriate tech, tooling, APIs in place to delight the data consumers
- need to understand your consumers/customers
- need to think about how you provide discoverability to the consumers (service discovery)?
	- API gateway
	- what are API's, endpoints, security, authorization, etc.
	- recommend single point of discovery for different data and data catalog
		- see metadata, owners, use cases, quality, last updated, cadence of update, sample data, etc.
			- every Data Product should register itself with this info with some tool
			- this could be published in Confluence as a first pass
- also data discovery
- you don't necessary need a super polished data model, it could your raw data with product thinking and self-serve incorporated into it
- would want schema consistency from product to product
- need to have good docs, schema, example data
- these could/should to integrate with other Data Products to become data products
- need to still retain interoperability and standardization for distributed systems to work
	- a customer will likely need to use multiple data products
	- global ID's for example for a user, mapping tables for different domains
	- timezone formats
	- schemas
	- consistent secure access model
#### Think of the infrastructure Platform (self-serve data infra)
- storage, logs, kafka
- need infrastructure to make this easy for other teams
	- discoverability, security, docs, etc
- the goal is decreased lead time for the data product team to get the dataset onto the Mesh Platform
- this requires bringing product thinking and people with those skills to different domains
	- these people care about data as a product
		- data lifecycle, features, versioning, SLO, quality metrics
- ops teams and likely SRE type role would need to support a distributed data mesh
	- compute, storage, networking, etc
- Domain team shouldn't need to work about the data storage, implementation, pipelines, etc.
- using REST and HTTP standards as inspiration

# Thought Exercise
## Data Products
### Looker Data (is currently a self-serve product)
### Hubspot Data
### Finance Team Data
### Marketing Data
### Partner Team Data
### Client Team Data
### Metrics Data
- aggregations
- YoY, Quarterly, Weekly Data
### Product/Engineering Team Data
- Jira Data
- Github data
### Platform Data
- Account Signups
- Social Graph Data
- User Accounts
- Engagements
- Opportunities
- Search Session
- Dwell Metrics
- Talent Sourcing
### Email Audit Data
### Notification Data
### Google Analytics Data
### Pendo Data
### PDL Data
### Crunchbase Data
