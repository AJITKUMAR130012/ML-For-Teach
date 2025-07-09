import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


st.title("Placement Prediction App")
cgpa= st.number_input("Enter your CGPA", min_value=0.0, max_value=10.0, step=0.01)
iq = st.number_input("Enter your IQ", min_value=0, max_value=200, step=1)

if st.button("Predict"):
    input_data = np.array([[cgpa, iq]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    
    if prediction[0] == 1:
        st.success("Congratulations! You are likely to get placed.")
    else:
        st.error("Unfortunately, you are not likely to get placed.")