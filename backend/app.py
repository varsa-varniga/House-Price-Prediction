import os
import joblib
import logging
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (Configure properly in production)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow all for now, restrict in production

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load trained model and encoder
MODEL_PATH = "model/model.pkl"
ENCODER_PATH = "model/encoder.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
    raise FileNotFoundError("🚨 Model or Encoder file not found! Train the model first.")

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

logging.info("✅ Model and encoder loaded successfully.")

# API endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        logging.info(f"📩 Received request data: {data}")

        # Validate input fields
        required_fields = {'area', 'bhk', 'location'}
        if not required_fields.issubset(data.keys()):
            missing = required_fields - data.keys()
            return jsonify({"error": f"❌ Missing key(s): {', '.join(missing)}"}), 400

        # Convert to correct data types
        area = float(data['area'])
        bhk = int(data['bhk'])
        location = str(data['location'])

        # One-hot encode 'location' (handle unknown locations)
        location_encoded = encoder.transform([[location]])

        # Create final feature array
        input_features = [[area, bhk] + list(location_encoded[0])]

        # Make the prediction
        prediction = model.predict(input_features)

        return jsonify({'predicted_price': round(prediction[0], 2)})

    except ValueError as e:
        logging.error(f"❌ ValueError: {e}")
        return jsonify({"error": "Invalid input type. Ensure numbers are correctly formatted."}), 400
    except Exception as e:
        logging.error(f"🔥 Error during prediction: {e}")
        return jsonify({"error": "Error during prediction", "message": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
