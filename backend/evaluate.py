import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoder.pkl")
X_TEST_PATH = os.path.join(MODEL_DIR, "X_test.pkl")
Y_TEST_PATH = os.path.join(MODEL_DIR, "y_test.pkl")

# Load the trained model, encoder, and test data
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)
X_test = joblib.load(X_TEST_PATH)
y_test = joblib.load(Y_TEST_PATH)

print("✅ Model, encoder, and test data loaded successfully!")

# Predict on test data
y_pred = model.predict(X_test)

# Evaluation Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print the results
print("\n📊 Model Evaluation on Test Set:")
print(f"📌 Mean Absolute Error (MAE): {mae:.2f} Lakhs")
print(f"📌 Mean Squared Error (MSE): {mse:.2f}")
print(f"📌 Root Mean Squared Error (RMSE): {rmse:.2f} Lakhs")
print(f"✅ R² Score (Accuracy-like): {r2:.2f}")
