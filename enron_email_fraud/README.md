# Enron Email Fraud Detection

## Table of Contents

- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Requirements](#requirements)
- [File Architecture](#file-architecture)
- [Additional Resources](#additional-resources)

## Business Understanding

In 2000, Enron was one of the largest companies in the United States. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. This project aims to build a machine learning model that can identify persons of interest (POIs) in the Enron fraud case based on financial and email data made public during the Federal investigation. POIs are individuals who were indicted, reached a settlement or plea deal with the government, or testified in exchange for prosecution immunity.

## Data Understanding

### Dataset Overview

- 146 Samples (individuals)
- 21 Features (financial and email metrics)
- Target variable: POI (boolean)

### Feature Types

Features in the dataset fall into three major categories:

| Feature Type | Description | Examples |
|--------------|-------------|----------|
| Financial Features | Monetary values related to compensation | bonus, salary, stock options |
| Email Features | Communication metrics | from_messages, to_messages, shared_receipt_with_poi |
| POI Label | Target variable | poi (boolean) |

### Statistical Summary

The dataset contains various financial metrics with significant variance and many missing values. Most features have a positively-skewed distribution with outliers.

| Statistic | bonus | salary | exercised_stock_options | expenses | from_messages | to_messages |
|-----------|-------|--------|-------------------------|----------|---------------|-------------|
| count | 82.00 | 95.00 | 102.00 | 95.00 | 86.00 | 86.00 |
| mean | 2,374,234.61 | 562,194.29 | 5,987,053.77 | 108,728.92 | 608.79 | 2,073.86 |
| std | 10,713,327.97 | 2,716,369.15 | 31,062,006.57 | 533,534.81 | 1,841.03 | 2,582.70 |
| min | 70,000.00 | 477.00 | 3,285.00 | 148.00 | 12.00 | 57.00 |
| max | 97,343,619.00 | 26,704,229.00 | 311,764,000.00 | 5,235,198.00 | 14,368.00 | 15,149.00 |

### Data Quality Issues

- Significant class imbalance for the POI feature
- Many features have missing values
- Non-individual entities in the dataset ('TOTAL', 'THE TRAVEL AGENCY IN THE PARK')
- Several features with unclear meaning (e.g., 'other')
- Features with extreme outliers

## Data Preparation

### Outlier Removal

- Removed 'TOTAL' sample (aggregate value)
- Removed 'THE TRAVEL AGENCY IN THE PARK' (not an individual)
- Retained other outliers as they represent actual individuals

### Feature Selection Process

#### Step 1: Missing Value Ratio

Removed features with more than 50% missing values:

- long_term_incentive (54.79%)
- deferred_income (66.44%)
- deferral_payments (73.29%)
- restricted_stock_deferred (87.67%)
- director_fees (88.36%)
- loan_advances (97.26%)
- email_address (100.00%)

#### Step 2: Low Variance Filter

Identified features with significant variance for retention.

#### Step 3: Correlation Analysis

Analyzed feature correlations to identify redundant and important features:

**Features With High Correlation to POI:**

| Feature | Correlation |
|---------|-------------|
| exercised_stock_options | 0.50 |
| total_stock_value | 0.37 |
| bonus | 0.30 |

**Features With Low Mean Correlation:**

| Feature | Mean Correlation |
|---------|------------------|
| expenses | 0.06 |
| bonus | 0.24 |

#### Feature Selection Methods

Applied multiple selection techniques:

- Correlation analysis
- Recursive Feature Elimination with Logistic Regression
- Recursive Feature Elimination with Random Forest

#### Selected Features

Based on the comprehensive analysis, three features were selected:

1. exercised_stock_options
2. bonus
3. expenses

### Feature Engineering

Created a new feature `pct_poi_messages` that calculates the percentage of a person's total messages that are to or from a POI.

### Dimensionality Reduction & Scaling

Applied various techniques to standardize features and reduce dimensionality:

- Principal Component Analysis (PCA)
- StandardScaler
- MinMaxScaler
- RobustScaler

## Modeling

### Model Selection

Tested multiple classification algorithms:

- Gaussian Naive Bayes
- Decision Tree
- AdaBoost
- K-Nearest Neighbors
- Random Forest

### Model Validation

Used 10-fold cross-validation with StratifiedShuffleSplit to ensure robust evaluation.

### Model Performance Comparison

| Classifier | Accuracy | Precision | Recall | F1 Score |
|------------|----------|-----------|--------|----------|
| GaussianNB (PCA) | 0.87 | 0.60 | 0.30 | 0.40 |
| DecisionTree (PCA) | 0.85 | 0.46 | 0.30 | 0.36 |
| AdaBoost (PCA) | 0.86 | 0.55 | 0.30 | 0.39 |
| KNeighbors (PCA) | 0.87 | 0.67 | 0.20 | 0.31 |
| RandomForest (StandardScaler + PCA) | 0.89 | 0.75 | 0.30 | 0.43 |

### Parameter Tuning

Used GridSearchCV to optimize model parameters, focusing on improving both precision and recall while maximizing F1 score.

### Tuned Model Performance

| Classifier | Accuracy | Precision | Recall | F1 Score |
|------------|----------|-----------|--------|----------|
| DecisionTree (RobustScaler + PCA) | 0.90 | 0.71 | 0.50 | 0.59 |
| RandomForest (RobustScaler + PCA) | 0.90 | 0.71 | 0.50 | 0.59 |
| KNeighbors (PCA) | 0.89 | 0.78 | 0.35 | 0.48 |
| AdaBoost (PCA) | 0.88 | 0.59 | 0.50 | 0.54 |

## Evaluation

### Selected Model

**DecisionTreeClassifier with RobustScaler and PCA**

## Conclusion

The Enron Email Fraud Detection project successfully developed a machine learning model to identify persons of interest in the Enron fraud case. The DecisionTreeClassifier, combined with RobustScaler and PCA, was selected as the final model due to its balanced performance across accuracy, precision, and recall. This model effectively captures the patterns indicative of fraudulent activities, providing a valuable tool for future fraud detection efforts. Continuous monitoring and updates will ensure the model remains effective and relevant.
