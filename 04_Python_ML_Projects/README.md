# Python ML Project Portfolio

This repository showcases a collection of **Python machine learning projects** demonstrating data analysis, feature engineering, predictive modeling, and visualization skills. Each project is self-contained with its own dataset (or sample), notebook, and README for detailed instructions.

---

## Projects Overview

### 1. Credit Card Fraud Detection
**Folder:** `Credit_Card_Fraud_Detection/`  
**Goal:** Detect fraudulent credit card transactions using machine learning and handle highly imbalanced datasets.  

**Key Features:**
- ETL and data preprocessing
- Handling class imbalance (SMOTE)
- Logistic Regression & Random Forest modeling
- Model evaluation metrics: accuracy, precision, recall, F1, ROC-AUC
- Hyperparameter tuning
- Deployment and monitoring concepts

**Notebooks:**
- **Sample Project:** Quick demo using a small subset of the dataset  
- **Full ETL Demo:** End-to-end production-oriented ML pipeline (random data for demo, Kaggle download optional)  

[View Project →](Credit_Card_Fraud_Detection/README.md)

---

### 2. Stock Trading Signal & Price Prediction
**Folder:** `Stock_Signal_Prediction/`  
**Goal:** Predict Buy/Hold/Sell signals and forecast next-day stock prices using technical indicators and ML models.  

**Key Features:**
- Signal Prediction (Classification: Buy/Hold/Sell) using MACD & RSI
- Machine Learning Models: Logistic Regression, Random Forest, SVM
- Model evaluation: Accuracy, Precision, Recall, F1, ROC & Precision-Recall curves
- Feature importance visualization
- Random Forest Regression for next-day price prediction
- Visualization used for exploratory analysis and model interpretation

> Note: Signal labels are derived from technical indicator rules, not future returns.  
> Regression task predicts next-day close price as a baseline; not intended for long-horizon forecasting.  

[View Project →](Stock_Signal_Prediction/README.md)

---

## Repository Structure
---
Python_ML_Project/
├── Credit_Card_Fraud_Detection/
│ ├── CreditCardFraud_Sample_Project/
│ ├── CreditCardFraud_Full_ETL_Demo/
│ └── README.md
├── Stock_Signal_Prediction/
│ ├── clean_data.csv （from kaggle , Not included)
│ ├── Stock_Signal_Prediction.ipynb
│ ├── outputs/ (generated PNG figures)
│ └── README.md
└── README.md <-- This file
---

