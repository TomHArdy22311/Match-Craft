import streamlit as st

def load_css():

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

    ...
    your CSS
    ...

    </style>
    """, unsafe_allow_html=True)