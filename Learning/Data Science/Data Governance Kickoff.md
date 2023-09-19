![[Pasted image 20230829202858.png]]
- **Project Initiation**
	- Spend a lot of time initializing the project
	- Ask lots of good research questions
	- learn the stakeholders workflows, operational challenges, what they're trying to achieve, how long it's going to take
- Goal is to convert business problem into Data Science problem
	- ask data-oriented questions to answer business problem
- Know how to explain, teach and instruct stakeholders on how to use ML outcomes
	- explain what you've done and how it solves the problem
	- ask "What is your objective? If I get this right, what are you trying to achieve"? "How would you measure it?" What is success?
		- Don't assume you can build a system without the knowing the problems to be solved
		- There are a lot of good questions, but not all questions can yield a relevant business action — those questions are not good problems to solve
		- There can be good questions, but no meaningful signal in the data to effectively answer the question
			- these types of models get shelved because they don't serve a purpose or provide actionable insights
			- a lot of great solutions never get used because they don't solve an actual problem
- Don't be afraid to ask for more/better requirements
	- ask make it easier to get requiremnets, build a template to make it easy for someone to know what requirements and in what format
- Decision Debt
	- "underthinking decisions comes back to bite you"
- Not everything needs ML, sometimes there are just business rules that can reasonably predict an outcome
# The What / Overview
- treating data as a business asset
- sharing data
- cataloging data assets
- create standards and processes
- currently data is siloed and teams are not incentivized to share or maintain their data

# What it is NOT
- glamorous, the "DevOps" of data
- data gatekeeping
- not a technology

# The Why / Benefits?
- data as an asset
- reduce data silos
- more effectively use data to meet business objectives
- have higher quality (accurate, fresh, dense, voluminous) data
- uncover additional
- every company already has a data governance policy
- cost, security, bias
- manage data lifecycle (acquisition/creation -> archival/deletion)
- data in isolation often has less utility than combined data
- easier to communicate cross functionally when using the same data
- understand what data gaps — what additional data would be useful
- gain outside perspective on data
- collaboration

# The How / Specifics
- Data Owners
- Data Stewards (Technical & Non-Technical)
- Data Council
- Data Discovery Meetings
- 

# Some Challenges
- poor branding
- training
- typically involves a cultural shift
- work is never complete
- cross functional time commitment
- need to adapt to your org — a lot of how implement X depends on org specific factors
- need a "corporate" sponsor 
- scaling with the organization
- maintain momentum and compliance
- define, measure, maintain and communicate success

# Data Mesh?
- Conceptual framework — isn't a tool you can buy
- decentralized/microservices approach to data within your org
- consider distributed systems architecture for data architectures
- meant to alleviate pain points with data pipelines, freshness, quality, iteration, scaling, etc.

## Principles
### Data is Owned and Organized through Individual Business Domains/teams
- data produced or constructed is first class asset aka "data product"
- teams are responsible for providing data in a consumable way to the rest of the org
- ownership data now becomes distributed and in the hands of those who best know the data
- distributed data domains does not mean the physical storage of the data needs to remain distributed

### Bring "product" thinking to the world of data via "Domain Data Products"
- put tech, tooling, APIs in place to "delight" the data consumers
- provide data discoverability to the consumers — similar to service discovery in distributed computing
- data products don't require polished data models, could be as self as providing raw data on a self-serve level
- goals: API consistency from product to product, good docs, schema, example data
- products need to retain interoperability and some standardization for effective integration with other products

### Create a Self-Serve Data Infrastructure Platform
- need infrastructure to make this easy for other teams
	- data discoverability, security, docs, etc
- bringing product mindset and people with those skills to different business domains
- focus on data lifecycle, features, versioning, SLO, quality metrics
- Domain teams shouldn't need to work about the data storage, implementation, pipelines, etc.

## Starting Point Recommendation
- 1 data team that periodically brings SMEs from different domains into the teams
- on day 1 still working together under a single program with the same goal
- decouple data domains
- build out 1 domain at a time
- once this matures, branch out to other domain teams
- find the business domains that goes through frequent changes — separate this one first
- create separate repos and mini-pipelines for different domains
- separate jira backlogs, epics, etc
- 

# Next Steps?
- understand where we're at
- understand where we want to go
- gauge our capacity

# Potential Data Products
### Looker Data (is currently a self-serve product)
### Hubspot Data
### Finance Team Data
### Marketing Data
### Partner Team Data
### Client Team Data
### Metrics Data
- aggregations
- Timeseries: YOY, Quarterly, Weekly Data
- projections
### Product/Engineering Team Data
- Jira Data
- Platform generated data
- Github, Code Climate Data
- Cloudwatch Data
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

# Questions, Thoughts, Ideas


# Next Best Actions (NBA)
- ![[Pasted image 20230829220122.png|500]]
- ![[Pasted image 20230829220157.png|500]]
- Use DAMA DMBOK Data Gov wheel to create framework or matrix
- use Knowledge Essential to an Information Quality (IQ) Professional Table
- Create (from Data in Action Triangle)
	- Processes
	- Projects
	- Programs
- how people +1 or upvote crowd source
## Steps
1. **Find Your Data Framework**
    1. DATA MISSION STATEMENT
    2. 
    3. Define Data Governance
	    1. know your org well enough to define a framework that will meet its goal
	    2. Data Practitioners have a strategy
	    3. 
    4. Clarify Your Company’s Mission Statement
    5. Find Your Data Governance Framework
	    1. ![[Pasted image 20230829222939.png|500]]
		    1. https://www.gartner.com/smarterwithgartner/7-key-foundations-for-modern-data-and-analytics-governance
	    2. Values and outcomes
	    3. Trust
	    4. Accountability and Decision Rights
	    5. Transparency and Ethics
	    6. Risk and Security
	    7. Education and Training
	    8. Collaboration and Culture
    7. Your Next Step
2. **Select Data Stewards**
    1. What Are Data Stewards?
    1. Fill Your Council with the Right People
    1. Your Next Step
3. **Build Your Data Governance Council**
    1. Find the Most Effective Sponsor
    1. Convince Colleagues to Join Your Council
    1. Clarify the Cadence for Your Council Meetings
    1. Confirm Key Principles for Your Council
    1. Define Data Domains
    1. Write a Data Dictionary
    1. Your Next Step
4. **Write Your Data Roadmap**
    1. Assess Your Data’s Current State
    1. Create a Current State Process Map
    1. Design Your Desired Future State for Data Governance
    1. Choose Which Outcomes You’ll Use to Measure Success
    1. Put Prioritized Ideas on Your Data Roadmap
    1. Your Next Step
5. **Practice Governance-Driven Development**
    1. Ask if You Have the Right Data Infrastructure
    1. Include Technical Partners in Your Data Governance
    1. Build with a Few High-Level Customers in Mind
    1. Give Your Data Stewards Room to Fail
    1. Start Scaling Past Your Super Users
    1. Your Next Step
6. **Monitor Data in Production**
    1. Make a Plan to Govern Data Throughout the Life Cycle
    1. Practice Data Mesh Principles
    1. Automate Federated Data Governance
    1. Execute Data Security Standards
    1. Set Specific Goals for Your Production Monitoring
    1. Use Data Lineage Tracking
    1. Use Feature Stores to Prevent Data Drift
    1. Ship New Data as Deployable Units
    1. Track Regulation Changes
    1. Your Next Step
