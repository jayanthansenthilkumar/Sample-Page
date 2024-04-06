import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_icon='papu.png',
    page_title='Swetha Minor Project',
    layout="wide",
    initial_sidebar_state="expanded",
)
def main_page():
    st.header("Drug Analysis on Ayurveda for Practitioners")
    st.text_input("Name")
    st.text_input("Contact Number")
    st.text_input("Address (For Contact Purpose alone)")
    st.file_uploader("Aadhar Card (For age purpose alone)")
    st.file_uploader("College ID Card (For Clarification)")
    st.camera_input("Your Photo (Confirming That's You)")
    st.text("I am Declaring the above given details are True and verified by myself")
    st.file_uploader("Your Signature")
    st.button("Create Account")
main_page()