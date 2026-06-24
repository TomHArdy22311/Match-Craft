import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Relationship Risk Analyzer",
    page_icon="🚩",
    layout="centered"
)

# -----------------------------------
# Common CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

h1{
    text-align:center;
    color:#ff4b91;
    font-size:42px;
}

.stButton > button{
    background-color:#ff4b91;
    color:white;
    border-radius:12px;
    height:3em;
    width:100%;
    font-size:18px;
    border:none;
}

.stButton > button:hover{
    background-color:#ff77c6;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Home Page
# -----------------------------------

# -----------------------------------
# Home Page
# -----------------------------------

st.title("🚩 Relationship Risk Analyzer")

st.write("Built for people who say **'I can fix them.'**")

st.divider()

st.subheader("💘 Welcome to the worst idea you'll have today")

st.write("""
This application uses Machine Learning to estimate
your relationship compatibility.

⚠️ Disclaimer: The AI is smart, but your dating decisions might not be.

### What this app does

- 💕 Predicts your chances of finding a match
- 📊 Analyzes relationship statistics
- 🚩 Detects potential emotional damage
- 🧠 Uses Machine Learning instead of your best friend's advice

### Things to remember

- Don't get your hopes too high.
- Don't blame the algorithm.
- Please don't change your entire personality for a prediction.
- Results may cause existential crises.

👉 Click **Prediction** from the sidebar to begin.
""")

st.info(
    "📌 Fun Fact: 87% of bad decisions started with 'Trust me bro.'"
)

st.warning(
    "💬 This app predicts compatibility, not whether they'll leave you on read."
)

st.success(
    "🫡 Good luck. You're going to need it."
)

st.divider()

st.subheader("⚠️ Legal Notice")

st.caption(
    "The developers are not responsible for emotional damage, ghosting, heartbreak, trust issues, or playlist depression."
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