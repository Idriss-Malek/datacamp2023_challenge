# datacamp2023_challenge
# Predicting Property Fair Visitors Booking Probability


## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Description](#dataset-description)
3. [Data Preparation](#data-preparation)
4. [Exploratory Data Analysis](#exploratory-data-analysis)
5. [Addressing Class Imbalance](#addressing-class-imbalance)
6. [Model Development](#model-development)
7. [Model Evaluation](#model-evaluation)
8. [Conclusion](#conclusion)

## Introduction
The objective of this study is to predict the probability of property fair visitors booking a property. This involves exploring a dataset comprising visitor information and their booking behavior at property fairs. The goal is to develop a machine learning model that accurately predicts the likelihood of a visitor booking a property based on various features provided in the dataset.

## Dataset Description
### Property Purchase Data:
This dataset contains information about visitors at a property fair and their likelihood of booking a property. Each row represents a visitor, and the columns contain various attributes associated with the visitor and their purchasing behavior.
   - `VisitorID`
   - `Proj_Group`
   - `Proj_Segment`
   - `Proj_Type`
   - `Visitor_Group`
   - `Visitor_Gender`
   - `Question_Age`
   - `Question_Budget`
   - `Question_HHIncome`
   - `Question_InstallmentMonthly`
   - `Question_MarriageStatus`
   - `Question_Nationality`
   - `Question_Occupation`
   - `Question_P_Income`
   - `Question_TimeToMoveIn`
   - `Target` (target variable)
- **VisitorID:** Unique identifier for each visitor.
- **Proj_Group:** Group classification of the project (e.g., Outer, Central, Urban).
- **Proj_Segment:** Segment classification of the project (e.g., Standard Units, Premium Units).
- **Proj_Type:** Type classification of the project.
- **Visitor_Group:** Group classification of the visitor (e.g., Central, Outer).
- **Visitor_Gender:** Gender of the visitor.
- **Question_Age:** Age range of the visitor.
- **Question_Budget:** Budget of the visitor for purchasing a property.
- **Question_HHIncome:** Household income of the visitor.
- **Question_InstallmentMonthly:** Monthly installment the visitor is willing to pay.
- **Question_MarriageStatus:** Marital status of the visitor.
- **Question_Nationality:** Nationality of the visitor.
- **Question_Occupation:** Occupation of the visitor.
- **Question_P_Income:** Personal income of the visitor.
- **Question_TimeToMoveIn:** Time frame in which the visitor plans to move in.
- **Target_Variable_Convert:** Binary variable indicating whether the visitor booked a property (TRUE) or not (FALSE).

These dataset provides insights into the characteristics and preferences of visitors at the property fair, which can be leveraged to predict the probability of visitors booking a property. Further analysis and modeling can help identify key factors influencing booking decisions and optimize marketing strategies to target potential buyers effectively.

## Data Preparation
- Checked data types for each column and performed necessary transformations.
- Identified and handled missing values in numeric fields.
- Detected and treated outliers, if any.
- Generated distribution histograms for numeric and categorical columns.

## Exploratory Data Analysis
- Conducted descriptive statistics to understand the data distribution.
- Utilized visualizations to extract insights into the relationships between features and the target variable.

## Addressing Class Imbalance
Assessed the presence of class imbalance in the target variable and applied appropriate techniques to balance the dataset if necessary.

## Model Development
- Selected appropriate classification models.
- Fine-tuned model hyperparameters to enhance performance.
- Implemented variable reduction techniques to improve model efficiency.

## Model Evaluation
- Evaluated models using multiple metrics such as AUC, Gini, KS, Accuracy, Precision, Recall, MSE, and Silhouette.
- Determined the preferred accuracy measure for this scenario and provided reasoning.
- Computed feature importance using relevant methods to identify key predictors.

## Conclusion
In conclusion, this study presents a comprehensive approach to predicting the probability of property fair visitors booking a property. By leveraging machine learning techniques and thorough data analysis, we aim to provide valuable insights for property fair organizers and marketers in optimizing their strategies for attracting potential buyers.
