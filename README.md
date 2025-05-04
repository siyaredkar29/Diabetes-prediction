 Diabetes Prediction App (Streamlit)

[Click here to try the live app!](https://diebetes-prediction-4schsux59xjivszv7cb2wb.streamlit.app/)

This project is a simple web application built using Streamlit that predicts whether a person is diabetic or not based on their medical data. The machine learning model used is an SVM (Support Vector Machine) classifier trained on the popular Pima Indians Diabetes dataset.


 Features

- User-friendly web interface for inputting health data
- Predicts diabetic or non-diabetic status using a trained model
- Displays probability of being diabetic
- Built with Python, Streamlit, and scikit-learn


---

 How It Works

1. Input Features:
   - Pregnancies
   - Glucose
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI
   - Diabetes Pedigree Function
   - Age

2. Prediction Logic:
   - The input values are passed to a trained Support Vector Machine (SVM) model.
   - The model predicts if the person is diabetic (`1`) or not (`0`).
   - Also shows the probability of being diabetic using `predict_proba()`.




