import streamlit as st

st.title("Username Generator")

name = st.text_input("Enter your name")
number = st.text_input("Enter a number")

if st.button("Generate Username"):
    username = name.lower() + number
    st.success(f"Your Username: {username}")