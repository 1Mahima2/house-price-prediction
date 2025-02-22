# House Price Prediction Flask App
# 🏡 House Price Prediction Web Application

This is a Flask-based web application that predicts house prices based on input features such as the number of bedrooms, bathrooms, square footage, and location. The application uses a trained **Machine Learning model** to make predictions.

---

## 🚀 Features
- Web-based interface for predicting house prices.
- User-friendly form to input house details.
- Machine Learning model trained on a housing dataset.
- Built using **Flask, HTML, CSS, JavaScript, and Python**.

---

## 🛠 Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Pickle
- **Deployment**: Localhost (for testing)

---

## 📂 Project Structure
House-Price-Prediction/
│── static/                
│   ├── style.css           # CSS styling
│   ├── script.js           # JavaScript validation
│── templates/              
│   ├── index.html          # Form for user input
│   ├── result.html         # Display predicted price
│── model/                  
│   ├── train_model.py      # Model training script
│   ├── house_price_model.pkl  # Saved model
│── app.py                  # Flask application
│── requirements.txt        # Dependencies
│── README.md               # Documentation

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
