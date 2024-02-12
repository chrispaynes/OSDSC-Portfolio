# Tip 179 - Key Tenets of the Kimball Method

1. **The dimensional model is the key asset.**

If you get the model right, and populate it with integrity, the rest is straightforward.

2. **Dimensional modeling is a group activity.**

Even the best dimensional modeler will create a poor dimensional model if she works solo. Not only is dimensional modeling a group activity, it is a group activity that must involve the business user community.

It is undoubtedly a huge request of the user community. Our design process usually requires 50-60 hours of sessions over a 4 to 6 week period (or more, depending on project complexity). The people whom we want to participate in the design sessions are always valuable and in demand. But if they can’t be convinced to put in the time and energy, the resulting system will fail.

3. **The dimensional model is the best specification for the DW/BI system.**

The majority of clients that I work with don’t have a written specification for the DW/BI system, certainly no document that reflects reality in a meaningful way. The most common specification format includes mind-numbing lists of what users want to filter and drill on, as well as the demand that all 2000 of the existing reports be supported by the new system. If all we’ve accomplished with our new DW/BI system is re-platforming the existing canned reports, we have failed.

==We ask the business users at the end of the design process to think about the analyses they’ve recently done, tried to do, or would have liked to do, from the information in the current design scope. We want them to say “Yes, this model meets our needs.” At the same time, the IT people on the team have been watching the discussion of data sources, transformations, and other technical details. We ask them to affirm “Yes, we can populate this data model.” The dimensional model design write-up is a meaningful and actionable specification of the requirements.==

4. **The dimensional model should add value beyond restructuring.**

==Some of the most valuable improvements that you can deliver in your DW/BI system are to add improved descriptors and groups to frequently used data. Yet these opportunities are often missed by the design team. I’ve even encountered teams with an explicit policy to add nothing beyond what is in the source system.==

Examples of valuable data model additions include:
- Making it easy for users to filter out the seldom used transaction codes.
- Providing attractive sort columns for pick lists and reports.
- Precompute banding, such as age ranges or transaction quality measures.
- Supporting different or deeper hierarchies than are managed in the source systems, such as marketing versus manufacturing views of the product dimension.

5. **Master data management systems are a great source.**

De-duplication is one of the most difficult tasks facing a data warehouse team. Since the earliest days of data warehousing, the back room team has struggled to design ETL processes that de-duplicate entities such as customer. The increasing popularity and functionality of master data management (MDM) technology and programs provides a much better solution than within the ETL flow. And not just because it’s hard! The rhythm of the ETL process, which on an ongoing basis we want to be bullet proof and hands free, is fundamentally at odds with the de-duplication process. No matter how great our tools, how clever our code, how complete our business rules, the automated de-duplication process cannot achieve 100% accuracy. A person is required to make a judgment on the questionable cases. This works much better if it is a job responsibility during the business day, rather than waiting for the ETL load.

A simple MDM system can be used to build the value-added data elements discussed previously in this _Design Tip_. Dimension hierarchies are notorious for being imperfectly structured if sourced from users’ desktops; the MDM tools deliver a simple platform to manage this information.

6. **Don’t skip the relational data warehouse.**

Designing and populating an enterprise conformed data warehouse is hard. Everyone would like to skip this step. Throughout the 23+ years of my career in data warehousing, I have observed any number of technological attempts to simplify the process, from building the BI layer directly on the transaction system, to so-called virtual data warehouses, back full circle to the current flavor of visualization tool build scripts.

As I discussed in _[Design Tip #162 Leverage Data Visualization Tools, But Avoid Anarchy](http://www.kimballgroup.com/2014/01/design-tip-162-leverage-data-visualization-tools-but-avoid-anarchy/)_, just say no! ==Unless you completely control all of your source data, you should leave ETL to the ETL tool, leave data storage and management to a relational database engine, and let the BI tools shine at what they do best: great visualizations and user experience.==

7. **It’s all about the business.**

==I say this many times during classes and consulting. It’s the most important characteristic of the Kimball Lifecycle method: practical, uncompromising focus on the business.== It infuses everything we do, and it’s the single most important message to carry forward.


# Tip 178 - Tried and True Concepts for DW-BI Success
I would like to share the perspective for DW/BI success I’ve gained from my 26 years in the data warehouse/business intelligence industry.

My suggestion for ongoing success is to keep your eyes wide open and constantly focus on the basics – the fundamental blocking and tackling of data warehousing. Embrace these tried and true concepts that years of experience have revealed to be true:

- **_Focus on the business and business requirements_** – Never forget to maintain a laser-like focus on achieving business value. The success of a DW/BI effort is totally dependent on business user engagement; keeping the business users involved and meeting their requirements dramatically increases the probability of success. In fact, it ensures it.
- **_Obtain strong senior management sponsorship_** – Lack of organizational support undermines the success of a DW/BI effort. Senior management must accept, support, manage and fund these efforts as long-term programs.
- **_Organize for success_** – Successful DW/BI initiatives are undertaken as a partnership between the IT team and the business units. The DW/BI effort cannot be identified as just an IT effort. The business community (not IT) needs to take ownership of the vision, strategy, roadmap (priorities), scope, timelines, governance, and quality of the DW/BI environment.
- **_Integration is critical_** – Leverage conformed dimensions as the basis for integration. Understand and embrace the discipline of dimensional design as the organizing theme for the data within the DW/BI environment.
- **_Establish and enforce common vocabulary_** – The first step to eliminating data inconsistency issues is to establish and enforce common names, definitions and descriptors across the DW/BI environment. Again, embracing the discipline of dimensional modeling is the secret to victory.
- **_Focus on data quality_** – ==At its foundation, the DW/BI environment must be a repository of high quality data.== The biggest challenges for most DW/BI efforts are data-related. In general, the effort to develop the ETL processes required to provide high quality data is typically more demanding than anticipated. Adequate time and resources, including key subject area experts, must be allocated to these tasks.
- **_Establish a phased design, development and deployment plan_** – Constructing a DW/BI environment is a significant effort. It is nearly impossible to tackle everything at once. Embrace an iterative development plan that avoids an overly ambitious scope. Project iterations need to be identified to phase-in the overall design, development and deployment effort. The environment should grow by tackling new and additional business processes (i.e., fact tables).
- **_Exhibit patience_** – The initial phase of a DW/BI initiative usually takes a disproportionately long time; I call this the “big gulp.” This is necessarily true. ==While the initial phase corresponds to deploying a single business process, the bulk of the time in this phase is committed to designing, developing and deploying the critical, core set of conformed dimensions that will be leveraged throughout the DW/BI environment in later phases. This is normal and to be expected.==
- 
# Tip 174 - Does Your Organization Need an Analytic Sandbox?
Nonetheless, regardless of the success achieved by these dimensional data warehouses, they are sometimes criticized as being too slow to react to new requirements, implement new data sources, and support new analytic capabilities. Sometimes these concerns are overstated as it clearly takes a certain amount of time to react to any new requirements, but sometimes these criticisms are true. Many data warehouses have grown and evolved to become mission-critical environments supporting key enterprise reporting, dashboards/scorecards, and self-serve data access capabilities. Due to the mission-critical nature, the data modeling, governance, ETL rules development, and change management requirements result in lengthy approval, design and development cycles for new requirements and changes. In many ways, these challenges are the price of success.

The data warehouse is likely to be very structured, heavily designed, subject to well-defined business rules, and tightly governed by the enterprise. Much of the data warehouse data is extensively cleansed and transformed to ensure it represents the true picture of what actually happened in the business. In addition, data warehouse data is frequently synchronized with the production environments via regularly scheduled loads. Thus, in the end, it is fairly rigid; it simply takes time to react to new data and analytic requests.

==Yet, in today’s competitive world, organizations need to be more nimble. They want to quickly test new ideas, new hypotheses, new data sources, and new technologies. The creation of an analytic sandbox may be an appropriate response to these requirements. An analytic sandbox complements your dimensional data warehouse. It is not intended to replace the data warehouse, but rather stand beside it and provide an environment that can react more quickly to new requirements.==

The analytic sandbox is not really a new concept, but the recent big data discussions have brought the concept back to the forefront. Typically an analytic sandbox is thought of as an area carved out of the existing data warehouse infrastructure or as a separate environment living adjacent to the data warehouse. It provides the environment and resources required to support experimental or developmental analytic capabilities. It’s a place where these new ideas, hypotheses, data sources, and tools can be utilized, tested, evaluated, and explored. Meanwhile, the data warehouse stands as the prerequisite data foundation containing the historically-accurate enterprise data that the analytic sandbox efforts spin around and against.

==Sometimes key data is fed from the existing data warehouse environment into the analytic sandbox and aligned with other non-data warehouse data stores. It is a place where new data sources can be tested to determine their value to the enterprise. Examples of these new data sources might be externally-acquired market intelligence, externally-acquired customer attributes, or sources such as social media interactions, mobile app interactions, mobile dust, and website activity. Often it may be too onerous to bring these new data sources into the existing data warehouse environment unless or until their value has been proven. Data in the analytic sandbox typically does not need to be synchronized on a recurring basis with production environment and these data sets expire after the passage of time.==

==A key objective of the analytic sandbox is to test a variety of hypotheses about data and analytics. Thus, it shouldn’t be a huge surprise that most analytic sandbox projects result in “failure.” That is, the hypothesis doesn’t pan out as expected. This is one of the big advantages of the analytic sandbox. The data utilized in these “failures” didn’t and won’t need to be run through the rigor expected of data contained in the data warehouse. In this case, failure is its own success; each failure is a step towards finding the right answer.==

Most business users will rightfully view the data warehouse as the go-to source for enterprise data. Their reporting, dashboards/scorecards and “self-serve” ad hoc requests will be readily supported by the data warehouse. The target users of the analytic sandbox are often called “data scientists.” These individuals are the small cadre of business users technologically savvy enough to identify potential sources of data, create their own “shadow” databases, and build special purpose analyses. Often these individuals have to work “off the grid.” They have crafted and created their own shadow analytic environments in spreadsheets, local data sets, under the desk data marts, or whatever it takes to get the job done. ==The analytic sandbox recognizes that these individuals have real requirements. It provides an environment for them to work “on the grid” in an environment that is blessed, supported, funded, available, performant and, to some light extent, governed.==

==Having the right skills in house is critical to the success of the analytic sandbox. The users of the analytic sandbox need to be able to engage with the data with far fewer rules of engagement than most business users. They are users capable of self-provisioning their required data whether it comes from the data warehouse or not. They are capable of building the analytics and models directly against this data without assistance.==

==The analytic sandbox should be minimally governed. The idea is to create an environment that lives without all the overhead of the data warehouse environment. It should not be used to support the organization’s mission critical capabilities. It shouldn’t be used to directly control or support any core operational capabilities. Likewise, it is not intended to be utilized for ongoing reporting or analytics required by the business on an ongoing basis, especially any reporting that supports external reporting to meet financial or government regulations.==

==An important characteristic of the analytic sandbox is that it is transient in nature. Data and analysis come and go as needed to support new analytic requirements. The data does not persist and it is not regularly updated via ongoing ETL capabilities. Data in the analytic sandbox typically has an agreed upon expiration date. Thus, any new findings or capabilities identified as important to the organization and critical for supporting ongoing capabilities will need to be incorporated into the enterprise operation or data warehouse environments.==

# Tip 168 - What’s in a Name?
==Good names for tables and columns are particularly important for ad hoc users of the DW/BI system who need to find the objects they’re looking for. Object names should be oriented to the business users, not the technical staff.==

As much as possible, strive to have the names in the DW/BI system be unchanged in the semantic layer and unchanged by report designers. More challenging, your users should be discouraged from changing object names once they’ve pulled the information to their desktop. We usually can’t prevent them from doing that, but attractive and sensible names will reduce the temptation.

Here are my top ten suggestions for naming objects in your data warehouse / business intelligence system.

1. Follow naming conventions.
If you don’t have them, create (and document!) naming conventions that follow the rules in this Design Tip. If your organization already has naming conventions, you may be faced with a problem: most existing naming conventions were developed for technical people. But names in the DW/BI environment should be oriented to the business users. They become row and column names in ad hoc analyses and predefined reports. We will return to this issue later.

2. Each object has one name.
Let’s not perpetuate the confusion around data definitions that already exists in our organizations. It is not OK to say that the sales team can call a column Geography and the marketing group calls the same entity Region. If it’s the same column, with the same content, it has to have the same name. If you can’t get agreement organization-wide on object names, enlist the help of your business sponsor.

3. Object names are descriptive.
Users should not need 20 years tenure at your organization to decipher what a name means. This rule forbids a lot of silliness, like RBVLSPCD (we have more than 8 characters to work with!). It also forbids column names like NAME, which is non-descriptive outside the context of the table you are examining.

4. Abbreviations and acronyms are discouraged.
Abbreviations and acronyms are endemic in the corporate world, and the non-corporate world is even worse. A lot of information can be encoded in an acronym, but it places a huge burden on newcomers. The most effective approach is to maintain a list of approved abbreviations, and try not to add to them without a good reason. You may even want to document that reason in the list. Examples include:
 Abbreviation 	 Replaces 	 Reason
 Amt 	 Amount 	 Extremely common
 Desc 	 Description 	 Extremely common
 Corp 	 Corporation 	 Common
 FDIC 	 Federal Deposit Insurance Corporation 	 Common; familiar to all users

For most organizations, a reasonable list has dozens of approved abbreviations, not hundreds.

5. Object names are pretty.
Remember that object names become headers in reports and analyses. Although beauty is in the eye of the beholder, I find all caps to be particularly annoying. The object names should contain a visual clue for where the words end.

    Spaces: [Column Name]
    Camel case: ColumnName
    Underscore: Column_Name or COLUMN_NAME

I recommend using spaces. They look the best when displayed in reports. And I scoff at the argument that developers have to type square brackets when they type the column name. I am confident that any developer who actually types SQL can figure out where the brackets keys are located, and they can develop the requisite finger muscles.

6. Object names are unique.
This rule is a corollary to the rule that each object has one name. If two objects are different, they should have different names. This rule forbids column names such as [City]. A better name is [Customer Mailing Address City]. This rule is especially important for ad hoc use of the DW/BI system. Although the context of [City] may be obvious during the analytic process, once that analysis is saved and shared, that context is lost. Are we looking at the customer’s city or the store’s city, the mailing address or the shipping address? Although we can’t prevent users from changing object names once they export to Excel, we don’t want to force them to do so in order to be clear.

7. Object names are not too long.
This rule conflicts with rules 3, 4, and 6. If we have unique, unabbreviated, descriptive object names, the odds are that some column names will be very long. Consider [Mandatory Second Payer Letter Opt Out Code] or [Vocational Provider Referral Category]. These are reasonably descriptive column names for someone in the insurance business, but what will happen when the user or report designer drags that column into the body of a report or analysis? The name will wrap unattractively, making the header row very fat. Or it will shrink down to a font so tiny that no one can read it. And then the user will rename the column, violating our key rule that each object has one name.

I try to limit column names to 30 characters, though sometimes I go to 35. In order to achieve this goal, I have to register more abbreviations or acronyms than I would like.

8. Consider prepending column names with an abbreviated table name.
I hate to make this recommendation, because it violates several of my previous rules about abbreviations and short names. But I am finding myself following this practice with increasing frequency in order to guarantee consistency and uniqueness.

9. Change names in the view layer if needed.
We have always recommended a set of views in the DW/BI system which sit atop the physical tables and to which all queries are directed. The primary purpose of the view layer is to provide a layer of insulation between the BI applications and the physical database, providing a bit of flexibility to smoothly migrate change to a system already in production. Additionally, the view layer can also provide a place to put the business-oriented names into the database.

Our first recommendation is always to name the physical tables and columns with business-oriented names. Failing that, use the view layer. We dislike changing the names in the BI tools for several reasons:

    Most organizations have several BI tools; the names should be consistent across all BI tools.
    The more business logic you put into the BI tool, the more challenging it will be to migrate to a different tool.
    If the names are only in the BI tool, there is a barrier to communication between users, front room support team, and back room database people.

10. Be consistent!
It’s only a foolish consistency that’s the hobgoblin of little minds. Consistency in naming is hugely valuable to your users.
