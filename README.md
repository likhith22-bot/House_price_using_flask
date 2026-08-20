# 🏠 House Price Prediction Using Multiple Linear Regression

A machine learning web application that predicts the estimated price of a house based on property details such as bedrooms, bathrooms, living area, lot area, floors, waterfront availability, view, condition, location, construction year, renovation year, and sale date.

The project uses **Multiple Linear Regression** for prediction and provides a user-friendly web interface built with **Flask, HTML, and CSS**.

---

## 🚀 Project Overview

House prices depend on multiple factors such as property size, number of rooms, location, condition, construction year, and other characteristics.

This project uses historical house-price data to train a **Multiple Linear Regression** model and predict the estimated price of a new property.

### Project Workflow

```text
                House Price Dataset
                         │
                         ▼
                Data Preprocessing
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
        Date Processing          City Encoding
             │                       │
       Year/Month/Day            0 - 43
             │                       │
             └───────────┬───────────┘
                         ▼
                  Train/Test Split
                         │
                         ▼
              Multiple Linear Regression
                         │
                         ▼
                    Model Training
                         │
                         ▼
                 Model Evaluation
                    ↙         ↘
                  R²          RMSE
                         │
                         ▼
                  Flask Web App
                         │
                         ▼
                 House Price Prediction
```

---

## 🎯 Objectives

* Build a Multiple Linear Regression model for house-price prediction.
* Perform data preprocessing using Python and Pandas.
* Convert date information into useful numerical features.
* Convert categorical city values into numerical values.
* Split the dataset into training and testing data.
* Train a machine learning regression model.
* Calculate R² score manually.
* Calculate RMSE manually.
* Save the trained model using Pickle.
* Develop a Flask-based web application.
* Provide a simple and attractive interface for users to predict house prices.

---

## 📊 Dataset

The dataset contains historical house/property information.

### Main Features

| Feature         | Description                     |
| --------------- | ------------------------------- |
| `price`         | Target house price              |
| `bedrooms`      | Number of bedrooms              |
| `bathrooms`     | Number of bathrooms             |
| `sqft_living`   | Living area in square feet      |
| `sqft_lot`      | Lot area in square feet         |
| `floors`        | Number of floors                |
| `waterfront`    | Waterfront property indicator   |
| `view`          | View rating                     |
| `condition`     | Property condition              |
| `sqft_above`    | Above-ground area               |
| `sqft_basement` | Basement area                   |
| `yr_built`      | Year the property was built     |
| `yr_renovated`  | Year the property was renovated |
| `city`          | Property city                   |
| `country`       | Country                         |
| `date`          | Date of the house record        |

---

## 🧹 Data Preprocessing

### Date Processing

The original `date` column is converted into a Pandas datetime object.

```python
df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
```

The original `date` column is then removed.

### City Encoding

The dataset contains 44 unique cities.

Each city is mapped to a numerical value from `0` to `43`.

```python
cities = df['city'].unique()

city_map = {}

for i, city in enumerate(cities):
    city_map[city] = i

df['city'] = df['city'].map(city_map)
```

### Country

Since the dataset contains the same country value, it is represented as:

```python
df['country'] = 0
```

---

## 🤖 Machine Learning Model

### Multiple Linear Regression

The project uses **Multiple Linear Regression** because house price depends on multiple independent variables.

The general regression equation is:

```text
Y = b0 + b1X1 + b2X2 + ... + bnXn
```

Where:

* `Y` = predicted house price
* `b0` = intercept
* `b1...bn` = model coefficients
* `X1...Xn` = input features

The model is implemented using:

```python
from sklearn.linear_model import LinearRegression
```

---

## 🔀 Train-Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

using:

```python
train_test_split(
    self.X,
    self.y,
    test_size=0.2,
    random_state=42
)
```

### Random State

`random_state=42` is used to make the train-test split reproducible.

---

## 📈 Model Evaluation

The project evaluates the model using:

### R² Score

R² measures how well the model explains the variation in house prices.

The project also implements the R² calculation manually.

```text
R² = 1 - SSres / SStot
```

Where:

```text
SSres = Σ(actual - predicted)²

SStot = Σ(actual - mean)²
```

### RMSE

Root Mean Squared Error measures the average magnitude of prediction errors.

```text
RMSE = √(Σ(actual - predicted)² / n)
```

The RMSE calculation is also implemented manually using Python loops.

---

## 💾 Model Saving

After training, the model is saved using Pickle:

```python
with open("MLR_Model.pkl", "wb") as t:
    pickle.dump(obj.reg, t)
```

The saved model can then be loaded by the Flask application.

---

## 🌐 Web Application

The project includes a Flask web application.

### User Input

The application allows users to enter:

* Bedrooms
* Bathrooms
* Living area
* Lot area
* Floors
* Waterfront
* View rating
* Condition
* Above-ground area
* Basement area
* Year built
* Year renovated
* City
* Sale date

The application automatically processes:

```text
City → Numerical city value

Date → Year + Month + Day

Country → 0
```

The processed values are passed to the trained machine learning model.

---

## 🖥️ User Interface

The frontend is created using:

* HTML
* CSS
* Flask Jinja Templates

The interface provides:

* Responsive design
* Property detail sections
* Dropdown selections
* Date selection
* Input validation
* Prediction result display
* Mobile-friendly layout

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Multiple Linear Regression

### Data Processing

* Pandas
* NumPy

### Web Development

* Flask
* HTML
* CSS

### Model Serialization

* Pickle

### Development Environment

* PyCharm

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
│
├── main.py
│
├── MLR_Model.pkl
│
├── data (1).csv
│
├── requirements.txt
│
├── README.md
│
└── templates/
    │
    └── index.html
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd House-Price-Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas numpy scikit-learn flask
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000/
```

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
Flask
numpy
pandas
scikit-learn
```

---

## 🔮 Prediction Process

```text
User enters property details
             ↓
       Flask receives data
             ↓
       Data preprocessing
             ↓
      City value mapping
             ↓
      Date feature extraction
             ↓
       Load MLR model
             ↓
       Generate prediction
             ↓
    Display estimated price
```

---

## 📌 Example

### Input

```text
Bedrooms: 3
Bathrooms: 2
Living Area: 1800 sqft
Lot Area: 5000 sqft
Floors: 1
Waterfront: No
View: 2
Condition: 3
Above Area: 1500 sqft
Basement Area: 300 sqft
Year Built: 2005
Year Renovated: 0
City: Seattle
Date: 2014-05-02
```

### Output

```text
Predicted House Price: $XXX,XXX.XX
```

> The predicted value depends on the trained model and the input values.

---

## 📊 Model Performance

Add your final model results here after running the project.

| Metric   |     Training |      Testing |
| -------- | -----------: | -----------: |
| R² Score | `Add Result` | `Add Result` |
| RMSE     | `Add Result` | `Add Result` |

### Current Model

```text
Algorithm: Multiple Linear Regression
Train/Test Split: 80/20
Random State: 42
```

---

## 🔗 Live Deployment

### 🚀 Deployed Application

**Deployment Link:**

> 🔗 **[ADD YOUR DEPLOYMENT LINK HERE]**

Example:

```text
https://your-house-price-app.onrender.com
```

Once the application is deployed, replace the placeholder above with your actual URL.

---

## 🔗 GitHub Repository

**Repository:**

> 🔗 **[ADD YOUR GITHUB REPOSITORY LINK HERE]**

---

## 🔮 Future Improvements

* Use One-Hot Encoding instead of numerical city mapping.
* Implement Gradient Descent from scratch.
* Compare Multiple Linear Regression with other regression algorithms.
* Apply feature scaling.
* Perform feature selection.
* Detect and handle outliers.
* Use cross-validation.
* Add more evaluation metrics.
* Add interactive visualizations.
* Improve the prediction interface.
* Deploy the application online.
* Add a database for storing prediction history.

---

## 👨‍💻 Author

**Likhith Naga Sai Tadikonda**

B.Tech – Computer Science & Engineering

### Skills Used in This Project

```text
Python
Pandas
NumPy
Scikit-learn
Multiple Linear Regression
Flask
HTML
CSS
Git
GitHub
```

---

## ⭐ Project Highlights

* ✅ Multiple Linear Regression
* ✅ Data preprocessing
* ✅ Date feature extraction
* ✅ Categorical data handling
* ✅ Manual R² implementation
* ✅ Manual RMSE implementation
* ✅ Train/Test split
* ✅ Pickle model serialization
* ✅ Flask backend
* ✅ Responsive frontend
* ✅ House price prediction
* ✅ Ready for deployment

---

## 📄 License

This project is created for educational and portfolio purposes.
