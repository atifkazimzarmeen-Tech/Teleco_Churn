import joblib

model = joblib.load("churn-pipeline-deployment/churn_pipeline_randomforest.joblib")

# Get feature names from preprocessor
preprocessor = model.named_steps['preprocessor']

# Get all feature names
try:
    feature_names = preprocessor.get_feature_names_out()
    print("Features after preprocessing:")
    for name in feature_names:
        print(f"  - {name}")
except:
    pass

# Get input feature names (before preprocessing)
try:
    input_features = preprocessor.feature_names_in_
    print("\nInput columns expected:")
    for name in input_features:
        print(f"  - {name}")
except:
    # Alternative: check the first transformer
    print("\nTrying alternative method...")
    for name, transformer, columns in preprocessor.transformers_:
        print(f"\n{name}: {columns}")