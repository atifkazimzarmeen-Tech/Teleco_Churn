# Teleco_Churn

Customer Churn Prediction with ML Pipeline
https://python.org
https://scikit-learn.org
https://flask.palletsprojects.com
End-to-end machine learning pipeline for predicting customer churn in telecom industry.

📊 Project Overview

Table
Copy
Metric	Value
Model	Random Forest Classifier
Accuracy	93.45%
F1 Score	75.52%
ROC-AUC	87.58%


Dataset	Telecom Churn (2,666 customers)
🎯 Features

✅ Production-ready ML Pipeline (scikit-learn Pipeline API)
✅ Automated Preprocessing (imputation, scaling, encoding)
✅ Hyperparameter Tuning (GridSearchCV)
✅ Web Interface (Flask + HTML/CSS/JS)
✅ Batch Predictions (CSV upload)
✅ Risk Analysis (High/Medium/Low classification)
🏗️ Project Structure

churn-prediction/
├── app.py                          # Flask backend
├── churn_pipeline_randomforest.joblib  # Trained model
├── requirements.txt                # Dependencies
├── templates/
│   └── index.html                  # Web interface
├── static/
│   ├── style.css                   # Styling
│   └── script.js                   # Frontend logic
├── test_customers.csv              # Sample data
└── README.md
                      
1. Clone Repository

bash
git clone https://github.com/yourusername/churn-prediction.git
cd churn-prediction

2. Install Dependencies

bash
pip install -r requirements.txt

3. Run Application
bash
python app.py

4. Open Browser
Navigate to http://localhost:5000

📈 Model Performance
Classification Report
              precision    recall  f1-score   support

    No Churn       0.95      0.98      0.96       456
       Churn       0.83      0.69      0.75        78

    accuracy                           0.93       534
   macro avg       0.89      0.83      0.86       534
weighted avg       0.93      0.93      0.93       534
Key Insights
High Precision for No Churn: 95% (few false alarms)
Good Churn Detection: 83% precision, 69% recall
Balanced Model: Handles class imbalance well

🔧 Pipeline Architecture
Raw Data
    ↓
[ColumnTransformer]
    ├── Numeric Pipeline: SimpleImputer → StandardScaler
    └── Categorical Pipeline: SimpleImputer → OneHotEncoder
    ↓
[Random Forest Classifier]
    ↓
Prediction + Probability

🌐 Web Interface Features
Feature	Description
Real-time Prediction	Single customer churn risk
Batch Upload	CSV file with multiple customers
Risk Scoring	High/Medium/Low classification
Probability Bars	Visual confidence indicators
Key Insights	Automated recommendations

📋 Input Features
Category	Features
Demographics	State, Account Length, Area Code
Plans	International Plan, Voice Mail Plan
Usage	Day/Evening/Night/Intl minutes, calls, charges
Support	Customer Service Calls

💾 Model Persistence
Saved with joblib for production deployment:
Python

import joblib

# Load pipeline
model = joblib.load('churn_pipeline_randomforest.joblib')

# Predict
prediction = model.predict(new_customer_data)
probability = model.predict_proba(new_customer_data)

🛠️ Technologies Used
Category	Tools
ML Framework	scikit-learn
Web Framework	Flask
Frontend	HTML5, CSS3, JavaScript
Visualization	Plotly (optional)
Deployment	joblib, Werkzeug

📊 Dataset
Source: Telecom Churn Dataset (BigML)
Samples: 2,666 customers
Features: 19 input features
Target: Churn (Yes/No)
Class Distribution: 85% No Churn, 15% Churn

🎯 Business Impact
Metric	Value
Cost to Acquire	$200-500 per customer
Cost to Retain	$10-50 per customer
Retention ROI	5-10x savings
Use Case: Identify at-risk customers for targeted retention campaigns.

📝 Sample Prediction
JSON
{
  "prediction": "Churn",
  "churn_probability": 85.5,
  "risk_level": "High",
  "confidence": 85.5
}
🔮 Future Improvements
[ ] SMOTE for class imbalance
[ ] Feature importance visualization
[ ] A/B testing framework
[ ] Docker containerization
[ ] Cloud deployment (AWS/GCP)
