#  Sales Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Project-brightgreen)


---

##  Project Overview

Sales prediction involves forecasting the amount of a product that customers will purchase, taking into account various factors such as advertising expenditure, target audience segmentation, and advertising platform selection.

In businesses that offer products or services, the role of a **Data Scientist** is crucial for predicting future sales. They utilize **machine learning techniques in Python** to analyze and interpret data, allowing them to make informed decisions regarding advertising costs. By leveraging these predictions, businesses can optimize their advertising strategies and **maximize sales potential**.

This project demonstrates how to predict sales using **Simple Linear Regression** in Python, based on advertising expenditures across different media channels.

---

##  Objective

To develop a machine learning model that can accurately predict product sales based on advertising investments, helping businesses allocate their budgets efficiently.

---

##  Dataset Information

**Dataset Name:** `advertising.csv`  
**Dataset Source:** Local / Kaggle  
**Total Records:** 200  
**Total Features:** 4

###  Dataset Columns

| Column Name | Description |
|--------------|-------------|
| **TV** | Advertising budget spent on TV (in thousands of dollars) |
| **Radio** | Advertising budget spent on Radio (in thousands of dollars) |
| **Newspaper** | Advertising budget spent on Newspaper (in thousands of dollars) |
| **Sales** | Sales revenue generated (in thousands of units) |

---

###  Sample Data (First 5 Rows)

| TV | Radio | Newspaper | Sales |
|----|--------|------------|-------|
| 230.1 | 37.8 | 69.2 | 22.1 |
| 44.5 | 39.3 | 45.1 | 10.4 |
| 17.2 | 45.9 | 69.3 | 9.3 |
| 151.5 | 41.3 | 58.5 | 18.5 |
| 180.8 | 10.8 | 58.4 | 12.9 |

---

###  Dataset Summary Statistics

| Feature | Mean | Min | Max | Std. Deviation |
|----------|------|-----|-----|----------------|
| **TV** | 147.04 | 0.7 | 296.4 | 85.85 |
| **Radio** | 23.26 | 0.0 | 49.6 | 14.85 |
| **Newspaper** | 30.55 | 0.3 | 114.0 | 21.78 |
| **Sales** | 14.02 | 1.6 | 27.0 | 5.22 |

---

##  Tools and Libraries Used

-  **Python 3.10+**
-  **Google Colab / Jupyter Notebook**
-  **Pandas** – Data manipulation and analysis  
-  **Matplotlib** – Data visualization  
-  **Scikit-learn (sklearn)** – Machine learning model creation and evaluation  

---

##  Steps Involved

1. **Import Libraries** – Load Python libraries for data analysis and visualization.  
2. **Upload Dataset** – Upload the CSV file to Google Colab using `files.upload()`.  
3. **Explore Data** – Inspect data structure, types, and missing values.  
4. **Visualize Data** – Plot TV advertising vs. sales to understand the relationship.  
5. **Model Building** – Apply `LinearRegression()` from sklearn.  
6. **Model Training** – Split data (80% training, 20% testing) and train the model.  
7. **Model Evaluation** – Evaluate using MAE, MSE, and R² Score.  
8. **Visualize Predictions** – Compare actual vs predicted values.  

---

##  Upload Dataset in Google Colab

```python
from google.colab import files
import pandas as pd

# Upload the dataset
uploaded = files.upload()

# Load the CSV file
data = pd.read_csv('advertising.csv')

# Display first few rows
print(data.head())

##sample output
Mean Absolute Error (MAE): 1.26
Mean Squared Error (MSE): 3.15
R² Score: 0.81

Regression Coefficient (Slope): 0.054
Regression Intercept: 7.02
