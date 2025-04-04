**🏠 House Price Prediction using Machine Learning (Chennai Dataset)**
Welcome to my end-to-end House Price Prediction project! This was an exciting journey where I explored the real-world application of machine learning by predicting house prices in Chennai using the Chennai House Price Dataset from Kaggle.

🚀 Project Overview
This project helped me dive deep into the machine learning workflow—from data preprocessing, model selection, evaluation, to deployment using Flask and frontend integration.

**📌 Highlights:**

Used Linear Regression and Random Forest Regressor to compare performance
Evaluated model using MAE, MSE, RMSE, and R² Score
Integrated Flask backend with a frontend interface
Learned to use OneHotEncoder, joblib, train-test splitting, and more
Explored how to download and prepare real-world datasets from Kaggle
Understood how ML APIs work and how to consume them in the frontend
🔧 Tech Stack
Python (ML model, backend)
scikit-learn (model building and evaluation)
Pandas & NumPy (data handling)
Flask (API framework)
React.js (optional frontend)
Joblib (model persistence)
Jupyter Notebook / VS Code
Kaggle Datasets


**🧠 What I Learned**
The full cycle of ML development from scratch
Training models and saving them with joblib
Measuring and comparing model performance with different metrics
Creating REST API endpoints using Flask
Connecting the backend to a React frontend
Organizing and structuring ML projects properly
Importance of data preprocessing and encoding categorical features
📊 Model Comparison
Metric	Linear Regression	Random Forest
MAE	14.37 Lakhs	10.65 Lakhs
MSE	778.18	584.11
RMSE	27.90 Lakhs	24.17 Lakhs
R² Score	0.80	0.85
✅ As shown, Random Forest Regressor performs significantly better than Linear Regression in this context.

**📂 Project Structure**
House-Price-Prediction/ ├── backend/ │ ├── pycache/ │ │ ├── app.cpython-313.pyc │ ├── model/ │ │ ├── encoder.pkl │ │ ├── model.pkl │ │ ├── X_test.pkl │ │ ├── y_test.pkl │ ├── .gitignore │ ├── app.py # Flask API │ ├── evaluate.py # Model evaluation │ ├── README.md │ ├── requirements.txt # Dependencies │ ├── Test_model.py # Model testing script │ ├── train_model.py # Model training script │ ├── dataset/ │ ├── clean_data.csv # Preprocessed dataset │ ├── frontend/ │ ├── node_modules/ │ ├── public/ │ ├── src/ │ │ ├── assets/ # Static assets │ │ ├── App.css │ │ ├── App.jsx │ │ ├── index.css │ │ ├── main.jsx │ ├── .gitignore │ ├── eslint.config.js │ ├── index.html # Main HTML file │ ├── package-lock.json

**📌 How to Run**
1. Clone the Repo
git clone https://github.com/varsa-varniga/house-price-prediction.git
cd house-price-prediction/backend
2. Create & Activate Virtual Environment
    python -m venv venv
    venv\Scripts\activate       # On Windows
    # or

   
    source venv/bin/activate    # On Mac/Linux
4. Install Requirements
    pip install -r requirements.txt
5. Train the Model
    python train_model.py
6. Run Flask API
    python app.py
7. Frontend (Optional)
    Open the React app in a browser (http://localhost:5174 or wherever it runs).


**📈 Sample Output**
Input:
area = 1000 sqft
bhk = 2
location = Ambattur

✅ Predicted House Price: ₹47.5 Lakhs
