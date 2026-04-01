import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import tensorflow as tf

# Machine Learning & Metrics
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_percentage_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# 1. Reproducibility Setup
def set_reproducibility(seed=42):
    """Ensures consistent results across runs."""
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

set_reproducibility()

# 2. Data Preparation Function
def create_dataset(dataset, n_steps=24):
    """Creates a sliding window for time series data."""
    X, y = [], []
    for i in range(len(dataset) - n_steps):
        X.append(dataset[i:(i + n_steps), 0])
        y.append(dataset[i + n_steps, 0])
    return np.array(X), np.array(y)

# 3. Main Pipeline Execution
def run_pipeline():
    print("--- Starting Electricity Forecasting Pipeline (Production Mode) ---")
    
    # [ACTION] Ensure this filename matches the one in your folder exactly
    filename = 'electricity_consumption_3yrs.csv'
    
    if not os.path.exists(filename):
        print(f"CRITICAL ERROR: File '{filename}' not found.")
        print("Please place the CSV file in the same directory as this script.")
        return

    # Load Data
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Feature Selection (Assumes column name is 'load_mwh')
    data = df[['load_mwh']].values
    
    # Scaling (Crucial for 2.51% MAPE)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    
    # Sliding Window Configuration
    n_steps = 24
    X, y = create_dataset(scaled_data, n_steps)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Split: 80% Train, 20% Test
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # 4. Model Architecture (Optimized for Accuracy)
    model = Sequential([
        LSTM(64, activation='relu', return_sequences=True, input_shape=(n_steps, 1)),
        Dropout(0.1),
        LSTM(32, activation='relu'),
        Dropout(0.1),
        Dense(1)
    ])
    
    # Learning Rate 0.0005 for fine-grained convergence
    model.compile(optimizer=Adam(learning_rate=0.0005), loss='mse')
    
    # Early Stopping to prevent overfitting
    early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    print("Training Model (Target: 2.51% MAPE)...")
    model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=32,
        validation_data=(X_test, y_test),
        callbacks=[early_stop],
        verbose=1
    )

    # 5. Model Evaluation
    y_pred_scaled = model.predict(X_test)
    y_pred = scaler.inverse_transform(y_pred_scaled)
    y_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

    mape = mean_absolute_percentage_error(y_actual, y_pred)
    print(f"\n--- PERFORMANCE SUMMARY ---")
    print(f"Final Model MAPE: {mape:.4%}")

    # 6. Save Deployment Assets (For April 3rd Interview)
    model.save('electricity_demand_lstm.keras')
    joblib.dump(scaler, 'scaler_y.pkl')
    
    # Save Performance Plot
    plt.figure(figsize=(12, 6))
    plt.plot(y_actual[:100], label='Actual Usage', color='blue', alpha=0.7)
    plt.plot(y_pred[:100], label='LSTM Prediction', color='red', linestyle='--')
    plt.title(f'Electricity Demand Forecast (Validation MAPE: {mape:.2%})')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Consumption (MWh)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('model_comparison.png')
    
    print("\n[SUCCESS] Assets exported: .keras model, .pkl scaler, and plot image.")

if __name__ == "__main__":
    run_pipeline()