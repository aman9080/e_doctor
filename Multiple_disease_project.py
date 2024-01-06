# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""

import pickle
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# loading the saved models

diabetes_model = pickle.load(open(r"C:\Users\hp\Desktop\MDD project\Model\Diabetes.sav", 'rb'))

heart_disease_model = pickle.load(open(r"C:\Users\hp\Desktop\MDD project\Model\Heart.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\hp\Desktop\MDD project\Model\Parkinsons.sav", 'rb'))

stroke_model = pickle.load(open(r"C:\Users\hp\Desktop\MDD project\Model\stroke_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Stroke Prediction'],
                           icons=['activity', 'heart', 'person', 'person'],

                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('CHECK DIABETES PREDICTION USING ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:

        Pregnancies = st.text_input('Pregnancies ')

    with col2:
        Glucose = st.text_input('Glucose Level ')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value ')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value ')

    with col2:
        Insulin = st.text_input('Insulin Level ')

    with col3:
        BMI = st.text_input('BMI value ')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value ')

    with col2:
        Age = st.text_input('Age of the Person ')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #e00;
    color:#00;
    }
</style>""", unsafe_allow_html=True)
    if st.button('CLICK FOR RESULT'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):

            diab_diagnosis = 'The person is Diabetic'
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\diabetes.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.caption(
                'Tips to reduce diabetes -:- Lose extra weight, Be more physically active, Eat healthy plant foods, Eat healthy fats, Skip fad diets and make healthier choices')


        else:
            diab_diagnosis = 'The person is Non Diabetic'
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\non diabetes.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')

            st.balloons()

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.number_input('Sex (1 for Male, 0 for Female)', 0, 1)

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #e00;
    color:#00;
    }
</style>""", unsafe_allow_html=True)

    if st.button('CLICK FOR RESULT'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\heart.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.caption(
                'Tips to reduce Heart disease :-  Eat a healthy balanced diet , Be more physically active (Exercising regularly ) , Give up smoking , Reduce your alcohol consumption , Keep your blood pressure under control , Keep your diabetes under control')


        else:
            heart_diagnosis = 'The person does not have any heart disease'
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\nonheart.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.balloons()
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #e00;
    color:#00;
    }
</style>""", unsafe_allow_html=True)

    if st.button("CLICK FOR RESULT"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\Parkinsons.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.caption(
                ' Tips to reduce Parkinsons Disease :- Go Organic (and Local) , Eat Fresh, Raw Vegetables , Incorporate Omega-3 Fatty Acids Into Your Diet , Vitamin D3 , Drink Green Tea , Regular Aerobic Exercise , Reduce Your Stress')

        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            audio_file = open(r"C:\Users\hp\Desktop\MDD project\nonparkinsons.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')
            st.balloons()
    st.success(parkinsons_diagnosis)

# Stroke disease prediction
if (selected == 'Stroke Prediction'):

    # page title
    st.title('Stroke Disease Prediction using ML')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        gender = st.text_input('Gender')

    with col2:
        age = st.text_input('Age')

    with col3:
        hypertension = st.text_input('Hypertension')

    with col4:
        heart_disease = st.text_input('heart_disease')

    with col1:
        ever_married = st.text_input('ever_married')

    with col2:
        work_type = st.text_input('work_type')

    with col3:
        Residence_type = st.text_input('Residence_type ')

    with col4:
        avg_glucose_level = st.text_input('avg_glucose_level ')

    with col1:
        bmi = st.text_input('bmi')

    with col2:
        smoking_status = st.text_input('smoking_status ')

    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction
    m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #e00;
    color:#e00;
    }
</style>""", unsafe_allow_html=True)

    if st.button('CLICK FOR RESULT'):
        stroke_prediction = stroke_model.predict(
            [[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type,
              avg_glucose_level, bmi, smoking_status]])

        if (stroke_prediction[0] == 1):
            stroke_diagnosis = 'The person is having Stroke disease'
        else:
            stroke_diagnosis = 'The person does not have Stroke disease'

    st.success(stroke_diagnosis)

