# Credit Card Fraud Detection

## Overview
The **Credit Card Fraud Detection** project uses machine learning techniques to identify fraudulent transactions from credit card transaction data. By analyzing patterns and features, the model classifies transactions as genuine or fraudulent.

## Problem Statement
To develop a machine learning model capable of detecting credit card fraud by analyzing transaction data and distinguishing between fraudulent and genuine transactions.

## Dataset
The dataset includes 13 columns detailing transaction data:
- **User**: Unique identifier for users (1 to 1000).
- **Card**: Credit card identifier (1 to 8).
- **Year, Month, Day**: Date of the transaction.
- **Amount**: Transaction amount in dollars.
- **Use Chip**: Type of transaction ("Swipe Transaction", "Chip Transaction", "Online Transaction").
- **Merchant Name, City, State, Zip**: Details about the merchant.
- **MCC**: Merchant Category Code.
- **Is Fraud?**: Indicates if the transaction was fraudulent ("Yes" or "No").

## Approach
The project was implemented in several phases:

### 1. Data Preprocessing
- Handled missing values in the `Merchant State` and `Zip` columns using simple imputation (mean for numeric values, most frequent for categorical values).
- Balanced the dataset using undersampling to address class imbalance (`Yes`: 872, `No`: 691,048).
- Saved the preprocessed data as a CSV file.

### 2. Exploratory Data Analysis (EDA)
- Analyzed transaction patterns, focusing on fraud occurrences across transaction types and geographical locations.
- Identified that most frauds occurred in **Swipe Transactions** and six specific states.

### 3. Feature Selection
- Used correlation analysis and Extra Tree Classifier to extract the most relevant features.

### 4. Model Creation and Evaluation
- Implemented the **Random Forest Classifier** for its accuracy and robustness.
- Evaluated the model using metrics such as accuracy, precision, recall, and F1-score.
- Achieved an accuracy of 96%.

### 5. Model Deployment
- Deployed the model using Gradio and FastAPI for real-time prediction and user interaction.

## Key Insights
- **Transaction Type Analysis**:
  - Fraudulent transactions were most common in swipe transactions due to their lower security compared to chip-enabled and online transactions.
  - Chip transactions are more secure due to dynamic transaction codes.
  - Online transactions have higher fraud risks due to the absence of a physical card.

- **Yearly Trend Analysis**:
  - Fraud transactions increased from 1997 to 2014.
  - A decline was observed in 2015, followed by a rise in 2016.

## Conclusion
The project successfully demonstrated the application of machine learning and data analytics to detect and prevent fraudulent transactions, providing a robust solution for credit card fraud detection.

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- **Deployment**: Gradio, FastAPI

## Future Enhancements
- Optimize the Random Forest algorithm for faster real-time performance.
- Integrate continuous learning to adapt to new fraud patterns.
- Explore lightweight models for better efficiency in production environments.

---

### Team Members
- Chandan Dutta
- Anirban Chattaraj
- Sreya Singh
- Rajat Thakur

### Acknowledgments
Special thanks to our project guide, **Simanta Hazra**, for their guidance and support.
