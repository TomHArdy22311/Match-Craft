import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("dating_model.pkl")

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Relationship Risk Analyzer",
    page_icon="🚩",
    layout="centered"
)

# -----------------------------------
# Custom CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

h1 {
    text-align: center;
    color: #ff4b91;
    font-size: 42px;
}

.stButton > button {
    background-color: #ff4b91;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #ff77c6;
    transform: scale(1.02);
}

div[data-baseweb="select"] {
    color: black;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Title
# -----------------------------------

st.title("🚩 Relationship Risk Analyzer")

st.write("Built for people who say 'I can fix them'.")

st.divider()

# -----------------------------------
# User Inputs
# -----------------------------------

age = st.slider(
    "Age",
    18,
    60,
    25
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

income = st.number_input(
    "Income",
    min_value=0,
    value=50000
)

likes = st.slider(
    "Likes",
    0,
    500,
    100
)

profile_completion = st.slider(
    "Profile Completion %",
    0,
    100,
    75
)

# -----------------------------------
# Convert Gender
# -----------------------------------

gender = 1 if gender == "Male" else 0

# -----------------------------------
# Feature Engineering
# -----------------------------------

# Engagement Level
if likes < 50:
    engagement_level = 0
elif likes < 120:
    engagement_level = 1
else:
    engagement_level = 2

# Attractiveness Index
attractiveness_index = (
    (likes * 0.5) +
    (profile_completion * 0.3) +
    ((income / 1000) * 0.2)
)

# User Influence Score
user_influence_score = (
    (likes * 0.7) +
    (profile_completion * 0.3)
)

# -----------------------------------
# Predict Button
# -----------------------------------

if st.button("Analyze Relationship Risk 🚨"):

    new_user = np.array([[
        age,
        gender,
        income,
        likes,
        profile_completion,
        engagement_level,
        attractiveness_index,
        user_influence_score
    ]])

    prediction = model.predict(new_user)

    st.divider()

    st.subheader("AI Relationship Analysis")

    if prediction[0] == 1:

        st.success(
            "💘 Congratulations. Red flags ignored successfully."
        )

        st.balloons()

        st.progress(90)

        st.metric(
            label="Relationship Survival Chance",
            value="87%"
        )

        st.info(
            "AI predicts a dangerously high chance "
            "of replying 'good morning ❤️' every day."
        )

    else:

        st.error(
            "💀 Even the algorithm said no."
        )

        st.progress(25)

        st.metric(
            label="Emotional Damage Probability",
            value="96%"
        )

        st.warning(
            "Recommended action: focus on career development."
        )

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("⚠️ Disclaimer")

st.sidebar.info(
    """
    This model predicts compatibility,
    not emotional stability.

    Side effects may include:
    - attachment issues
    - trust problems
    - playlist depression
    - texting first every time
    """
)

st.sidebar.success(
    "Powered by Machine Learning & questionable choices."
)