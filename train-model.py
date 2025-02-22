import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('housing.csv')  # Ensure you have a dataset

# Data Preprocessing
label_encoder = LabelEncoder()
df['ocean_proximity'] = label_encoder.fit_transform(df['ocean_proximity'])

X = df[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms',
        'population', 'households', 'median_income', 'ocean_proximity']]
y = df['median_house_value']

X.fillna(X.mean(), inplace=True)

# Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
os.makedirs('model', exist_ok=True)  # Create 'model' directory if it doesn't exist
with open('model/house_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)  # Save model as a .pkl file

print("Model training complete. Model saved in 'model/house_price_model.pkl'.")
