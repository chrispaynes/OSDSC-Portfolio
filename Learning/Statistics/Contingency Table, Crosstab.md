A contingency table, also known as a cross-tabulation or crosstab, is a table that displays the frequency distribution of two or more categorical variables. In the context of a chi-square test, a contingency table is used to examine the association between two categorical variables.

Let's consider a simple example to illustrate the concept. Suppose we have two categorical variables: "Gender" (with categories Male and Female) and "Smoking Status" (with categories Smoker and Non-Smoker). We collect data on a group of individuals and record their gender and smoking status. The contingency table might look like this:

```
                 |  Smoker  | Non-Smoker |
-----------------|----------|------------|
      Male       |   20     |     30     |
      Female     |   15     |     35     |
```

In this table:

- The rows represent the categories of one variable (e.g., Gender).
- The columns represent the categories of another variable (e.g., Smoking Status).
- The intersection cells contain the frequencies or counts of individuals falling into each combination of categories.

Once the contingency table is constructed, it can be used to perform a chi-square test of independence. The chi-square test assesses whether there is a statistically significant association between the two categorical variables. The test compares the observed frequencies in the contingency table with the frequencies that would be expected if the variables were independent.

The hypotheses for the chi-square test are as follows:

- Null Hypothesis (H₀): There is no association between the variables.
- Alternative Hypothesis (H₁): There is an association between the variables.

The chi-square test statistic is calculated based on the differences between observed and expected frequencies. If the calculated chi-square statistic is significantly different from what would be expected under independence, the null hypothesis may be rejected, suggesting evidence of an association between the variables.