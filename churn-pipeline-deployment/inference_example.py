
import joblib
import pandas as pd

# Load pipeline
model = joblib.load("churn_pipeline_randomforest.joblib")

# Example customer
new_customer = pd.DataFrame([{
    # Fill with actual column names and sample values from your dataset
}])

prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)

print(f"Churn: {'Yes' if prediction[0] == 1 else 'No'}")
print(f"Probability: {probability[0][1]:.2%}")
