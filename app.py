from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "churn-pipeline-deployment/churn_pipeline_randomforest.joblib"

try:
    model = joblib.load(MODEL_PATH)
    model_loaded = True
    print("✅ Model loaded successfully")
except Exception as e:
    model_loaded = False
    print(f"❌ Error loading model: {e}")

# Exact columns from your model
FEATURES = {
    'numeric': [
        'Account length',
        'Area code',
        'Number vmail messages',
        'Total day minutes',
        'Total day calls',
        'Total day charge',
        'Total eve minutes',
        'Total eve calls',
        'Total eve charge',
        'Total night minutes',
        'Total night calls',
        'Total night charge',
        'Total intl minutes',
        'Total intl calls',
        'Total intl charge',
        'Customer service calls'
    ],
    'categorical': {
        'State': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
        'International plan': ['No', 'Yes'],
        'Voice mail plan': ['No', 'Yes']
    }
}

@app.route('/')
def index():
    return render_template('index.html', features=FEATURES, model_loaded=model_loaded)

@app.route('/predict', methods=['POST'])
def predict():
    if not model_loaded:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        # Get form data
        data = {}
        
        # Numeric fields - convert to float/int
        for field in FEATURES['numeric']:
            value = request.form.get(field, '0')
            # Area code and Account length should be int, others float
            if field in ['Area code', 'Account length', 'Number vmail messages', 'Total day calls', 'Total eve calls', 'Total night calls', 'Total intl calls', 'Customer service calls']:
                data[field] = int(float(value))
            else:
                data[field] = float(value)
        
        # Categorical fields
        for field in FEATURES['categorical'].keys():
            data[field] = request.form.get(field, '')
        
        # Create DataFrame with EXACT column order
        input_df = pd.DataFrame([data])
        
        # Ensure column order matches training
        all_columns = FEATURES['numeric'] + list(FEATURES['categorical'].keys())
        input_df = input_df[all_columns]
        
        # Predict
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]
        
        churn_prob = probability[1]
        no_churn_prob = probability[0]
        
        result = {
            'prediction': 'Churn' if prediction == 1 else 'No Churn',
            'churn_probability': round(churn_prob * 100, 2),
            'no_churn_probability': round(no_churn_prob * 100, 2),
            'risk_level': 'High' if churn_prob > 0.7 else 'Medium' if churn_prob > 0.3 else 'Low',
            'confidence': round(max(churn_prob, no_churn_prob) * 100, 2)
        }
        
        return jsonify(result)
    
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)