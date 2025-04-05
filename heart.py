import streamlit as st
import joblib
st.title('Heart Disease Prediction')
model=joblib.load('archive.joblib')
Age=st.number_input('Enter age')
Gender=st.number_input('Enter gender male:0 ,female:1')
Cholesterol=st.number_input('Enter cholesterol')
BloodPressure=st.number_input('Enter Blood Pressure')
Smoking=st.number_input('Enter smoking Never:0 , Current:1')
AlcoholIntake=st.number_input('Enter Alocohol Intake Heavy:1 ,NaN:0, Moderate:0.5')
ExerciseHours=st.number_input('Enter Exercise Hours')
FamilyHistory=st.number_input('Enter Family History yes:1, No:0')
Diabetes=st.number_input('Enter Diabetes yes:1, No:0')
Obesity=st.number_input('Enter Obesity yes:1, No:0')
StressLevel=st.number_input('Enter Stress Level')
BloodSugar=st.number_input('Enter Blood Sugar')
ExerciseInducedAngina=st.number_input('Enter Exercise Induced Angina yes:1, No:0')
ChestPain=st.number_input('Enter Chest pain Atypical Angina:0,Typical Angina:1,Non-anginal Pain:2,Asymptomatic:3')
if st.button('predict Approval'):
    prediction=model.predict([[Age,Gender,Cholesterol,BloodPressure,Smoking,AlcoholIntake,ExerciseHours,Diabetes,Obesity,StressLevel,BloodSugar,ExerciseInducedAngina,ChestPain]])
    if prediction=='Y':
        st.text('Yes')
    else:
        st.text('No')
