# Anomaly Detection Using Density Estimation

This project demonstrates **unsupervised anomaly detection** on industrial sensor data using **density estimation methods**.  
The goal is to detect anomalous sensor readings that may indicate **sensor drift, errors, or unusual events**.  

---

## Dataset

**Gas Sensor Array Drift Dataset (UCI)**  
Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Gas+Sensor+Array+Drift+Dataset)

> Note: The full dataset is **not included** due to size and multi-file `.dat` format.  
> To reproduce the results:
> 1. Download the dataset from UCI.
> 2. Extract the files to a local directory.
> 3. Update the `ZIP_FILE_PATH` / `EXTRACT_DIR` variable in the notebook.

Dataset details:  
- Sensor readings for 16 chemical sensors over multiple batches.  
- Values are in the format `sensor_index:value`.  
- Contains missing or invalid entries that require cleaning.

---

## Methods

- Data parsing and cleaning
- Handling missing values (drop mostly empty columns, fill remaining with median)
- Feature standardization using `StandardScaler`
- Density-based anomaly detection:
  - Gaussian Mixture Model (GMM): log-likelihood scores
  - Kernel Density Estimation (KDE): density scores
- Threshold-based anomaly selection (bottom 5% of density)
- Visualization of anomaly scores using Matplotlib & Seaborn

> Visualization is used for **exploratory analysis and model interpretation**, not as a primary EDA project.

---

## Steps Performed

1. Load dataset from ZIP (downloaded from UCI)  
2. Parse `index:value` format → extract numeric values  
3. Drop columns with >50% missing values  
4. Fill remaining missing values with column median  
5. Standardize features  
6. Unsupervised anomaly detection:
   - GMM: compute log-likelihood anomaly scores  
   - KDE: compute density-based anomaly scores  
7. Select anomalies: samples in the **lowest 5% density**  
8. Visualize anomaly scores and save figures to `figures/` folder

---

## Outputs

Figures saved in `figures/` folder:  
- `gmm_anomaly_scores.png` – GMM log-likelihood scores  
- `kde_anomaly_scores.png` – KDE density scores  

> Note: Anomalies detected are based on **density-based rules**, not labels.  
> This demonstrates unsupervised anomaly detection skills and may not generalize to other datasets.

---

## Key Skills Demonstrated

- Advanced data parsing and cleaning of real-world IoT datasets  
- Feature standardization and preprocessing  
- Unsupervised ML: GMM & KDE for anomaly detection  
- Threshold selection and anomaly score interpretation  
- Visualization for model interpretation and portfolio demonstration  
- Handling multi-file and messy sensor datasets  
- Portfolio-ready skills applicable to **industrial IoT monitoring, fraud detection, and high-dimensional unsupervised ML**

---

## Project Structure
```
Anomaly_Detection/
│
├── Anomaly_Detection.ipynb/PDF # Main analysis notebook
├──Outputs/figures/ # Saved figures of anomaly scores
│ ├── gmm_anomaly_scores.png
│ ├── kde_anomaly_scores.png
│
├── README.md # Project description
```

---

## How to Run

1. Download the dataset from [UCI](https://archive.ics.uci.edu/ml/datasets/Gas+Sensor+Array+Drift+Dataset)  
2. Place the ZIP file in your environment (e.g., Colab)  
3. Update `ZIP_FILE_PATH` and `EXTRACT_DIR` in the notebook  
4. Open `Anomaly_Detection.ipynb`  
5. Run all cells  

