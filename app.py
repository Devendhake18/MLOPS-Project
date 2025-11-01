# app.py
import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
model_path = os.path.join("models", "rf_food_waste_model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return "Food Waste Prediction API is running."

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        json_data = request.get_json()
        
        # Convert JSON to DataFrame
        # Assumes input JSON is a single record or a list of records
        df = pd.DataFrame(json_data)
        
        # CRITICAL: Ensure the columns are in the *exact* order
        # as the training data.
        # You must modify your pipeline to save the feature names
        # and encoders.
        
        # Example feature list (you MUST verify this)
        # This list is based on your params.yaml and scripts.
        # It assumes 'date' and 'city' are label-encoded.
        features = [
            'restaurant_id', 'city', 'date', 'sales', 'temperature', 
            'rainfall', 'num_events', 'is_holiday', 'day_of_week'
        ]
        
        # Reorder columns to match model's expectation
        X = df[features]

        # Make prediction
        prediction = model.predict(X)
        
        return jsonify({"prediction": list(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))