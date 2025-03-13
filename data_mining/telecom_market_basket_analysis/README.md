# Gibson Telecom Market Basket Analysis

## Table of Contents

- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Conclusion](#conclusion)

### 1. Business Understanding

Gibson Telecom aims to enhance customer loyalty and reduce churn by experimenting with a customer rewards program. The company plans to offer discounted tech item bundles to customers on their birthdays and to new customers upon signup. The primary business question is whether analysts can mine customer transaction data to identify key product associations that can help develop these product bundles.

### 2. Data Understanding

- **Data Collection**: The dataset consists of customer transaction records from Gibson Telecom, detailing purchased items.
- **Data Description**: Each transaction includes multiple items, represented in a one-hot encoded format where each row corresponds to a transaction.
- **Exploratory Data Analysis**: Initial analysis includes understanding the distribution of items across transactions and identifying any prevalent purchasing patterns.

### 3. Data Preparation

- **Data Cleaning**: Address missing values and ensure data consistency.
- **Data Transformation**: Convert transaction data into a format suitable for market basket analysis, typically using one-hot encoding.
- **Data Splitting**: Not applicable, as market basket analysis is an unsupervised learning technique.

### 4. Modeling

- **Model Selection**: Market Basket Analysis using the Apriori algorithm is selected to identify frequent itemsets and association rules.
- **Model Training**: The Apriori algorithm is applied to the dataset to generate frequent itemsets and association rules.
- **Model Evaluation**: The rules are evaluated based on support, confidence, and lift metrics to ensure they provide actionable insights.

### 5. Evaluation

- **Performance Analysis**: Analyze the generated association rules to identify meaningful product bundles.
- **Business Evaluation**: Assess how well the identified product bundles align with business objectives and can be used to enhance customer loyalty.

### 6. Deployment

- **Model Deployment**: The identified product bundles are used to inform the customer rewards program, offering discounts to customers.
- **Monitoring and Maintenance**: Continuous monitoring of transaction data to update and refine product bundles as necessary.

### Conclusion

The Gibson Telecom Market Basket Analysis project successfully utilized the Apriori algorithm to identify key product associations within customer transaction data. The analysis identified three product bundles that can be offered to customers as part of a rewards program. These bundles are designed to enhance customer loyalty and reduce churn by providing value to both existing and new customers. The project demonstrates the potential of market basket analysis to uncover valuable insights from transaction data, supporting strategic marketing initiatives.
