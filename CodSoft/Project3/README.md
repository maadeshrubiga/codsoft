#  Iris Flower Classification using Machine Learning

##  Overview
The **Iris Flower Dataset** is one of the most famous datasets in machine learning and statistics.  
It consists of **three Iris species** — *Setosa*, *Versicolor*, and *Virginica* — which can be distinguished based on the measurements of their **sepal** and **petal** lengths and widths.

This project aims to build a **machine learning classification model** that can accurately identify the species of an Iris flower based on its features.

---

##  Objective
To develop a model that learns from the given flower measurements and **classifies Iris flowers into their respective species** using supervised machine learning techniques.

---

##  Dataset Description
**File:** `iris.csv`

| Feature | Description |
|----------|--------------|
| `sepal length (cm)` | Length of the sepal in centimeters |
| `sepal width (cm)` | Width of the sepal in centimeters |
| `petal length (cm)` | Length of the petal in centimeters |
| `petal width (cm)` | Width of the petal in centimeters |
| `species` | Target variable (Setosa, Versicolor, Virginica) |

**Dataset Size:** 150 rows × 5 columns  
**Classes:** 3 (Setosa, Versicolor, Virginica)

---

##  Technologies Used
- **Python 3**
- **Pandas** – Data handling  
- **NumPy** – Numerical operations  
- **Matplotlib & Seaborn** – Data visualization  
- **Scikit-learn** – Model building and evaluation  

---

##  Approach

1. **Data Loading**
   - Loaded the dataset using Pandas from a `.csv` file.
2. **Data Visualization**
   - Explored feature relationships using **pair plots**, **heatmaps**, and **boxplots**.
3. **Data Preprocessing**
   - Split data into training and test sets (80/20).
   - Standardized features for better model performance.
4. **Model Training**
   - Trained a **Random Forest Classifier** to predict flower species.
5. **Evaluation**
   - Evaluated the model using **Accuracy**, **Precision**, and a **Confusion Matrix**.

---

##  Results

| Metric | Value |
|--------|--------|
| **Accuracy** | ~100% |
| **Precision** | ~100% |
| **Model Used** | Random Forest Classifier |

The Random Forest model achieved perfect accuracy on the test set, showing that the Iris dataset is linearly separable and suitable for introductory classification tasks.

---

##  Visualizations
- Pair Plot showing species separation  
- Correlation Heatmap between features  
- Box Plot for feature distributions  
- Confusion Matrix for model performance  

---

##  How to Run in Google Colab

1. Upload `iris.csv` to your Colab session:
   ```python
   from google.colab import files
   uploaded = files.upload()
