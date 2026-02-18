# Churn Prediction Pipeline

## Model: RandomForest

### Performance
- Accuracy: 0.9345
- F1 Score: 0.7552
- ROC-AUC: 0.8758

### Files
- churn_pipeline_randomforest.joblib: Trained pipeline
- confusion_matrix_RandomForest.png: Evaluation visualization
- inference_example.py: Usage example

### Usage
```python
import joblib
import pandas as pd

model = joblib.load("churn_pipeline_randomforest.joblib")
prediction = model.predict(new_data)
```