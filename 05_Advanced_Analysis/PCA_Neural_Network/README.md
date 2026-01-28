# PCA and Neural Network-Based Dimensionality Reduction — Human Activity Recognition

## Project Overview
This project demonstrates **dimensionality reduction techniques** on the **Human Activity Recognition Using Smartphones (HAR) dataset**, a high-dimensional sensor dataset capturing human motion activities such as walking, sitting, standing, and climbing stairs.

The main goals are:
- Apply **Principal Component Analysis (PCA)** for linear dimensionality reduction.
- Implement a **neural network autoencoder** for non-linear dimensionality reduction.
- Compare linear and non-linear representations to explore complex structures in sensor data.
- Visualize low-dimensional embeddings for model interpretation.

> Visualization is used for exploratory analysis and **model interpretation**, not just EDA.

---

## Dataset

**Human Activity Recognition Using Smartphones (HAR) Dataset** — UCI Machine Learning Repository  
[Download Link](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones)

**Details:**
- **Features:** 561 sensor time- and frequency-domain signals  
- **Samples:** 7352 training, 2947 test  
- **Activities (labels):** 6 classes — Walking, Walking Upstairs, Walking Downstairs, Sitting, Standing, Laying  

**Note:**  
Dataset is **not included** in this repository due to size and copyright.  
To run the notebook, download the zip file and upload it to **Google Colab**.

---

## Methodology

1. **Data Preprocessing**
   - Load training and test sets.
   - Standardize features using `StandardScaler` for fair comparison between PCA and neural networks.

2. **Linear PCA**
   - Reduce high-dimensional features to 2D.
   - Analyze explained variance ratio.
   - Visualize clusters of activities in 2D space.

3. **Neural Network Autoencoder**
   - Build a symmetric feed-forward autoencoder using TensorFlow/Keras.
   - Bottleneck layer = 2D for direct comparison with PCA.
   - Train autoencoder to reconstruct inputs.
   - Extract 2D latent representations for visualization.

4. **Comparison & Analysis**
   - Examine how well PCA vs. autoencoder separates activities.
   - Highlight non-linear representation advantages.
   - Discuss interpretability vs. flexibility trade-offs.

---

## Key Skills Demonstrated

- High-dimensional data preprocessing and standardization
- Linear (PCA) and non-linear (autoencoder) dimensionality reduction
- Neural network design, training, and representation learning
- 2D visualization and interpretation of latent embeddings
- Reproducible ML workflow suitable for GitHub/Colab

---

## Results

- **PCA 2D Projection:** Shows partial separation between activity clusters; some overlap remains.  
- **Autoencoder 2D Representation:** Better separation, capturing non-linear structures in the data.  
- Both visualizations are included in the notebook and can be found in the `figures/` folder.

> Note: This project focuses on dimensionality reduction and representation learning, not activity classification or long-term prediction.

---

## How to Run

1. Open `PCA_with_Neural_Networks.ipynb` in **Google Colab**.  
2. Upload the downloaded dataset zip (`UCI HAR Dataset.zip`) to Colab.  
3. Run all cells sequentially.  
4. Figures and embeddings will be saved in the `figures/` folder.

---

## Repository Structure
```
PCA_Neural_Network/
│
├── PCA_with_Neural_Networks.ipynb # Main notebook
├── figures/ # Visualizations output
│ ├── pca_2d_projection.png
│ └── autoencoder_2d_projection.png
├── README.md # Project description
```
