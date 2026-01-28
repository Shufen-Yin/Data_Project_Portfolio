# Advanced Analysis Projects 

This folder contains **advanced Python machine learning projects** demonstrating **unsupervised learning, clustering, anomaly detection, and dimensionality reduction techniques**.  
These projects highlight skills in **data preprocessing, feature engineering, PCA, neural networks, and visualization** applied to real-world datasets.

> All projects are self-contained and designed for **portfolio showcase**, highlighting objectives, methods, skills, and outcomes.  

---

## Projects Overview

### 1. Anomaly Detection
**Folder:** `Anomaly_Detection/`  
**Goal:** Detect unusual patterns or outliers in high-dimensional sensor data using unsupervised techniques.  

**Key Features:**
- Gaussian Mixture Model (GMM) and Kernel Density Estimation (KDE)
- Feature scaling and data cleaning
- Threshold-based anomaly detection
- Visualization of anomaly scores
- Insights into sensor drift or faulty measurements

[View Project →](Anomaly_Detection/README.md)

---

### 2. Customer Segmentation
**Folder:** `Customer_Segmentation/`  
**Goal:** Segment wholesale customers based on purchasing behavior to support marketing, pricing, and business strategy.  

**Key Features:**
- K-Means clustering and evaluation (Elbow & Silhouette methods)
- Feature scaling and PCA for visualization
- Cluster profiling and business interpretation
- Insights for customer targeting, inventory, and promotions

[View Project →](Customer_Segmentation/README.md)

---

### 3. PCA & Neural Network Dimensionality Reduction
**Folder:** `PCA_Neural_Network/`  
**Goal:** Apply linear and non-linear dimensionality reduction techniques to high-dimensional sensor data.  

**Key Features:**
- Principal Component Analysis (PCA) as baseline
- Neural network autoencoder for non-linear reduction
- 2D latent space visualization
- Comparison between PCA and autoencoder representations
- Insights into complex structure of Human Activity Recognition (HAR) data

[View Project →](PCA_Neural_Network/README.md)

---

## Dataset Disclaimer

All datasets are **not included** due to size and copyright restrictions.  
Please download from the official sources and upload to **Google Colab** before running notebooks:

1. **Wholesale Customers Data Set:**  
   [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers)

2. **Gas Sensor Array Drift Dataset:**  
   [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Gas+Sensor+Array+Drift+Dataset)

3. **Human Activity Recognition Using Smartphones Dataset (HAR):**  
   [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones)

> All notebooks automatically read datasets from uploaded folders.

---

## Skills Highlight

- Unsupervised learning: clustering, anomaly detection, density estimation  
- Dimensionality reduction: PCA, autoencoders, feature scaling  
- Neural networks: autoencoder design and training  
- Data visualization: 2D scatter plots, anomaly score plots  
- Portfolio-ready ML workflow and reproducible analysis

---

## How to Use

1. Open the notebook of the project you want to run in **Google Colab**.  
2. Upload the corresponding dataset zip to the Colab environment.  
3. Run all cells sequentially.  
4. Figures and outputs are saved in the respective project `figures/` folder.

---

## Repository Structure
```
05_Advanced_Analysis/
│
├── Anomaly_Detection/
│ ├── README.md
│ ├── Anomaly_Detection.ipynb/PDF
│ └── figures/Outputs
│
├── Customer_Segmentation/
│ ├── README.md
│ ├── Customer_Segmentation.ipynb/PDF
│ └── figures/Outputs
│
├── PCA_Neural_Network/
│ ├── README.md
│ ├── PCA_with_Neural_Networks.ipynb/PDF
│ └── figures/Outputs
│
├── README.md # This overview file
```

---

This folder provides a **comprehensive showcase of advanced data science skills**, from clustering and anomaly detection to dimensionality reduction and neural network modeling, ready for inclusion in a professional portfolio.
