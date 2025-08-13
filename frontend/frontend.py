import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Prediction", page_icon="💉")

st.title("Diabetes Prediction App")
st.write("Enter patient details below:")

# Input fields
Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
Glucose = st.number_input("Glucose", min_value=0.0, max_value=300.0, value=120.0)
BloodPressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
SkinThickness = st.number_input("Skin Thickness", min_value=0.0, max_value=100.0, value=20.0)
Insulin = st.number_input("Insulin", min_value=0.0, max_value=900.0, value=85.0)
BMI = st.number_input("BMI", min_value=0.0, max_value=100.0, value=33.6)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.35)
Age = st.number_input("Age", min_value=0, max_value=120, value=29)

# Button
if st.button("Predict"):
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }
    
    # Call the backend API
    url = "https://diabetes-prediction-api-frontend.onrender.com/predict"
    response = requests.post(url, json=input_data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['result']}")
        st.info(f"Confidence: {result['confidence']}")
    else:
        st.error("Error contacting API. Please try again.")

