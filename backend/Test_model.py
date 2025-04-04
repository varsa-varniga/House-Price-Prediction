import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/model.pkl")
print("✅ Model loaded successfully!")

# Sample input - Replace this with actual user inputs
area = 1000  # Example: User enters 1000 sqft
bhk = 2  # Example: User enters 2 BHK
location = "Ambattur"  # Example: User selects "Ambattur"

# Load the encoder (Ensure you saved it during training)
encoder = joblib.load("model/encoder.pkl")  # Path to the saved OneHotEncoder
location_encoded = encoder.transform([[location]])  # No .toarray()

input_features = np.hstack([np.array([area, bhk]), location_encoded.flatten()])


# Predict price
predicted_price = model.predict([input_features])[0]

print(f"🏠 Predicted House Price: {predicted_price:.2f} Lakhs")
