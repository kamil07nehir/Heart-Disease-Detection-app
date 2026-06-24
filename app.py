import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Machine Learning Prediction App")

st.write("Enter the values below and click Predict")

# Example inputs (change these according to your model)
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)

if st.button("Predict"):
    features = np.array([[feature1, feature2, feature3, feature4]])

    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]}")
