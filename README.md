<!-- # Logistic_Regression

<img width="881" height="875" alt="image" src="https://github.com/user-attachments/assets/be39e4d3-bf58-4846-a59f-4438c8c8862c" /> -->


## Logistic Regression – Binary Classification Predictor

This project implements a Logistic Regression model using a Flask-based web app. It predicts binary outcomes (e.g., Pass/Fail, Yes/No) based on user input features such as hours studied, attendance, and other relevant metrics.

---

## What is Logistic Regression?

Logistic Regression is a supervised classification algorithm used when the dependent variable is binary (i.e., two possible outcomes). It estimates the probability that an instance belongs to a particular class using the logistic (sigmoid) function.

---
## Model Used
- LogisticRegression from scikit-learn

- Model trained on student performance data

- Binary target encoded using label encoding

- Serialized with joblib


##  Project Structure
```
Logistic_Regression/
├── app.py               # Flask app
├── train_model.py       # Model training script
├── student_data.csv     # Dataset file
├── model.pkl            # Trained model
├── pass_map.pkl         # Target encoding map
│
├── templates/
│   └── index.html       # Web interface
└── README.md            # Project documentation



```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Logistic_Regression.git
cd Logistic_Regression

```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:10000

---
## Screenshots
<img width="881" height="875" alt="image" src="https://github.com/user-attachments/assets/be39e4d3-bf58-4846-a59f-4438c8c8862c" /> 

---
## Future Improvements
Add visualizations for data distribution

Support multi-class classification

Add export to CSV for user predictions

