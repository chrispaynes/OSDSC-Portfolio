https://greenteapress.com/wp/think-bayes/
https://github.com/AllenDowney/ThinkBayes2
https://allendowney.github.io/ThinkBayes2/

# Preface

# Chapter 01 - Probability
- The foundation of Bayesian statistics is Bayes's Theorem, and the foundation of Bayes's Theorem is conditional probability.
- A **probability** is a fraction of a finite set.
	- For example, if we survey 1000 people, and 20 of them are bank tellers, the fraction that work as bank tellers is 0.02 or 2%. If we choose a person from this population at random, the probability that they are a bank teller is 2%. By "at random" I mean that every person in the dataset has the same chance of being chosen.
- "**Conjunction**" is another name for the logical and operation. If you have two propositions, A and B, the conjunction A and B is True if both A and B are True, and False otherwise.
	- We expect conjunction to be commutative; that is, A & B should be the same as B & A.
- **Conditional probability** is a probability that depends on a condition
	- "What is the probability that a respondent is a Democrat, **given that** they are liberal?"
		- we can interpret like this: "Of all the respondents who are liberal, what fraction are Democrats?"
	-  conditional probability **is not** commutative; that is, conditional(A, B) is not the same as conditional(B, A).
- We can combine conditional probability and conjunction:
	- `conditional(female, given=liberal & democrat)`
	- `conditional(liberal & female, given=banker)`
### Laws of Probability
- three relationships between conjunction and conditional probability:
	- **Theorem 1:** Using a conjunction to compute a conditional probability.
		- `𝑃(𝐴) is the probability of proposition 𝐴.`
		- What fraction of bankers are female?
			- `conditional(female, given=banker)`
			- there is another way to compute this conditional probability, by computing the ratio of two probabilities:
				- The fraction of respondents who are female bankers, and
				- The fraction of respondents who are bankers.
				- prob(female & banker) / prob(banker)
				- $P(A|B) = \frac{P(A~\mathrm{and}~B)}{P(B)}$

	- **Theorem 2:** Using a conditional probability to compute a conjunction.
		- `𝑃(𝐴 and 𝐵) is the probability of the conjunction of 𝐴 and 𝐵, that is, the probability that both are true.`
		- $P(A~\mathrm{and}~B) = P(B) ~ P(A|B)$
		- compute a conjunction using the product of two probabilities.
			- `prob(democrat) * conditional(liberal, democrat)`
		- 
	- **Theorem 3:** also known as Bayes's Theorem, gives us a way to get from 𝑃(𝐴|𝐵) to 𝑃(𝐵|𝐴), or the other way around:
		- Using `conditional(A, B)` to compute `conditional(B, A)`.
		- `𝑃(𝐴|𝐵) is the conditional probability of 𝐴 given that 𝐵 is true. The vertical line between 𝐴 and 𝐵 is pronounced "given".`
		-  also known as Bayes's Theorem
		- `𝑃(𝐴 and 𝐵) = 𝑃(𝐵 and 𝐴)`
		- `𝑃(𝐵)𝑃(𝐴|𝐵)=𝑃(𝐴)𝑃(𝐵|𝐴)`
		- $P(A|B) = \frac{P(A) P(B|A)}{P(B)}$
### The Law of Total Probability
- $𝑃(𝐴)=𝑃(𝐵1and𝐴)+𝑃(𝐵2and𝐴)$
- In words, the total probability of 𝐴 is the sum of two possibilities: either 𝐵1 and 𝐴 are true or 𝐵2 and 𝐴 are true.
	- this law applies only if 𝐵1 and 𝐵2 are:
		- Mutually exclusive, which means that only one of them can be true, and
		- Collectively exhaustive, which means that one of them must be true.
- `prob(male & banker) + prob(female & banker)`
	- Because male and female are mutually exclusive and collectively exhaustive (MECE), we get the same result we got by computing the probability of banker directly.
- **When** there are more than two conditions, it is more concise to write the law of total probability as a summation:
- ![[Pasted image 20240215090246.png]]
	- $𝑃(𝐴)=∑𝑖𝑃(𝐵𝑖)𝑃(𝐴|𝐵𝑖)$
- If we have all of the data, we can compute any probability we want, any conjunction, or any conditional probability, just by counting. We don't have to use these formulas. And you are right, _if_ we have all of the data. But often we don't, and in that case, these formulas can be pretty useful
# Chapter 02 - Bayes’s

# Chapter 03 - Distributions

# Chapter 04 - Estimating

# Chapter 05 - Estimating

# Chapter 06 - Odds

# Chapter 07 - Minimum

# Chapter 08 - Poisson

# Chapter 09 - Decision

# Chapter 10 - Testing

# Chapter 11 - Comparison

# Chapter 12 - Classification

# Chapter 13 - Inference

# Chapter 14 - Survival

# Chapter 15 - Mark

# Chapter 16 - Logistic

# Chapter 17 - Regression

# Chapter 18 - Conjugate

# Chapter 19 - MCMC

# Chapter 20 - Approximate