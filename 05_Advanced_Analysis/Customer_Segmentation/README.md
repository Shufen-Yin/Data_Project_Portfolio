# Customer Segmentation & Anomaly Detection Using Unsupervised Learning

## Project Overview
This project focuses on **customer segmentation and anomaly detection** using **unsupervised learning** techniques.  
The goal is to discover hidden customer groups, understand purchasing behavior, and identify unusual or high-risk customers to support marketing, pricing, and business decision-making.  

Unlike supervised classification or prediction tasks, this project emphasizes **data structure exploration and insight generation** rather than forecasting outcomes.  
Visualization is used for exploratory analysis and model interpretation.

---

## Business Use Case
Customer segmentation and anomaly detection are widely used in:

- Marketing strategy and targeted promotions  
- Customer value analysis and retention planning  
- Product positioning and assortment optimization  
- Resource allocation and inventory planning  
- Risk assessment and anomaly identification  

This project demonstrates how unsupervised learning can transform raw transactional data into actionable business insights.

---

## Dataset
**Wholesale Customers Dataset** (UCI Machine Learning Repository)

- Features include annual spending on different product categories.  
- Each row represents a customer; there are no predefined labels (true unsupervised learning scenario).  
- Note: The dataset is lightweight and suitable for GitHub.  
  For large datasets, only code is provided with download links.

[Dataset Download Link](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers)

---

## Methods & Techniques
1. **Exploratory Data Analysis (EDA)**  
   - Distribution analysis of customer spending patterns  
   - Identification of skewness, outliers, and heterogeneity  

2. **Feature Scaling**  
   - Standardization to ensure fair distance-based clustering  
   - Prevents high-magnitude features from dominating  

3. **Dimensionality Reduction**  
   - Principal Component Analysis (PCA)  
   - Reduces high-dimensional data to 2D for visualization  
   - Helps interpret cluster separation and structure  

4. **Clustering Algorithms**  
   - **K-Means Clustering**  
     - Identifies natural customer segments  
     - Optimized using inertia / elbow method  
   - *(Optional extension)* Hierarchical Clustering or Gaussian Mixture Models  

5. **Cluster Profiling**  
   - Analyze average spending behavior per cluster  
   - Identify:  
     - High-value customers  
     - Low-engagement customers  
     - Specialized or niche segments  

6. **Anomaly Detection**  
   - Density-based analysis to detect unusual customers  
   - Useful for identifying:  
     - Potential fraud  
     - Data quality issues  
     - Exceptional purchasing behavior  

---

## Key Skills Demonstrated
- Unsupervised learning: KMeans clustering, PCA for visualization  
- Data preprocessing: feature scaling, missing value handling  
- Cluster profiling and business insight extraction  
- Anomaly detection using density-based methods  
- Visualization for model interpretation  
- Portfolio-ready ML workflow for customer analytics

---

## Project Structure
```
Customer_Segmentation/
│
├── notebook/ Customer_Segmentation.ipynb/PDF # Main analysis notebook
│
├── figures/ # Visualization output
│ ├── silhouette_score.png
│ ├── pca_scatter.png
│ └── ...
│
├── README.md # This file

```

---

## How to Run
1. Download the **Wholesale Customers Dataset** from [UCI](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers).  
2. Place the CSV file in the notebook folder or update the path in the notebook.  
3. Open `Customer_Segmentation.ipynb` in Jupyter or Google Colab.  
4. Run all cells to reproduce clustering, PCA visualization, and anomaly detection.  
5. Figures will be saved in the `figures/` folder.

---

## Notes
- Clusters are generated using KMeans on scaled features; cluster numbers are arbitrary.  
- Anomalies are detected using density-based approaches and do not represent labeled fraud.  
- All insights are **demonstration purposes only** and suitable for portfolio showcase.
