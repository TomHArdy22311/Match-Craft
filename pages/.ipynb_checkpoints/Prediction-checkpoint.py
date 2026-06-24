
import streamlit as st
import joblib
import numpy as np
import random

# -----------------------------------
# Load Model
# -----------------------------------

model = joblib.load("dating_model.pkl")

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Prediction",
    page_icon="🚩",
    layout="centered"
)

# -----------------------------------
# CSS
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

st.write("AI Compatibility Prediction")

st.caption("⚠️ Proceed at your own emotional risk.")

st.divider()

# -----------------------------------
# Funny Messages
# -----------------------------------

male_success = [

    "👑 King, somebody might finally text back.",

    "🌙 Chances are you're talking till 3 a.m.",

    "📱 She's replying in under 10 seconds.",

    "💘 Operation 'I can fix her' has begun.",

    "🎉 Bro escaped the friend zone.",

    "🥳 Good news. You're not getting ghosted today."

]

male_failure = [

    "🏋️ Congratulations. A gym membership has been unlocked.",

    "💼 Focus on your career, bro.",

    "📚 Your books need you more.",

    "🎮 Side quest unlocked: self-improvement.",

    "🙏 Pray to God at this point.",

    "📱 Even the algorithm left you on read."

]

female_success = [

    "💅 Queen energy detected.",

    "💖 Somebody may finally deserve your attention.",

    "✨ Green flags spotted. That's rare.",

    "📱 Expect random good morning texts.",

    "🥰 This one might actually know how to communicate.",

    "☕ Coffee date probability increased."

]

female_failure = [

    "💀 Even Snapchat couldn't save this one.",

    "🚩 Red flag collector achievement unlocked.",

    "☕ Maybe stop saying 'I can fix him.'",

    "🧠 The AI saw something your heart didn't.",

    "💅 Queen, this one's a hard pass.",

    "☠️ This wasn't a match. This was a warning."

]

# -----------------------------------
# Inputs
# -----------------------------------

age = st.slider("Age",18,60,25)

gender = st.selectbox(
    "Gender",
    ["Female","Male"]
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

pet_preference = st.selectbox(
    "Pet Preference 🐾",
    ["Dogs","Cats","Both","None"]
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
# Encoding
# -----------------------------------

gender = 1 if gender == "Male" else 0

if likes < 50:

    engagement_level_num = 0
    engagement_level = "Low"

elif likes < 120:

    engagement_level_num = 1
    engagement_level = "Medium"

else:

    engagement_level_num = 2
    engagement_level = "High"

pet_mapping = {

    "Both":0,
    "Cats":1,
    "Dogs":2,
    "None":3

}

music_mapping = {

    "Classical":0,
    "Lo-fi":1,
    "Phonk":2,
    "Pop":3,
    "Rap":4,
    "Rock":5,
    "Sad Songs":6

}

relationship_mapping = {

    "Figuring out my dating goals":0,
    "Monogamy":1,
    "Non-monogamy":2

}

pet_preference_encoded = pet_mapping[
    pet_preference
]

music_taste_encoded = music_mapping[
    music_taste
]

relationship_type_encoded = relationship_mapping[
    relationship_type
]

# -----------------------------------
# Feature Engineering
# -----------------------------------

attractiveness_index = (

    (likes * 0.5)

    + (profile_completion * 0.3)

    + ((income / 1000) * 0.2)

)

user_influence_score = (

    (likes * 0.7)

    + (profile_completion * 0.3)

)

# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button("Analyze Relationship Risk 🚨"):

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

    prediction = model.predict(new_user)

    st.divider()

    st.subheader("📊 Relationship Analytics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Engagement Level",
            engagement_level
        )

    with col2:

        st.metric(
            "Attractiveness Index",
            round(attractiveness_index,2)
        )

    with col3:

        st.metric(
            "Influence Score",
            round(user_influence_score,2)
        )

    st.divider()

    st.subheader("🤖 AI Relationship Analysis")

    # MATCH

    if prediction[0] == 1:

        if gender == 1:

            st.success(
                random.choice(male_success)
            )

        else:

            st.success(
                random.choice(female_success)
            )

        st.balloons()

        st.progress(90)

        st.metric(
            "Relationship Survival Chance",
            "87%"
        )

        if gender == 1:

            st.info(
                "🌙 High probability of talking till 3 a.m., king."
            )

            st.write("### Possible side effects")

            st.write("""
❤️ Excessive use of heart emojis

📱 Checking messages every 5 minutes

🎵 Making playlists together

☕ Unnecessary coffee dates

😴 Losing sleep every night
""")

        else:

            st.info(
                "💖 High probability of receiving random good morning texts."
            )

            st.write("### Possible side effects")

            st.write("""
✨ Excessive use of sparkles

📸 Random selfies

☕ Coffee date planning

🎵 Sharing playlists

😴 Sleeping later than usual
""")

    # NO MATCH

    else:

        if gender == 1:

            st.error(
                random.choice(male_failure)
            )

        else:

            st.error(
                random.choice(female_failure)
            )

        st.progress(25)

        st.metric(
            "Emotional Damage Probability",
            "96%"
        )

        if gender == 1:

            st.write("### AI Recovery Plan")

            st.write("""
🏋️ Hit the gym

💼 Build your career

📚 Study instead

🎮 Side quest: self-improvement

🚫 Don't text 'Hey' at 2 a.m.
""")

        else:

            st.write("### AI Recovery Plan")

            st.write("""
💅 Focus on yourself

☕ Drink some coffee

📚 Build your main character arc

🛍️ Buy yourself something nice

🚩 Stop collecting red flags
""")

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("⚠️ Disclaimer")

st.sidebar.info(
'''
This model predicts compatibility,
not emotional stability.

Side effects may include:

- attachment issues
- trust problems
- playlist depression
- texting first every time
'''
)

st.sidebar.success(
    "Powered by Machine Learning & questionable choices."
)
