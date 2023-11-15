## Preface

## 1. Introduction: Data-Analytic Thinking

> There is a fundamental structure to data-analytic thinking, and basic principles that should be understood. There are also particular areas where intuition, creativity, common sense, and domain knowledge must be brought to bear.

> At a high level, data science is a set of fundamental principles that guide the extraction of knowledge from data. Data mining is the extraction of knowledge from data, via technologies that incorporate these principles.

> you should be able to assess the proposal systematically and decide whether it is sound or flawed. This does not mean that you will be able to tell whether it will actually succeed — for data mining projects, that often requires trying — but you should be able to spot obvious flaws, unrealistic assumptions, and missing pieces.

> It would be more valuable to discover patterns due to the hurricane that were not obvious.
### The Ubiquity of Data Opportunities

### Example: Hurricane Frances

### Example: Predicting Customer Churn

### Data Science, Engineering, and Data-Driven Decision Making
> view the ultimate goal of data science as improving decision making, as this generally is of direct interest to business.

> ==Data-driven decision-making (DDD) refers to the practice of basing decisions on the analysis of data, rather than purely on intuition.== For example, a marketer could select advertisements based purely on her long experience in the field and her eye for what will work. Or, she could base her selection on the analysis of data regarding how consumers react to different ads.

> The benefits of data-driven decision-making have been demonstrated conclusively. Economist Erik Brynjolfsson and his colleagues from MIT and Penn’s Wharton School conducted a study of how DDD affects firm performance (Brynjolfsson, Hitt, & Kim, 2011). They developed a measure of DDD that rates firms as to how strongly they use data to make decisions across the company. They show that statistically, the more data-driven a firm is, the more productive it is — even controlling for a wide range of possible confounding factors. And the differences are not small. One standard deviation higher on the DDD scale is associated with a 4%–6% increase in productivity. DDD also is correlated with higher return on assets, return on equity, asset utilization, and market value, and the relationship seems to be causal.

> Importantly, in both the Walmart and the Target examples, the data analysis was not testing a simple hypothesis. Instead, the data were explored with the hope that something useful would be discovered.[

### Data Processing and “Big Data”
> A separate study, conducted by economist Prasanna Tambe of NYU’s Stern School, examined the extent to which big data technologies seem to help firms (Tambe, 2012). He finds that, after controlling for various possible confounding factors, using big data technologies is associated with significant additional productivity growth. Specifically, one standard deviation higher utilization of big data technologies is associated with 1%–3% higher productivity than the average firm; one standard deviation lower in terms of big data utilization is associated with 1%–3% lower productivity.

### From Big Data 1.0 to Big Data 2.0

### Data and Data Science Capability as a Strategic Asset
> Often, we don’t have exactly the right data to best make decisions and/or the right talent to best support making decisions from the data. ... The best data science team can yield little value without the appropriate data; the right data often cannot substantially improve decisions without suitable data science talent. As with all assets, it is often necessary to make investments. Building a top-notch data science team is a nontrivial undertaking, but can make a huge difference for decision-making.

> They knew that a small proportion of customers actually account for more than 100% of a bank’s profit from credit card operations (because the rest are break-even or money-losing). If they could model profitability, they could make better offers to the best customers and “skim the cream” of the big banks’ clientele.

> Once we view data as a business asset, we should think about whether and how much we are willing to invest. In Signet’s case, data could be generated on the profitability of customers given different credit terms by conducting experiments. Different terms were offered at random to different customers. This may seem foolish outside the context of data-analytic thinking: you’re likely to lose money! This is true. In this case, losses are the cost of data acquisition. The data-analytic thinker needs to consider whether she expects the data to have sufficient value to justify the investment.
> Once we view data as a business asset, we should think about whether and how much we are willing to invest. In Signet’s case, data could be generated on the profitability of customers given different credit terms by conducting experiments. Different terms were offered at random to different customers. This may seem foolish outside the context of data-analytic thinking: you’re likely to lose money! This is true. In this case, losses are the cost of data acquisition. The data-analytic thinker needs to consider whether she expects the data to have sufficient value to justify the investment.

> When a customer calls looking for a better offer, data-driven models calculate the potential profitability of various possible actions (different offers, including sticking with the status quo), and the customer service representative’s computer presents the best offers to make.

> In 2000, the bank was reported to be carrying out 45,000 of these “scientific tests” as they called them.

> Sociodemographic data provide a substantial ability to model the sort of consumers that are more likely to purchase one product or another. However, sociodemographic data only go so far; after a certain volume of data, no additional advantage is conferred. In contrast, detailed data on customers’ individual (anonymized) transactions improve performance substantially over just using sociodemographic data. The relationship is clear and striking and — significantly, for the point here — the predictive performance continues to improve as more data are used, increasing throughout the range investigated by Martens and Provost with no sign of abating. This has an important implication: banks with bigger data assets may have an important strategic advantage over their smaller competitors. If these trends generalize, and the banks are able to apply sophisticated analytics, banks with bigger data assets should be better able to identify the best customers for individual products. The net result will be either increased adoption of the bank’s products, decreased cost of customer acquisition, or both.


### Data-Analytic Thinking
> ==When faced with a business problem, you should be able to assess whether and how data can improve performance.==

> “Digital 100” companies (Business Insider, 2012), have high valuations due primarily to data assets they are committed to capturing or creating.[5] Increasingly, managers need to oversee analytics teams and analysis projects, marketers have to organize and understand data-driven campaigns, venture capitalists must be able to invest wisely in businesses with substantial data assets, and business strategists must be able to devise plans that exploit data.

> ==If a competitor announces a new data partnership, you should recognize when it may put you at a strategic disadvantage.== Or, let’s say you take a position with a venture firm and your first project is to assess the potential for investing in an advertising company. The founders present a convincing argument that they will realize significant value from a unique body of data they will collect, and on that basis are arguing for a substantially higher valuation.

> On a scale less grand, but probably more common, data analytics projects reach into all business units. Employees throughout these units must interact with the data science team. If these employees do not have a fundamental grounding in the principles of data-analytic thinking, they will not really understand what is happening in the business. This lack of understanding is much more damaging in data science projects than in other technical projects, because the data science is supporting improved decision-making.

### This Book

### Data Mining and Data Science, Revisited
> Extracting useful knowledge from data to solve business problems can be treated systematically by following a process with reasonably well-defined stages. The Cross Industry Standard Process for Data Mining, abbreviated CRISP-DM (CRISP-DM Project, 2000), is one codification of this process.

> Fundamental concept: Formulating data mining solutions and evaluating the results involves thinking carefully about the context in which they will be used. If our goal is the extraction of potentially useful knowledge, how can we formulate what is useful? It depends critically on the application in question. For our churn-management example, how exactly are we going to use the patterns extracted from historical data? Should the value of the customer be taken into account in addition to the likelihood of leaving? More generally, does the pattern lead to better decisions than some reasonable alternative? How well would one have done by chance? How well would one do with a smart “default” alternative?

### Chemistry Is Not About Test Tubes: Data Science Versus the Work of the Data Scientist

### Summary

--- 
## 2. Business Problems and Data Science Solutions

> Understanding the whole process helps to structure data mining projects, so they are closer to systematic analyses rather than heroic endeavors driven by chance and individual acumen.

Provost, Foster; Fawcett, Tom. Data Science for Business (p. 46). O'Reilly Media. Kindle Edition. 
### From Business Problems to Data Mining Tasks

> A critical skill in data science is the ability to decompose a data-analytics problem into pieces such that each piece matches a known task for which tools are available. Recognizing familiar problems and their solutions avoids wasting time and resources reinventing the wheel. It also allows people to focus attention on more interesting parts of the process that require human involvement — parts that have not been automated, so human creativity and intelligence must come into play.

> ==Classification== and class probability estimation attempt to predict, for each individual in a population, which of a (small) set of classes this individual belongs to.

> ==Regression== (“value estimation”) attempts to estimate or predict, for each individual, the numerical value of some variable for that individual. An

> ==Similarity== matching attempts to identify similar individuals based on data known about them.

> ==Clustering== attempts to group individuals in a population together by their similarity, but not driven by any specific purpose. An example clustering question would be: “Do our customers form natural groups or segments?” Clustering is useful in preliminary domain exploration to see which natural groups exist because these groups in turn may suggest other data mining tasks or approaches. Clustering also is used as input to decision-making processes focusing on questions such as: What products should we offer or develop? How should our customer care teams (or sales teams) be structured?

> ==Co-occurrence grouping== (also known as frequent itemset mining, association rule discovery, and market-basket analysis) attempts to find associations between entities based on transactions involving them.

> ==Profiling== (also known as behavior description) attempts to characterize the typical behavior of an individual, group, or population. An example profiling question would be: “What is the typical cell phone usage of this customer segment?” Behavior may not have a simple description; profiling cell phone usage might require a complex description of night and weekend airtime averages, international usage, roaming charges, text minutes, and so on. Behavior can be described generally over an entire population, or down to the level of small groups or even individuals. 
> Profiling is often used to establish behavioral norms for anomaly detection applications such as fraud detection and monitoring for intrusions to computer systems (such as someone breaking into your iTunes account). For example, if we know what kind of purchases a person typically makes on a credit card, we can determine whether a new charge on the card fits that profile or not. We can use the degree of mismatch as a suspicion score and issue an alarm if it is too high.

> ==Link prediction== attempts to predict connections between data items, usually by suggesting that a link should exist, and possibly also estimating the strength of the link. Link prediction is common in social networking systems: “Since you and Karen share 10 friends, maybe you’d like to be Karen’s friend?” Link prediction can also estimate the strength of a link.

> ==Data reduction== attempts to take a large set of data and replace it with a smaller set of data that contains much of the important information in the larger set. The smaller dataset may be easier to deal with or to process.


> ==Causal modeling== attempts to help us understand what events or actions actually influence others. For example, consider that we use predictive modeling to target advertisements to consumers, and we observe that indeed the targeted consumers purchase at a higher rate subsequent to having been targeted. Was this because the advertisements influenced the consumers to purchase? Or did the predictive models simply do a good job of identifying those consumers who would have purchased anyway? Techniques
### Supervised Versus Unsupervised Methods

> The terms supervised and unsupervised were inherited from the field of machine learning. Metaphorically, a teacher “supervises” the learner by carefully providing target information along with a set of examples. An unsupervised learning task might involve the same set of examples but would not include the target information. The learner would be given no information about the purpose of the learning, but would be left to form its own conclusions about what the examples have in common.

### Data Mining and Its Results

### The Data Mining Process

![[Pasted image 20231107085910.png]]

#### Business Understanding
> Often recasting the problem and designing a solution is an iterative process of discovery. The initial formulation may not be complete or optimal so multiple iterations may be necessary for an acceptable solution formulation to appear.
> 
> The Business Understanding stage represents a part of the craft where the analysts’ creativity plays a large role. Data science has some things to say, as we will describe, but often the key to a great success is a creative problem formulation by some analyst regarding how to cast the business problem as one or more data science problems. High-level knowledge of the fundamentals helps creative business analysts see novel formulations. 
> 
> This can mean structuring (engineering) the problem such that one or more subproblems involve building models for classification, regression, probability estimation, and so on.
> 
> In this first stage, the design team should think carefully about the problem to be solved and about the use scenario.  What exactly do we want to do? How exactly would we do it? What parts of this use scenario constitute possible data mining models? 
> 
> for example framing a business problem in terms of expected value can allow us to systematically decompose it into data mining tasks.

Provost, Foster; Fawcett, Tom. Data Science for Business (pp. 60-61). O'Reilly Media. Kindle Edition. 

#### Data Understanding
> It is important to understand the strengths and limitations of the data because rarely is there an exact match with the problem. Historical data often are collected for purposes unrelated to the current business problem, or for no explicit purpose at all. A customer database, a transaction database, and a marketing response database contain different information, may cover different intersecting populations, and may have varying degrees of reliability.
> 
> It is also common for the costs of data to vary. Some data will be available virtually for free while others will require effort to obtain. Some data may be purchased. Still other data simply won’t exist and will require entire ancillary projects to arrange their collection. A critical part of the data understanding phase is estimating the costs and benefits of each data source and deciding whether further investment is merited. Even after all datasets are acquired, collating them may require additional effort.

> The fact that both of these are fraud detection problems is a superficial similarity that is actually misleading. In data understanding we need to dig beneath the surface to uncover the structure of the business problem and the data that are available, and then match them to one or more data mining tasks for which we may have substantial science and technology to apply. It is not unusual for a business problem to contain several data mining tasks, often of different types, and combining their solutions will be necessary

Provost, Foster; Fawcett, Tom. Data Science for Business (p. 63). O'Reilly Media. Kindle Edition. 

Provost, Foster; Fawcett, Tom. Data Science for Business (p. 61). O'Reilly Media. Kindle Edition. 

#### Data Preparation
> The analytic technologies that we can bring to bear are powerful but they impose certain requirements on the data they use. They often require data to be in a form different from how the data are provided naturally, and some conversion will be necessary. Therefore a data preparation phase often proceeds along with data understanding, in which the data are manipulated and converted into forms that yield better results.
> Typical examples of data preparation are converting data to tabular format, removing or inferring missing values, and converting data to different types. Some data mining techniques are designed for symbolic and categorical data, while others handle only numeric values. In addition, numerical values must often be normalized or scaled so that they are comparable. Standard techniques and rules of thumb are available for doing such conversions. 
> More generally, data scientists may spend considerable time early in the process defining the variables used later in the process. This is one of the main points at which human creativity, common sense, and business knowledge come into play. Often the quality of the data mining solution rests on how well the analysts structure the problems and craft the variables (and sometimes it can be surprisingly hard for them to admit it).
> One very general and important concern during data preparation is to beware of “leaks” (Kaufman et al. 2012). A leak is a situation where a variable collected in historical data gives information on the target variable — information that appears in historical data but is not actually available when the decision has to be made. As an example, when predicting whether at a particular point in time a website visitor would end her session or continue surfing to another page, the variable “total number of webpages visited in the session” is predictive. However, the total number of webpages visited in the session would not be known until after the session was over (Kohavi et al., 2000) — at which point one would know the value for the target variable! As another illustrative example, consider predicting whether a customer will be a “big spender”; knowing the categories of the items purchased (or worse, the amount of tax paid) are very predictive, but are not known at decision-making time (Kohavi & Parekh, 2003). Leakage must be considered carefully during data preparation, because data preparation typically is performed after the fact — from historical data.

Provost, Foster; Fawcett, Tom. Data Science for Business (pp. 63-64). O'Reilly Media. Kindle Edition. 


#### Modeling

#### Evaluation

> The purpose of the evaluation stage is to assess the data mining results rigorously and to gain confidence that they are valid and reliable before moving on. If we look hard enough at any dataset we will find patterns, but they may not survive careful scrutiny. We would like to have confidence that the models and patterns extracted from the data are true regularities and not just idiosyncrasies or sample anomalies. It is possible to deploy results immediately after data mining but this is inadvisable; it is usually far easier, cheaper, quicker, and safer to test a model first in a controlled laboratory setting.
> Equally important, the evaluation stage also serves to help ensure that the model satisfies the original business goals. Recall that the primary goal of data science for business is to support decision making, and that we started the process by focusing on the business problem we would like to solve. Usually a data mining solution is only a piece of the larger solution, and it needs to be evaluated as such. Further, even if a model passes strict evaluation tests in “in the lab,” there may be external considerations that make it impractical. For example, a common flaw with detection solutions (such as fraud detection, spam detection, and intrusion monitoring) is that they produce too many false alarms. A model may be extremely accurate (> 99%) by laboratory standards, but evaluation in the actual business context may reveal that it still produces too many false alarms to be economically feasible. (How much would it cost to provide the staff to deal with all those false alarms? What would be the cost in customer dissatisfaction?)
> Evaluating the results of data mining includes both quantitative and qualitative assessments. Various stakeholders have interests in the business decision-making that will be accomplished or supported by the resultant models. In many cases, these stakeholders need to “sign off” on the deployment of the models, and in order to do so need to be satisfied by the quality of the model’s decisions. What that means varies from application to application, but often stakeholders are looking to see whether the model is going to do more good than harm, and especially that the model is unlikely to make catastrophic mistakes.[8] To facilitate such qualitative assessment, the data scientist must think about the comprehensibility of the model to stakeholders (not just to the data scientists). And if the model itself is not comprehensible (e.g., maybe the model is a very complex mathematical formula), how can the data scientists work to make the behavior of the model be comprehensible.
> Finally, a comprehensive evaluation framework is important because getting detailed information on the performance of a deployed model may be difficult or impossible. Often there is only limited access to the deployment environment so making a comprehensive evaluation “in production” is difficult. Deployed systems typically contain many “moving parts,” and assessing the contribution of a single part is difficult. Firms with sophisticated data science teams wisely build testbed environments that mirror production data as closely as possible, in order to get the most realistic evaluations before taking the risk of deployment.
> Nonetheless, in some cases we may want to extend evaluation into the development environment, for example by instrumenting a live system to be able to conduct randomized experiments. In our churn example, if we have decided from laboratory tests that a data mined model will give us better churn reduction, we may want to move on to an “in vivo” evaluation, in which a live system randomly applies the model to some customers while keeping other customers as a control group (recall our discussion of causal modeling from Chapter 1). Such experiments must be designed carefully, and the technical details are beyond the scope of this book. The interested reader could start with the lessons-learned articles by Ron Kohavi and his coauthors (Kohavi et al., 2007, 2009, 2012). We may also want to instrument deployed systems for evaluations to make sure that the world is not changing to the detriment of the model’s decision-making. For example, behavior can change — in some cases, like fraud or spam, in direct response to the deployment of models. Additionally, the output of the model is critically dependent on the input data; input data can change in format and in substance, often without any alerting of the data science team. Raeder et al. (2012) present a detailed discussion of system design to help deal with these and other related evaluation-in-deployment issues.

Provost, Foster; Fawcett, Tom. Data Science for Business (pp. 65-67). O'Reilly Media. Kindle Edition. 

#### Deployment

### Implications for Managing the Data Science Team

### Other Analytics Techniques and Technologies

#### Statistics

#### Database Querying

#### Data Warehousing

#### Regression Analysis

#### Machine Learning and Data Mining

#### Answering Business Questions with These Techniques

### Summary

--- 
## 3. Introduction to Predictive Modeling: From Correlation to Supervised Segmentation

### Models, Induction, and Prediction

### Supervised Segmentation

#### Selecting Informative Attributes

#### Example: Attribute Selection with Information Gain

#### Supervised Segmentation with Tree-Structured Models

### Visualizing Segmentations

### Trees as Sets of Rules

### Probability Estimation

### Example: Addressing the Churn Problem with Tree Induction

### Summary


--- 
## 4. Fitting a Model to Data

### Classification via Mathematical Functions

#### Linear Discriminant Functions

#### Optimizing an Objective Function

#### An Example of Mining a Linear Discriminant from Data

#### Linear Discriminant Functions for Scoring and Ranking Instances

#### Support Vector Machines, Briefly

### Regression via Mathematical Functions

### Class Probability Estimation and Logistic “Regression”

#### * Logistic Regression: Some Technical Details

### Example: Logistic Regression versus Tree Induction

### Nonlinear Functions, Support Vector Machines, and Neural Networks

### Summary


--- 

## 5. Overfitting and Its Avoidance

### Generalization

### Overfitting

### Overfitting Examined

#### Holdout Data and Fitting Graphs

#### Overfitting in Tree Induction

#### Overfitting in Mathematical Functions

### Example: Overfitting Linear Functions

### * Example: Why Is Overfitting Bad?

### From Holdout Evaluation to Cross-Validation

### The Churn Dataset Revisited

### Learning Curves

### Overfitting Avoidance and Complexity Control

#### Avoiding Overfitting with Tree Induction

#### A General Method for Avoiding Overfitting

#### * Avoiding Overfitting for Parameter Optimization

### Summary


--- 
## 6. Similarity, Neighbors, and Clusters

### Similarity and Distance

### Nearest-Neighbor Reasoning

#### Example: Whiskey Analytics

#### Nearest Neighbors for Predictive Modeling

#### Classification

#### Probability Estimation

#### Regression

#### How Many Neighbors and How Much Influence?

#### Geometric Interpretation, Overfitting, and Complexity Control

#### Issues with Nearest-Neighbor Methods

#### Intelligibility

#### Dimensionality and domain knowledge

#### Computational efficiency

### Some Important Technical Details Relating to Similarities and Neighbors

#### Heterogeneous Attributes

#### * Other Distance Functions

#### * Combining Functions: Calculating Scores from Neighbors

### Clustering

#### Example: Whiskey Analytics Revisited

#### Hierarchical Clustering

#### Nearest Neighbors Revisited: Clustering Around Centroids

#### Example: Clustering Business News Stories

#### Data preparation

#### The news story clusters

#### Understanding the Results of Clustering

#### * Using Supervised Learning to Generate Cluster Descriptions

### Stepping Back: Solving a Business Problem Versus Data Exploration

### Summary


--- 
## 7. Decision Analytic Thinking I: What Is a Good Model?

### Evaluating Classifiers

#### Plain Accuracy and Its Problems

#### The Confusion Matrix

#### Problems with Unbalanced Classes

#### Problems with Unequal Costs and Benefits

### Generalizing Beyond Classification

### A Key Analytical Framework: Expected Value

#### Using Expected Value to Frame Classifier Use

#### Using Expected Value to Frame Classifier Evaluation

#### Error rates

#### Costs and benefits

### Evaluation, Baseline Performance, and Implications for Investments in Data

### Summary


--- 
## 8. Visualizing Model Performance

### Ranking Instead of Classifying

### Profit Curves

### ROC Graphs and Curves

### The Area Under the ROC Curve (AUC)

### Cumulative Response and Lift Curves

### Example: Performance Analytics for Churn Modeling

### Summary

--- 

## 9. Evidence and Probabilities

### Example: Targeting Online Consumers With Advertisements

### Combining Evidence Probabilistically

#### Joint Probability and Independence

#### Bayes’ Rule

### Applying Bayes’ Rule to Data Science

#### Conditional Independence and Naive Bayes

#### Advantages and Disadvantages of Naive Bayes

### A Model of Evidence “Lift”

### Example: Evidence Lifts from Facebook “Likes”

#### Evidence in Action: Targeting Consumers with Ads

### Summary


--- 
## 10. Representing and Mining Text

### Why Text Is Important

### Why Text Is Difficult

### Representation

#### Bag of Words

#### Term Frequency

#### Measuring Sparseness: Inverse Document Frequency

#### Combining Them: TFIDF

### Example: Jazz Musicians

### * The Relationship of IDF to Entropy

### Beyond Bag of Words

#### N-gram Sequences

#### Named Entity Extraction

#### Topic Models

### Example: Mining News Stories to Predict Stock Price Movement

#### The Task

#### The Data

#### Data Preprocessing

#### Results

### Summary


--- 
## 11. Decision Analytic Thinking II: Toward Analytical Engineering

### Targeting the Best Prospects for a Charity Mailing

#### The Expected Value Framework: Decomposing the Business Problem and Recomposing the Solution Pieces

#### A Brief Digression on Selection Bias

### Our Churn Example Revisited with Even More Sophistication

#### The Expected Value Framework: Structuring a More Complicated Business Problem

#### Assessing the Influence of the Incentive

#### From an Expected Value Decomposition to a Data Science Solution

#### Summary


--- 
## 12. Other Data Science Tasks and Techniques

### Co-occurrences and Associations: Finding Items That Go Together

#### Measuring Surprise: Lift and Leverage

#### Example: Beer and Lottery Tickets

#### Associations Among Facebook Likes

### Profiling: Finding Typical Behavior

### Link Prediction and Social Recommendation

### Data Reduction, Latent Information, and Movie Recommendation

### Bias, Variance, and Ensemble Methods

### Data-Driven Causal Explanation and a Viral Marketing Example

### Summary


--- 
## 13. Data Science and Business Strategy

### Thinking Data-Analytically, Redux

### Achieving Competitive Advantage with Data Science

### Sustaining Competitive Advantage with Data Science

#### Formidable Historical Advantage

#### Unique Intellectual Property

#### Unique Intangible Collateral Assets

#### Superior Data Scientists

#### Superior Data Science Management

### Attracting and Nurturing Data Scientists and Their Teams

### Examine Data Science Case Studies

### Be Ready to Accept Creative Ideas from Any Source

### Be Ready to Evaluate Proposals for Data Science Projects

#### Example Data Mining Proposal

#### Flaws in the Big Red Proposal

### A Firm’s Data Science Maturity


--- 
## 14. Conclusion

### The Fundamental Concepts of Data Science

#### Applying Our Fundamental Concepts to a New Problem: Mining Mobile Device Data

#### Changing the Way We Think about Solutions to Business Problems

### What Data Can’t Do: Humans in the Loop, Revisited

### Privacy, Ethics, and Mining Data About Individuals

### Is There More to Data Science?

### Final Example: From Crowd-Sourcing to Cloud-Sourcing

### Final Words


--- 

## A. Proposal Review Guide

### Business and Data Understanding

### Data Preparation

### Modeling

### Evaluation and Deployment


--- 

## B. Another Sample Proposal

### Scenario and Proposal

#### Flaws in the GGC Proposal


--- 

## Glossary