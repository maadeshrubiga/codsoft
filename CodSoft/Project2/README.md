https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies
#  Movie Rating Prediction using Lasso Regression

##  Project Overview

The **Movie Rating Prediction** project aims to build a machine learning model that predicts the **rating of a movie** based on its **genre, director, actors, year, duration, and votes**.  
By analyzing historical movie data, this project explores how different factors influence movie ratings given by users or critics.

The model uses **Lasso Regression**, a linear regression technique with regularization that helps reduce overfitting and identifies the most influential features.

---

## Objective

- Analyze historical movie data and understand key factors affecting ratings.  
- Preprocess and visualize the dataset to extract meaningful patterns.  
- Build a **Lasso Regression model** to predict movie ratings.  
- Evaluate model performance using metrics like **MAE**, **RMSE**, and **R² score**.  
- Provide insights into which features contribute most to the prediction.

---

##  Dataset Details

**Dataset Name:** `filmtv_movies.csv`

**Description:**  
This dataset contains detailed information about movies including their genre, duration, director, main actors, votes, and rating.

| Column Name | Description |
|--------------|-------------|
| `name` | Name of the movie |
| `year` | Release year of the movie |
| `duration` | Duration of the movie in minutes |
| `genre` | Genre or category of the movie |
| `total_avg` | Average rating of the movie (target variable) |
| `votes` | Number of votes or reviews |
| `director` | Director of the movie |
| `actors` | Lead actor |


---

##  Technologies Used

- **Python 3**
- **Pandas** – Data manipulation  
- **NumPy** – Numerical operations  
- **Matplotlib & Seaborn** – Data visualization  
- **Scikit-learn** – Machine Learning (Lasso Regression, preprocessing, metrics)

---

##  Project Workflow

### 1. Data Preprocessing
- Handle missing values in categorical and numerical columns  
- Encode categorical variables using **OneHotEncoder**  
- Split dataset into **training** and **testing** sets  

### 2. Exploratory Data Analysis (EDA)
Visualizations were used to understand the data:
- Distribution of movie ratings  
- Average rating by genre  
- Votes vs. ratings  
- Correlation between numeric features  
- Rating trends over years  

### 3. Model Building
Used **Lasso Regression** with a pipeline for:
- Data preprocessing (encoding + scaling)  
- Model training and prediction  

### 4. Model Evaluation
Evaluated using the following metrics:
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

---

##  Sample Output
 Model Evaluation:
Mean Absolute Error (MAE): 0.417
Root Mean Squared Error (RMSE): 0.581
R² Score: 0.832

 Predicted rating for new movie: 8.46


