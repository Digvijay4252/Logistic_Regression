import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("logistic_student_data.csv")

# Encode target variable
le = LabelEncoder()
data['Pass_encoded'] = le.fit_transform(data['Pass'])  # Yes = 1, No = 0

# Features and label
X = data[['Hours_Studied', 'Attendance', 'Assignments_Completed', 'Sleep_Hours']]
y = data['Pass_encoded']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and label encoder
joblib.dump(model, 'model.pkl')
joblib.dump(le, 'label_encoder.pkl')

print("Logistic Regression model trained and saved successfully.")
