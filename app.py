import streamlit as st
import joblib
import numpy as np

# -----------------------------------
# Load Trained Model
# -----------------------------------

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

/* Title */
h1 {
    text-align: center;
    color: #ff4b91;
    font-size: 42px;
}

/* Buttons */
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

/* Select Box Text */
div[data-baseweb="select"] {
    color: black;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.1);
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
# New Features
# -----------------------------------

pet_preference = st.selectbox(
    "Pet Preference 🐾",
    [
        "Dogs",
        "Cats",
        "Both",
        "None"
    ]
)

music_taste = st.selectbox(
    "Music Taste 🎵",
    [
        "Pop",
        "Rock",
        "Rap",
        "Lo-fi",
        "Classical",
        "Sad Songs",
        "Phonk"
    ]
)

relationship_type = st.selectbox(
    "Relationship Goals ❤️",
    [
        "Monogamy",
        "Non-monogamy",
        "Figuring out my dating goals"
    ]
)

st.divider()

# -----------------------------------
# Manual Label Encoding
# -----------------------------------

# Gender Encoding
gender = 1 if gender == "Male" else 0

# Engagement Level Encoding
if likes < 50:
    engagement_level_num = 0
    engagement_level = "Low"

elif likes < 120:
    engagement_level_num = 1
    engagement_level = "Medium"

else:
    engagement_level_num = 2
    engagement_level = "High"

# Pet Preference Encoding
pet_mapping = {
    "Both": 0,
    "Cats": 1,
    "Dogs": 2,
    "None": 3
}

pet_preference_encoded = pet_mapping[pet_preference]

# Music Taste Encoding
music_mapping = {
    "Classical": 0,
    "Lo-fi": 1,
    "Phonk": 2,
    "Pop": 3,
    "Rap": 4,
    "Rock": 5,
    "Sad Songs": 6
}

music_taste_encoded = music_mapping[music_taste]

# Relationship Type Encoding
relationship_mapping = {
    "Figuring out my dating goals": 0,
    "Monogamy": 1,
    "Non-monogamy": 2
}

relationship_type_encoded = relationship_mapping[
    relationship_type
]

# -----------------------------------
# Feature Engineering
# -----------------------------------

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

    # Model Input
    new_user = np.array([[
        age,
        gender,
        income,
        likes,
        profile_completion,
        engagement_level_num,
        attractiveness_index,
        user_influence_score,
        pet_preference_encoded,
        music_taste_encoded,
        relationship_type_encoded
    ]])

    # Prediction
    prediction = model.predict(new_user)

    st.divider()

    # -----------------------------------
    # Generated Metrics
    # -----------------------------------

    st.subheader("Relationship Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Engagement Level",
            engagement_level
        )

    with col2:
        st.metric(
            "Attractiveness Index",
            round(attractiveness_index, 2)
        )

    with col3:
        st.metric(
            "Influence Score",
            round(user_influence_score, 2)
        )

    st.divider()

    # -----------------------------------
    # Prediction Result
    # -----------------------------------

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