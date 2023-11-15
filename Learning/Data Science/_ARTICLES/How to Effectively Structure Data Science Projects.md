https://towardsdatascience.com/how-to-effectively-structure-data-science-projects-85f717e65c75

# Introduction

I used to work with plenty of Data Science projects to help customers deal with various regression and classification tasks: look-alike models and recommender systems, NLP problems, predictive analytics just to name a few.

==Very often, clients are busy with their job routine, so they can’t afford to schedule meetings for long hours to describe in detail what they want to see in the project. Thus, it is so important to have a detailed and well-structured agenda.==

==On the call with experts, I often apply the **PSW (or Problem Statement Worksheet) approach** to fully understand the customer’s needs.==

> ==**The PSW is a business task description template that is used mainly in consulting, but also perfectly suits for almost any IT-project.**==

In this post, I will show you how to use the PSW tool to better understand the key points of Data Science projects and get the most out of client meetings by making them more consistent and concise.

==PSW usually contains six main blocks:==

- **Background**. This block is filled with brief information about the current status of the project and challenges that caused its initiation.
- **Criteria for success**. Here it is important to find out how possible decisions to solve the project’s task(s) will be evaluated, and to rank all the criteria in order of importance.
- **Scope of solution space**. This block provides understanding where the boundaries of analysis end. It is best to clarify with the customer which areas should no longer be included in the consideration.
- **Constraints within solution space**. Here we outline the barriers that may arise in the decision space. It could be specific programming languages to use, some model requirements, or strict budget limits.
- **Stakeholders**. This is a list of people who will influence decision making and the success of the project. These people can be divided into those who decide, those who help, and those who hinder.
- **Key sources of insight**. This block intends to answer the question “Where to get data for solving our project’s tasks?”.  
    It is better to divide sources of information into relevant groups, like:  
    1) books, relevant research articles;  
    2) the latest industry reports;  
    3) similar projects, etc.

Below I will consider each of the blocks separately and give examples of what information they can be filled with.

# 1. Background

![](https://miro.medium.com/v2/resize:fit:700/0*HdCxwZulHiv3buAq)

Photo by [Keith Misner](https://unsplash.com/@keithmisner?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

==This is the first block, and usually it naturally happens after mutual greetings. Here I often ask clients to provide a little bit more context about the project: **why it appears, why it is important for the company, etc**. On one hand, these details will create a solid basement for a deeper dive into the project’s nuances, on the other — help with formulation the main goal of the project.==

==**If you can define the Project Objective in one sentence, then you understand the project just perfectly.**==

Here is a typical example of Background section based on input from one of the customers:

> Any mobile app must take into account the user needs in order to offer them the most convenient solutions. It is well established that users enter the app for a specific purpose, performing certain actions. But this sequence can be shortened by adding recommendations to the screen, for example, to make a transaction to another user faster. That’s where Machine Learning (ML) based recommender systems can help.
> 
> As a part of the project, it is necessary to rank contacts for each user depending on the amount of transfers made. There have already been attempts to train the model, so the baseline is already available, but now the task is to improve its accuracy by 5% or more while applying ML recommender algorithms.

As you can see, Background block helps to fit the project’s tasks into the general context of the business (**make an app even more user-friendly**) and could, if necessary, adjust them taking into account global goals (**applying ML-based recommender systems for that**).

# 2. Criteria for Success

![](https://miro.medium.com/v2/resize:fit:700/0*EHx4nH7k9V5eok8w)

Photo by [Guille Álvarez](https://unsplash.com/@guillealvarez?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

==Here you can ask the client **on what main parameters the project will be evaluated** and **what criteria will be used to determine the “success of the project”**. These can be financial indicators (like reduced costs) and non-financial ones (e.g. the number of active users of the application, the accuracy of the built model, etc.). In addition to specific criteria, it is important to learn about all the immeasurable wishes of the customer. Perhaps your clients will revolutionise their corporate culture with the help of your proposed measures (why not?!).==

Continuing with the mobile app and recommendation systems example, below are the possible success criteria for this project:

> 1) Selection a ML model for the system is properly explained.  
> 2) The baseline model has been improved by 5% or more.  
> 3) Speed of running model with no more than 6 hours from the moment of launch until the results are received.  
> 4) Model performance is checked on available data — it should have more than 85% accuracy on the test set.

# 3. Scope of Solution Space

![](https://miro.medium.com/v2/resize:fit:700/0*IqGGnYiUqx8s0qT0)

Photo by [Nicolas Lobos](https://unsplash.com/@lobosnico?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

==Here it is important to understand what are the boundaries of the project. Very often, this block of PSW includes a brief project’s background— why the topic of the project is important and relevant now, what solutions and benchmarks already exist on the market and can be modified further to satisfy the customer’s requirements.==

> If we talk about recommender systems, one should keep in mind that there are several approaches to create them.
> 
> We can consider methods based on content (content-based) or knowledge (knowledge-based), using collaborative filtering (collaborative filtering), or a hybrid approach. Hybrid systems combine the advantages of several systems, allowing them to become a one-stop tool for making recommendations.

# 4. Constraints within Solution Space

![](https://miro.medium.com/v2/resize:fit:700/0*tPEJ3VIrLc-MleM2)

Photo by [Joshua Hoehne](https://unsplash.com/@mrthetrain?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

==In this block, we want to outline the range of acceptable and unacceptable solutions. You can directly ask customers about this. “What are our limitations?” question might help. Here you might hear about restrictions on methods / techniques / programming languages. For the project we analysed, there were limits related to the use of open-source datasets for training ML models and reproducibility of obtained results. The latter can be achieved through providing a `README` file with detailed project’s description.==

> 1. Restriction on the use of third-party sources: when developing a recommender system, don’t use open data for model pre-training.  
> 2. Reproducibility of the implemented approach: when restarting model on another PC, the similar results should be obtained.

## Note

Blocks 3 and 4 in PSW might be confused. Really, how to understand the difference between solution space and constraints? Let’s look at an example.

Imagine you have found an old letter where your grandfather wrote that many years ago he hid in the backyard of the family house a chest with gold. He didn’t specify where exactly he did that, so the whole backyard would be a solution space. Once you read this letter you want to extract the treasure as soon as possible and think of using an escalator to find it. Unfortunately, the backyard is fenced and it is not possible to go there by escalator. In this case, the inability to use escalators would be a clear constraint within the solution space.

![](https://miro.medium.com/v2/resize:fit:700/0*DDSlpCELmJEqYLmd)

Photo by [Jean-Frederic Fortier](https://unsplash.com/@jffortier?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# 5. Stakeholders

![](https://miro.medium.com/v2/resize:fit:700/0*R0SRyYcZPzx0Y2H7)

Photo by [airfocus](https://unsplash.com/@airfocus?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

==This block of PSW gives an idea of which people’s opinion should be taken into account when implementing the project. Typically, stakeholders are those with an interest in the project’s outcome. They could be the members of a project team, project managers, executives, project investors, customers, and end users.==

> Stakeholders are people who will be affected by the project at any point in its life cycle, and their input can directly impact the outcome. In a case of development the recommender system, its integration to the app will be beneficial for two main groups of people:
> 
> 1) Users of the mobile app who save their time while using this system.  
> 2) Application developers who will increase user loyalty by making their product more functional.

# 6. Key Sources of Insight


==Typically this block contains any relevant information which allows to fully understand the topic — e.g. links to open-sourced API libraries [1], tutorials [2], repositories, research articles, etc.==

Here it is vitally important to ask customers about what has already been done on this project before. And if so, do not hesitate to ask them to share what was good and what was poorly implemented while doing the initial steps within the project. This will give you some hints about possible further actions and directions in which the project can be taken.

> For the considered Data Science project with recommender system, use any materials, including articles in the field of machine learning and predictive analytics, e.g. a comprehensive review about the latest achievements in this industry might be a good starting point [3].
> 
> Focus on up-to-date approaches to solving similar problems of ranking and recommendations.

# Conclusion

I hope the information in this post helps you to be well prepared for any client meetings and to ask proper questions on them.

Below I will summarise the main insights about the PSW method:

1. ==While applying PSW, don’t forget to record all the moments that the customer tells you. I usually sum up all the info into a single **Follow Up** file, which I use during the Data Science project implementation.==
2. The PSW tool is useful not only for client meetings. In addition, it can help newcomers to the Data Science project groups to quicker dive into the project while asking valuable questions to more experienced project group members.
3. Please, keep in mind that while PSW is a great and easy-to-use tool, it’s not a magical ‘one-size-fits-all’ solution. In some cases it won’t work.

> In general, the PSW approach works well for Data Science projects, where there is a clear vision of the task with some inputs from the client and initial trials of solving the task. In this case, customers can share this information with me in order to solve their challenge together with the help of PSW. However, in a case, when the project is characterised with a lot of unknown insights and unclear perspective, it would be difficult to apply the PSW tool. For instance, if clients request some idea generation for their Data Science project that hasn’t started yet, the PSW method won’t be applicable, and one needs to choose different ones.

Thanks for reading, and good luck with your projects!