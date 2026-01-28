# Stock Trading Signal & Future Price Prediction

## Project Overview
This project demonstrates how to predict **Buy/Hold/Sell signals** and forecast **next-day stock prices** using technical indicators and machine learning models. It is designed for **demonstration purposes** and is suitable for a portfolio showcase of data analysis and ML skills.

**Key Features:**
- **Signal Prediction (Classification):**
  - Predicts Buy, Hold, or Sell signals using:
    - MACD (Moving Average Convergence Divergence)
    - RSI (Relative Strength Index)
  - Machine Learning Models:
    - Logistic Regression
    - Random Forest Classifier
- **Future Price Prediction (Regression):**
  - Predicts next-day closing prices using Random Forest Regression.
- **Visualizations:**
  - Feature importance for Random Forest
  - ROC & Precision-Recall curves
  - Signal distribution
  - Actual vs Predicted prices for regression

**Dataset:**
- Daily stock prices including Open, High, Low, Close, and Volume.
- Multiple tickers included.
- **Data source:** [Yahoo Finance](https://finance.yahoo.com/) or [Kaggle Stock Market Dataset](https://www.kaggle.com/datasets)

---

## Usage
- The notebook is designed for **demonstration purposes**; no dataset is included in the repository.  
- To run the notebook:
  1. Download historical stock data (CSV) for the tickers you want from Yahoo Finance or Kaggle.
  2. Place the CSV in the project folder and rename it `clean_data.csv` (or update the notebook path accordingly).
  3. Run the notebook to execute all steps:
     - Data preprocessing and technical indicator computation
     - Buy/Hold/Sell signal generation
     - Train ML models (Logistic Regression, Random Forest, SVM)
     - Evaluate model performance and plot feature importance
     - ROC / Precision-Recall curves for classification
     - Random Forest Regression for next-day price prediction

> **Note:** For demonstration purposes, the notebook will generate plots and evaluation metrics once the CSV is loaded. Results may vary depending on the tickers and date ranges you choose.

---

## Model Evaluation

**Classification (Random Forest Example):**
- Accuracy: 0.999
- Precision: 0.999
- Recall: 0.999
- F1 Score: 0.999
- Feature Importance:
  - MACD and MACD_signal are the most influential indicators.
  - RSI contributes moderately.

**Regression (Random Forest Regression):**
- MAE: 0.49 — predicted prices deviate on average by 0.49 units.
- RMSE: 0.64 — larger deviations indicate occasional sensitivity to outliers.
- Captures short-term trends reasonably well, but not suitable for live trading.

---

## Insights
- Random Forest outperforms Logistic Regression for classification.
- Feature importance shows MACD is the most significant predictor of Buy/Sell signals.
- Regression provides reasonable next-day price trends.
- Combining classification signals with regression predictions can be used for hybrid analysis.
- This project demonstrates **ML workflow, feature engineering, and visualization** for stock market data.

---

## Notes
- Signals and predictions are **for demonstration only**.
- Does **not account for transaction costs, slippage, or market impact**.
- Should not be used for actual trading.
- Users must download their own historical stock data to reproduce results.
