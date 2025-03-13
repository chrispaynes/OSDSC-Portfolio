# Gibson Telecom Customer Analysis Using PCA

## Table of Contents

- [Business Understanding](#business-understanding)
- [Data Understanding](#data-understanding)
- [Data Preparation](#data-preparation)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Conclusion](#conclusion)

### 1. Business Understanding

Understanding customer characteristics is crucial for long-term profitability in customer relationship management. Gibson Telecom has recently hired Lisa Murphy, a new VP of Growth for the Northeastern Region of the United States. Lisa aims to familiarize herself with Gibson Telecom's customer base and personas. The primary business goal is to use Principal Component Analysis (PCA) to identify the principal variables of Gibson's customers, enabling better business and strategic decision-making.

### 2. Data Understanding

- **Data Collection**: The dataset includes customer data from Gibson Telecom, with features related to customer demographics, service usage, and financial metrics.
- **Data Description**: Key features include customer tenure, income, service usage patterns, and other demographic information.
- **Exploratory Data Analysis**: Initial analysis includes understanding the distribution of key metrics and identifying patterns in customer behavior.

### 3. Data Preparation

- **Data Cleaning**: Address missing values, remove duplicates, and normalize data where necessary.
- **Data Transformation**: Feature engineering to create new variables and prepare the data for PCA.
- **Data Splitting**: The dataset is prepared for PCA without the need for traditional train-test splits, as PCA is an unsupervised learning technique.

### 4. Modeling

- **Model Selection**: Principal Component Analysis (PCA) is used to reduce the dimensionality of the dataset.
- **Model Training**: PCA is applied to the dataset to identify the principal components that capture the maximal variance.
- **Model Evaluation**: The number of principal components is selected to explain at least 75% of the variance in the dataset.

### 5. Evaluation

- **Performance Analysis**: Evaluation of the PCA results to ensure that the selected components provide a comprehensive understanding of customer characteristics.
- **Business Evaluation**: Assessment of how well the principal components align with business objectives and provide actionable insights for strategic decision-making.

### 6. Deployment

- **Model Deployment**: The PCA results are used to inform business strategies and initiatives led by Lisa Murphy.
- **Monitoring and Maintenance**: Continuous monitoring of the PCA results and updates as necessary to maintain relevance and accuracy.

### Conclusion

The Gibson Telecom Customer Analysis project successfully utilized Principal Component Analysis (PCA) to identify key customer characteristics. The analysis revealed that 18 principal components (PCs) could account for 99.97% of the variance in the dataset. However, based on the scree plot and Kaiser Rule, the first 7 PCs were retained, capturing 57% of the variance. To capture 75% of the variance, the first 10 PCs were retained.

Key findings include:
- **PC1** captured 15% of the variance, with `Outage_sec_perweek`, `Email`, and `Item1` as the highest contributing features.
- **PC2** captured 11% of the variance, with `Income`, `Email`, and `Item1` as top contributors, noting that `Email` had a negative contribution.
- **PC3** captured 8% of the variance.

Throughout the 7 PCs, `Item1`, `Email`, and `Bandwidth_GB_Year` were frequently seen as top contributors. These insights provide a robust framework for understanding customer behavior and informing strategic initiatives, equipping Lisa Murphy with the necessary insights to drive growth in the Northeastern Region, aligning with Gibson Telecom's business objectives.
