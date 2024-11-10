from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Load the trained model
model = joblib.load('heart_risk_model.pkl')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data from JSON
        data = request.json
        age = data.get('age')
        sex = 1 if data.get('sex').lower() == 'male' else 0  # Convert to numerical
        cp = data.get('cp')
        trestbps = data.get('trestbps')
        chol = data.get('chol')

        # Validate input
        if None in [age, sex, cp, trestbps, chol]:
            return jsonify({"error": "Missing data"}), 400

        # Prepare the data in the required format
        input_data = np.array([[age, sex, cp, trestbps, chol]])

        # Make prediction
        prediction = model.predict(input_data)
        risk_level = "High Risk" if prediction[0] == 1 else "Low Risk"

        # Return the prediction as JSON
        return jsonify({"risk_level": risk_level})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
