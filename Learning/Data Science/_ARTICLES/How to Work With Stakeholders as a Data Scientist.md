https://towardsdatascience.com/how-to-work-with-stakeholders-as-a-data-scientist-13a1769c8152


One of the most important skills for a data scientist is being able to work effectively with stakeholders. Your impact will depend on your ability to brainstorm with product managers, collaborate with engineers, and persuade executives. This is a really exciting part of the job, however, it’s hard to find advice on doing it well. I’ve spent the past two years as a data scientist on product teams at Uber and Booking.com. Here are some tips on working with stakeholders over the course of a project that I wish I’d known when I started.

**1. Turn requests into dialogues**

When a stakeholder requests a specific output from you, that output is almost always the means to achieving some other goal. Try to turn the request into a dialogue about their primary goal and the best way to achieve it.

Suppose that a product manager asks you to experiment with removing the requirement that users provide their mailing address at signup, for example. If the product manager’s main goal is to drive conversion, you may decide that starting with a detailed funnel analysis could help to identify even more impactful opportunities.

A similar idea underpins [interest-based negotiation](https://www.amazon.com/Getting-Yes-Negotiate-Agreement-Without/dp/0743526937), which recommends that the parties to a negotiation should explore their underlying interests, rather than the more immediate positions with which they come to the table. ==As a data scientist, rather than just focusing on your stakeholder’s initial position (their immediate request), understand the interests that underpin it.==

**2. Learn to say no**

Within the first few weeks of starting as a data scientist, you’ll have more requests coming to you than it’s possible to handle. Taking on requests that you can’t complete won’t help anyone, so you’re going to have to say no. But if you say no in the wrong way, you’ll to annoy a lot of people. Here are a few of the techniques that I’ve found helpful.

Start by assuming the best, or at least being aware that you lack full information. If you get a request that you think the person should have taken care of themselves, for example, it can be tempting to ignore it or respond grumpily. Stop yourself! There’s a chance you’re missing a crucial piece of information and it’s a more reasonable request than you thought. Regardless, there’s no point in offending anyone.

Even if you’re responding with the best intentions, saying no without getting on a person’s bad side is not easy. One approach that I’ve found helpful is to [“separate the people from the problem”](https://www.amazon.com/Getting-Yes-Negotiate-Agreement-Without/dp/0743526937), another useful lesson from interest-based negotiation. Frame the discussion as two people working together to solve the problem of how best to invest data science resources, rather than you pushing back on their personal request.

![](https://miro.medium.com/v2/resize:fit:1400/1*CdjKq5aRBrHcODE0ZKKgVQ.png)

A second, closely related, strategy is to be transparent about your reasons for not prioritizing a project. Having objectives that everyone agrees on [“can make it easier to say no to the less important ideas. Saying no isn’t a political or emotional debate, it becomes a rational response to a commitment.”](https://rework.withgoogle.com/print/guides/6229207193485312/) A well-organized backlog of tasks can also help to turn potentially tense disagreements into rational discussions about where to spend your time, even when priorities are unclear and form part of the conversation.

Having a genuine discussion about the optimal use of your time will also make you more effective, as sometimes you’ll discover that “no” was in fact the wrong answer.

**3. Manage expectations**

When you’re new to a job and a colleague asks how long they’re going to have to wait for something they urgently need, it’s tempting to tell them what you think they want to hear, or at least put a positive spin on things. Resist that temptation!

We systematically underestimate how long tasks are going to take because [we focus on what’s in front of us and ignore the “unknown unknowns”](https://www.amazon.com/dp/B00555X8OA/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1), for example, the bug in your experiment that you didn’t anticipate. At the same time, the gap between people’s expectations and the outcomes that they perceive plays a large role in shaping their satisfaction, according to [expectancy-disconfirmation theory](https://en.wikipedia.org/wiki/Expectation_confirmation_theory).

Put these two psychological phenomena together and you have a recipe for trouble. You set expectations high by giving stakeholders your over-optimistic estimate (possibly exaggerating even further in the hopes of making them happy), and then their opinion of you comes crashing down when you fail to deliver. So be careful in managing expectations.

![](https://miro.medium.com/v2/resize:fit:1124/1*JgGV2Wrvgx9cuSuikDjJOg.png)

[Image source](https://theincidentaleconomist.com/wordpress/planning-falacy/)

One strategy to help address the overconfidence in your forecasts is a [premortem](https://www.amazon.com/dp/B00555X8OA/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1): imagine before you start that the project goes very wrong, and write a postmortem. If you decide that a full premortem is overkill, at least take the time to think through the different things that could go wrong. Considering potential pitfalls will help to both limit your overconfidence and catch problems before they happen.

**4. Know the context and own the execution**

Good product managers, Ben Horowitz argues, should [“know the context going in…and take responsibility for devising and executing a winning plan (no excuses).”](https://a16z.com/2012/06/15/good-product-managerbad-product-manager/) The same goes for data scientists, because you should also play a role in driving projects forward.

When working on projects as part of a bigger team, don’t bury your head in the data. Deeply understanding the context of the problem will help you do better work. It’s also important when communicating with stakeholders, since if you can’t answer a basic question about the larger project it will undermine your credibility.

Once you dive into a project, own the details and execution. The more you understand or contribute to the code used in deploying your model, for example, the more likely that you’ll spot problems before they arise. The outcome of a project will matter far more than who did what, so take ownership of projects succeeding beyond what is strictly your responsibility.

**5. Produce a minimum viable analysis**

Start by producing a minimum viable analysis: the fastest analysis that will let you begin to test the feasibility of your project. Then iterate and improve on your initial work. If you’re building a predictive model, for example, start with a simple model and a couple of promising features.

There are two advantages to starting with the most basic possible analysis, from the point of view of working with stakeholders. First, you will either have something to show for your work or can fail fast if the project isn’t going to work. You don’t want to find yourself three weeks into building a sophisticated model for your first project with nothing to share and no certainty about whether you’ll produce anything useful.

![](https://miro.medium.com/v2/resize:fit:1400/1*Uzber8zxlp4NEQ5N1f4ohA.png)

[Image source](https://medium.com/insights-from-meeteor/how-smart-meeting-practices-help-you-build-measure-learn-509dfc3f6c60)

Second, starting with a simple analysis allows you to get feedback as you iterate. The idea of a minimum viable product is to start with the minimum version of a product that allows for a [complete loop of building, measuring the product’s performance, and learning](https://www.amazon.com/Lean-Startup-Entrepreneurs-Continuous-Innovation/dp/0307887898). You can think of a similar loop as you progress with an analysis, with the measuring phase including getting feedback. I wouldn’t circulate your results to a large group here. Rather, ask for feedback from a small number of individuals, such as the product manager or another data scientist.

This iterative workflow isn’t the only way to structure a data science project, but it’s an effective and low-risk approach, especially for your first projects on a team.

**6. Communicate often and clearly**

As a product manager, Lenny Rachitsky notes, [“it’s very difficult to over-communicate”](https://hackernoon.com/how-to-get-into-product-management-78c58bd9c8cf). The same is true for data scientists because, again, you’ll often help to manage projects. Frequent communication is especially valuable, but tempting to avoid, when projects get delayed. Regular messaging keeps stakeholders up to date on progress and helps to reassure them that you’re dealing with the problem.

Good data scientists, like good product managers, [“err on the side of clarity.”](https://a16z.com/2012/06/15/good-product-managerbad-product-manager/) Pay great attention to clarity when sharing insights. You need to make sure that your findings can be quickly understood and will be correctly interpreted. If your results only apply to a specific group of users, for example, make it clear that people should be cautious about extrapolating to a broader population.

You should also take particular care to communicate clearly in writing. Gergely Orosz, an engineering manager I work with, highlights that writing well enables you to [“scale your ability to communicate efficiently to multiple teams, to an organisation or across the company.”](https://blog.pragmaticengineer.com/on-writing-well/) A key part of writing well as a data scientist is avoiding mistakes. You’re asking people to make big decisions based on your numbers, and they’ll find it hard to trust your diligence if your writing is full of typos. Always read over emails and docs to check for errors before sharing them.

**7. Communicate widely: Get visibility for your work**

The importance of communication doesn’t stop with wrapping up your analysis or deploying your model. Make sure to get visibility for your projects beyond your immediate team.

There are many ways to do this: reach out to discuss your project with people while it’s still in progress (you may also get useful input), write up your project and widely circulate an email linking to it (be sure to include a summary of your main points in the email), [create FAQs, papers, and other resources that people can leverage](https://a16z.com/2012/06/15/good-product-managerbad-product-manager/) (a persuasive plot can go far), or present your results internally or at external events.

It will be good for your career if people see the work that you’re doing, but it’s not just self-promotion. It’s extremely helpful for other people in your organization to know what you are working on, to avoid duplicating your work and identify opportunities to work together.

I hope that you’ve found this post helpful. This list is subjective and far from exhaustive, and it would be great if there were more discussion about how data scientists can work effectively within organizations. So if you disagree with anything or have other tips to share, please do comment below or reach out on [Twitter](https://twitter.com/sgbarrows).

_Big thank you to_ [_Mark_](https://www.linkedin.com/in/mark-belvedere/)_,_ [_Nick_](https://www.linkedin.com/in/jones-nicholas-s/) _and_ [_Samir_](https://www.linkedin.com/in/samir-mathew-a6487639/) _for reviewing drafts of this post._