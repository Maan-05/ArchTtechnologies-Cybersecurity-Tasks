# Task 4: Credit Card Fraud Detection

## Project Goal
The objective of this task is to develop a robust machine learning classification model to identify fraudulent credit card transactions. By analyzing transaction patterns, the model aims to minimize financial risk and improve security for cardholders.

## Technical Overview
* **Programming Language:** Python
* **Development Environment:** Google Colab
* **Key Libraries:** Pandas, Scikit-learn, Matplotlib, Seaborn

## Methodology
The following technical steps were implemented to ensure high detection accuracy:

1. **Data Preprocessing:** Standardized the "Amount" feature using `StandardScaler` to ensure the model is not biased by varying transaction scales.
2. **Handling Class Imbalance:** Since fraud cases are rare, the model was trained using `class_weight='balanced'`. This ensures the minority class (Fraud) receives appropriate weight during the training phase.
3. **Data Splitting:** Utilized a stratified 80/20 train-test split to maintain the proportional representation of fraud cases in both training and evaluation sets.

## Performance Metrics
The model was evaluated using a classification report and a confusion matrix with the following results:
* **Recall (Fraud Class):** **0.92** – Successfully identified 92% of all fraudulent activities.
* **Overall Accuracy:** **0.97**.
* **Optimization Priority:** Focused on **Recall** as the primary metric to ensure maximum detection of actual fraud cases.

## Repository Files
* `Creditcard_Fraud_Detection.ipynb`: The primary Python notebook containing the full implementation.
* `Confusion_Matrix.png`: Heatmap visualization showing the model's prediction accuracy.
* `Classification_Report.txt`: Full breakdown of Precision, Recall, and F1-score for both classes.

---
**Note:** This project was completed as part of the Arch Technologies internship program.