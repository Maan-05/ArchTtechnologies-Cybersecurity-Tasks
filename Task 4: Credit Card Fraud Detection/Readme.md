Task 4: Credit Card Fraud Detection
Project Overview
This project involves building a machine learning model to identify fraudulent credit card transactions. The dataset contains transactions made by European cardholders, where the objective is to classify transactions as either Legitimate (0) or Fraudulent (1).

Key Challenges
Class Imbalance: Fraudulent transactions represent a very small fraction of the total data (less than 1%).

Feature Scaling: Features like 'Amount' have a much wider range than the anonymized 'V' variables, requiring normalization.

Technical Implementation
Data Preprocessing: Used StandardScaler to normalize the transaction amount, ensuring it does not bias the model due to its scale.

Handling Imbalance: Implemented the class_weight='balanced' parameter in the Logistic Regression model to ensure the minority (Fraud) class is given appropriate importance during training.

Data Splitting: Performed a stratified train-test split (80/20) to maintain the original distribution of fraud cases in both sets.

Model Performance
The model was evaluated using a classification report and a confusion matrix to prioritize Recall, as catching fraud is more critical than avoiding false alarms in this context.

Classification Report Summary:
Accuracy: 97%

Recall (Class 1 - Fraud): 0.92 (92%)

Precision (Class 1 - Fraud): 0.06

Confusion Matrix Insights:
The model successfully identified the majority of fraudulent cases, which is demonstrated in the high Recall score of 0.92.

Tools Used
Language: Python

Environment: Google Colab

Libraries: Pandas, Scikit-learn, Seaborn, Matplotlib