import streamlit as st
import pandas as pd
import joblib
import numpy as np


model = joblib.load('diabetes_model_svm.pkl')

# Streamlit 
st.title('Diabetes Prediction')
st.write("""
         This is a simple app that predicts whether a person is diabetic or not based on their medical data.
         """)

# Create input fields for the user to enter data
pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose', min_value=0)
blood_pressure = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.number_input('Age', min_value=0)


if st.button('Predict'):
 
    input_data = np.array([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]).reshape(1, -1)
    

    prediction = model.predict(input_data)
    
    # Show the prediction result
    if prediction[0] == 1:
        st.write("Prediction: Diabetic")
    else:
        st.write("Prediction: Not Diabetic")


    probability = model.predict_proba(input_data)
    st.write(f"Probability of being diabetic: {probability[0][1]:.2f}")
