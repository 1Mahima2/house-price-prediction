import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load trained model from 'house_price_model.pkl'
with open('model/house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array(features).reshape(1, -1)
    prediction = model.predict(final_features)
    return render_template('result.html', prediction_text=f'Estimated House Price: ${prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
