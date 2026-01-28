
# Credit Card Fraud Detection – End-to-End ML Pipeline

This folder contains a production-oriented machine learning pipeline for credit card fraud detection using both a small sample dataset and a full pipeline demonstration.

---

## Project Overview

Credit card fraud datasets are highly imbalanced and require careful preprocessing, modeling, and evaluation.  
This project demonstrates:

- ETL and data preprocessing
- Handling class imbalance (SMOTE)
- Logistic Regression & Random Forest modeling
- Model evaluation metrics (accuracy, precision, recall, F1, ROC-AUC)
- Hyperparameter tuning
- Deployment and monitoring considerations

> Note:
> - The Sample Notebook uses a small subset (~5,000 rows) from the full Kaggle dataset (`creditcard_sample.csv`) for quick demonstration and analysis.
> - The Full ETL Notebook demonstrates a complete ML pipeline. For reproducibility and simplicity, it uses randomly generated data (`random seed`) instead of the full Kaggle dataset. Kaggle download code is included but commented.

---

## Folder Structure
```
Credit_Card_Fraud_Detection/
├── CreditCardFraud_Sample_Project/
│ ├── creditcard_sample.csv # Small sample dataset (~5,000 rows)
│ └── CreditCardFraud_Sample.ipynb/PDF
├── CreditCardFraud_Full_ETL_Demo/
│ └── CreditCardFraud_Full_ETL_Demo.ipynb /PDF# Full ETL & pipeline workflow with random data
```

### Sample Project
- **Purpose**: Quick demo using a real small sample of the full dataset  
- **Notebook**: `CreditCardFraud_Sample.ipynb`  
- **Skills demonstrated**:
  - Exploratory Data Analysis (EDA)
  - Data preprocessing & feature scaling
  - Logistic Regression & Random Forest modeling
  - Model evaluation metrics: accuracy, precision, recall, F1, ROC-AUC
  - Quick hyperparameter tuning for Random Forest
  - Observations and insights extraction

### Full ETL Demo
- **Purpose**: Demonstrate a full production-oriented ML pipeline  
- **Notebook**: `CreditCardFraud_Full_ETL_Demo.ipynb`  
- **Key highlights**:
  - ETL pipeline and data preprocessing
  - Handling class imbalance using SMOTE
  - Logistic Regression model training and hyperparameter tuning
  - Model evaluation focusing on ROC-AUC and confusion matrix
  - Deployment and monitoring considerations
  - Random data generated for demo purposes (`np.random.seed`)  
  - Kaggle full dataset download code included but commented for reproducibility

**Evaluation Focus**

- **ROC-AUC** is prioritized over accuracy due to class imbalance
- **Confusion matrix** helps assess false negatives, which are costly in fraud detection.

> **Note:** The output shows that the sample data is highly imbalanced, resulting in a recall of 0.  
> In practice, when using the full dataset, techniques such as **SMOTE** or **class weighting** are needed to improve recall.
  
---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Shufen-Yin/Python_Project.git
cd 04_Python_ML_Project/Credit_Card_Fraud_Detection
```
## Open notebooks in Jupyter or VSCode

- **Sample Notebook:** [Sample Notebook](https://github.com/Shufen-Yin/Data_Project_Portfolio/tree/main/04_Python_ML_Projects/Credit_Card_Fraud_Detection/CreditCardFraud_Sample_Project)
or CreditCardFraud_Sample_Project/CreditCardFraud_Sample.ipynb 

- **Full ETL Notebook:** [Full ETL Notebook](https://github.com/Shufen-Yin/Data_Project_Portfolio/tree/main/04_Python_ML_Projects/Credit_Card_Fraud_Detection/CreditCardFraud_Full_ETL_Demo)
or CreditCardFraud_Full_ETL_Demo/CreditCardFraud_Full_ETL_Demo.ipynb

The Full ETL notebook runs with generated random data, so you do not need the full Kaggle dataset to explore the pipeline.

**Key Skills Demonstrated**

-  Data preprocessing and feature scaling

-  Handling imbalanced datasets (SMOTE, class weighting)

-  Logistic Regression & Random Forest modeling

-  Model evaluation metrics (accuracy, precision, recall, F1-score, ROC-AUC)

-  Quick hyperparameter tuning

-  Production-oriented pipeline concepts

-  Deployment and monitoring considerations
