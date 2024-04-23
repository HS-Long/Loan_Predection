import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('finalized_model.sav', 'rb'))

# Create input fields
st.markdown("<h1 style='text-align: center;'>🏦 Loan Prediction App By Team-6</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Please enter the following information:</p>", unsafe_allow_html=True)

# Input fields
st.write('Enter applicant details:')
gender = st.selectbox('👨‍🦲 Gender', ['Male', 'Female'])
married = st.selectbox('💍 Married', ['Yes', 'No'])
dependents = st.selectbox('👨‍👩‍👦 Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('🎓 Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('💼 Self Employed', ['Yes', 'No'])
loan_amount = st.number_input('💰 Loan Amount')
loan_amount_term = st.number_input('⏰ Loan Amount Term')
credit_history = st.selectbox('💳 Credit History', ['1.0', '0.0'])
property_area = st.selectbox('🏘️ Property Area', ['Urban', 'Semiurban', 'Rural'])
total_income = st.number_input('💵 Total Income')

# Convert categorical variables
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Yes' else 0
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
property_area = {'Urban': 1, 'Rural': 0, 'Semiurban': 2}[property_area]
dependents = {'0': 0, '1': 1, '2': 2, '3+': 3}[dependents]
credit_history = 1 if credit_history == '1.0' else 0

# Calculate total_income_log
total_income_log = np.log(total_income) if total_income > 0 else 0

# Create a button to predict
if st.button('Predict'):
    # Create a dataframe from the inputs
    data = {
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area],
        'total_income_log': [total_income_log]
    }
    df = pd.DataFrame(data)

    # Use the model to predict
    prediction = model.predict(df)

    # Display the prediction
    if prediction == 1:
        st.write('🎉 Loan Approved')
    else:
        st.write('❌ Loan Rejected')
