import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('dating_model.pkl')

st.title("Dating Match Prediction")

# User Inputs
age = st.number_input("Enter Age", min_value=18, max_value=60)

gender = st.selectbox("Gender", [0, 1])

income = st.number_input("Enter Income")

likes = st.number_input("Enter Likes")

profile_completion = st.number_input(
    "Profile Completion",
    min_value=0,
    max_value=100
)

# Predict Button
if st.button("Predict"):

    new_user = np.array([[
        age,
        gender,
        income,
        likes,
        profile_completion
    ]])

    prediction = model.predict(new_user)

    if prediction[0] == 1:
        st.success("Matched!")
    else:
        st.error("Not Matched")