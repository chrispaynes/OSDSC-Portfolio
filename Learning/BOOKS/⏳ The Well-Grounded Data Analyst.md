# Chapter 2 - Encoding geographies
**Each project throughout your career will require you to**
- Ensure you understand the problem
- Think about the end goal you are working toward
- Consider whether you have the right data
- Identify the caveats you would need to flag when presenting your findings
- Document what further work is possible once you have arrived at a minimum viable answer

## Summary
- Using a results-driven approach helps focus on the specific problem you are solving.
- Part of the results-driven approach is to ensure you understand the problem before starting the analysis.
- Envisioning the end result at the start creates a goal to work toward.
- There are multiple possible approaches to extracting the city part of a free-type address, each with its pros and cons.
- Analyses will diverge depending on the choices and assumptions made; therefore, it is possible to get different, but still correct, results.
- Even seemingly smaller tasks, such as extracting city information from address data, benefit from a results-driven approach by helping focus on a valuable outcome.

# Chapter 3 - Data modeling
- Whenever these business rules need to be applied constantly to ensure data is accurate, it is a good opportunity to build a ==**data model**==.
	- A data model is a dataset created from raw data that has been cleaned, with specific business rules built into it.
	- Creating reusable data models will save you time and maintenance headaches in the future.
	- Data modeling also forces you to think deeply about your or your stakeholder’s question, which leads to a more valuable answer.

## 3.1 The importance of data modeling
Data modeling is a foundational step in the analytical workflow. It is the process of taking raw data, mapping it to business-specific entities, and creating new data models. We can think of it as converting data in its raw state to a more useful form, which we can call information. Data analysis is then the process of converting this information into insight.

Your data models should encode any business logic required to transform the raw data to be suitable for analysis. If you always need to remember to filter out certain rows from your raw data, you should have an intermediate data model where that filter has already been applied. What does a “lapsed customer” mean for your business? Is it someone who hasn’t purchased anything for a certain time? Or perhaps someone who hasn’t even logged in to your platform for a while? Whatever that definition, it should be encoded in a data model.

Creating data models increases transparency because there is a single place to look for how a customer, a vehicle, or a purchase event is defined. All other analyses should be done using these intermediate models, not the raw data. Another benefit is that this kind of cleaner data model could be exposed to data-savvy stakeholders to work with directly, thus enabling self-service.

### 3.1.1 Common data modeling tasks

Data modeling usually involves some combination of[](https://livebook.manning.com/book/the-well-grounded-data-analyst/chapter-3/13)

- Repetitive data cleaning tasks, such as fixing date formats or converting text columns into their numeric equivalents.
- Defining business entities, concepts, and activities.
- Deduplicating the source data.
- Restructuring the raw data to be in a format more useful to the analytical questions it is designed to answer. This might involve making a choice between wide or long data, which we will discuss later in this section.
- Zooming in or out, altering the level of granularity for different analytical questions.

It is important to ask questions to clarify the terminology because even everyday terms like “customer” might have ambiguous meanings. Does a customer mean a single person or an organization? What if your business deals with both? Part of the data modeling process is defining these terms so that they can be encoded in a data table. When it comes to definitions, you cannot work in a vacuum; decisions about what concepts mean concretely need to be made in collaboration with your stakeholders.

- Examples: Each of these examples applies **business logic to raw data**, ensuring it’s structured, usable, and insightful. Here are some common **data modeling** examples that incorporate business rules to ensure **data accuracy, consistency, and usability**:

	**1. Data Cleaning & Standardization**
	• **Deduplication** → Removing duplicate customer records in a CRM
	• **Entity resolution** → Matching different records that refer to the same entity (e.g., merging “J. Smith” and “John Smith” if they have the same email)
	• **Address normalization** → Standardizing addresses in a customer database (e.g., “123 Main St.” vs. “123 Main Street”)
	• **Phone/email validation** → Ensuring consistent formats (e.g., converting phone numbers to +1-XXX-XXX-XXXX)
	
	**2. Aggregation & Summarization**
	• **Customer lifetime value (CLV) modeling** → Calculating total revenue per customer over time
	• **Daily/monthly revenue metrics** → Summarizing transaction data into a structured model
	• **Churn prediction models** → Aggregating user engagement and subscription data to predict drop-offs
	
	**3. Business Rule Enforcement**
	• **Data governance rules** → Ensuring specific fields (e.g., SSN, DOB) are always populated
	• **Product hierarchy modeling** → Structuring categories like “Electronics > Laptops > Gaming Laptops”
	• **Compliance reporting** → Ensuring financial transaction data meets regulatory requirements
	
	**4. Time-Series & Historical Modeling**
	• **Slowly changing dimensions (SCD)** → Keeping track of historical changes in customer addresses or pricing models
	• **Event stream processing** → Structuring clickstream/log data for behavioral analysis
	
	**5. Relationship & Network Modeling**
	• **Customer segmentation models** → Grouping users based on purchase behavior
	• **Supply chain optimization** → Structuring vendor and inventory data for logistics
	• **Graph models for fraud detection** → Mapping transactions and relationships to spot anomalies
	
#### Wide vs. long data

In many cases, your data will consist of one row per entity, such as a customer. Each row represents a customer, and each column represents a property or attribute of that customer, such as their name, age, department, and so forth. This is called a _wide_ format because as the number of measurements grows, the data gains additional columns.[](https://livebook.manning.com/book/the-well-grounded-data-analyst/chapter-3/18)

In contrast, _long_ data is when one row represents a single measurement of an entity. This means an entity, such as a customer, will require multiple rows. When a new measurement about the entities is added, the data gains additional rows.	

Neither a wide nor a long format is better than the other; the choice between them depends on the question you are trying to answer using the data. Assessing what format is best suited to your analytical question is the essence of data modeling.

#### Identifying the right level of granularity
When beginning this project, start by asking, “What should the structure of the final data model be?” Working toward that goal (in a results-focused way!) will guide the concrete steps you will need to take.
