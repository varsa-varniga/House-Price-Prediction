import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DATA_PATH = os.path.join(BASE_DIR, "../dataset/clean_data.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "encoder.pkl")

# Ensure model directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)
df = df.dropna()

# Features and target
X = df[['area', 'bhk', 'location']]
y = df['price']

# One-Hot Encode 'location'
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_locations = encoder.fit_transform(df[['location']])

# Combine encoded features
X_encoded = np.concatenate((df[['area', 'bhk']].values, encoded_locations), axis=1)

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# ✅ Save test data for evaluation
joblib.dump(X_test, os.path.join(MODEL_DIR, "X_test.pkl"))
joblib.dump(y_test, os.path.join(MODEL_DIR, "y_test.pkl"))

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, MODEL_PATH)
joblib.dump(encoder, ENCODER_PATH)

print(f"✅ Model saved at: {MODEL_PATH}")
print(f"✅ Encoder saved at: {ENCODER_PATH}")
