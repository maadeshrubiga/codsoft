#  Titanic Survival Prediction using Logistic Regression (Google Colab)

This project applies data mining techniques to predict passenger survival on the Titanic using **Logistic Regression**. The analysis is performed in **Google Colab**, making use of its interactive notebook environment and built-in file upload capabilities. The goal is to build a predictive model using demographic and ticketing data, and to visualize key patterns in survival outcomes.

---

##  Dataset Description

The dataset (`tested.csv`) contains information about passengers aboard the Titanic. Each row represents a passenger, with the following columns:

- **PassengerId**: Unique identifier for each passenger  
- **Survived**: Survival status (0 = No, 1 = Yes)  
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)  
- **Name**: Full name of the passenger  
- **Sex**: Gender of the passenger  
- **Age**: Age in years  
- **SibSp**: Number of siblings/spouses aboard  
- **Parch**: Number of parents/children aboard  
- **Ticket**: Ticket number  
- **Fare**: Fare paid  
- **Cabin**: Cabin number (may contain missing values)  
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

---

##  Project Workflow

### 1. Environment Setup
- Open the notebook in [Google Colab](https://colab.research.google.com/)
- Import required libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

### 2. Data Upload
- Use `files.upload()` to upload `tested.csv` from your local machine
- Load the dataset using `pd.read_csv()` and display the first few rows

### 3. Initial Exploration
- Check for missing values using `df.isnull().sum()`
- Understand data types and distributions with `df.describe()` and `df.info()`

### 4. Data Cleaning
- Fill missing `Age` values with the median
- Fill missing `Embarked` values with the mode
- Drop columns like `Cabin`, `Ticket`, `Name`, and `PassengerId` if not useful

### 5. Encoding Categorical Variables
- Convert `Sex` and `Embarked` into numerical format using `LabelEncoder`

### 6. Feature Scaling
- Normalize `Age` and `Fare` using `StandardScaler` to improve model performance

### 7. Train-Test Split
- Separate features (`X`) and target (`y`)
- Split the dataset into training and testing sets using `train_test_split`

### 8. Model Training
- Create and train a `LogisticRegression` model on the training data

### 9. Model Evaluation
- Predict on the test set and calculate accuracy
- Display classification report and confusion matrix
- Visualize the confusion matrix using `seaborn.heatmap`

---

##  Data Visualization

- Plot survival count by gender using `countplot`
- Show age distribution with a histogram
- Compare fare distributions with boxplots
- Analyze survival rates by class and embarkation using bar plots

---

##  Tools & Libraries

- Google Colab  
- Python 3.x  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn

---

##  How to Run

- Open the notebook in Google Colab  
- Upload the `tested.csv` file when prompted  
- Run each cell sequentially to preprocess data, train the model, and visualize results

---

##  Results

The logistic regression model provides a baseline accuracy for survival prediction. You can improve performance by:
- Engineering new features
- Tuning hyperparameters
- Trying advanced models like Random Forest or XGBoost

