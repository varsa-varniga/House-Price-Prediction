# House Price Prediction - Frontend

## Overview
This is the frontend of the **House Price Prediction** project, built using **React.js** and **Material-UI**. It allows users to input property details (area, number of bedrooms, and location) and get a predicted house price based on the trained machine learning model hosted in the backend.

## Features
- 📌 User-friendly interface with **Material-UI** design
- 📌 Real-time price prediction by connecting with the **Flask API**
- 📌 **Loading animation** while waiting for predictions
- 📌 **Error handling** for failed predictions
- 📌 Smooth animations using **Framer Motion**

## Tech Stack
- **React.js** - Frontend framework
- **Material-UI** - UI components and styling
- **Axios** - API requests
- **Framer Motion** - Animations

## Project Structure
```
frontend/
├── src/
│   ├── assets/            # Static assets
│   ├── App.css            # Global styles
│   ├── App.jsx            # Main application file
│   ├── index.css          # Additional styles
│   ├── main.jsx           # Entry point
├── public/
│   ├── index.html         # Root HTML file
├── .gitignore
├── eslint.config.js
├── package-lock.json
```

## Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction/frontend
```

### 2️⃣ Install Dependencies
```sh
npm install
```

### 3️⃣ Run the Application
```sh
npm start
```
The app will be available at: **http://localhost:3000/**

## API Integration
The frontend communicates with the backend via **Axios**. Ensure the backend is running at **http://localhost:5000/** before making requests.

```js
const response = await axios.post("http://localhost:5000/predict", {
  area: Number(area),
  bhk: Number(bedrooms),
  location: location,
});
```

## Future Enhancements
🚀 Add Google Maps integration to improve location input.
🚀 Enhance UI with better responsiveness and animations.
🚀 Implement authentication and user profile features.

---
📌 **Author:** Varniga  
📌 **GitHub Repo:** [Your Repo Link Here]  
📌 **Project Dataset:** Chennai House Price Dataset

