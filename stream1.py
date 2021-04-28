import streamlit as st

langs = st.multiselect("Which are programming languages?",
                         ["Python", "Java","English", "C++", "JavaScript","Farsi"])

if "Python" in langs:
    st.write("You are correct!")
if "Java" in langs:
    st.write("You are correct!")
if "C++" in langs:
    st.write("You are correct!")
if "JavaScript" in langs:
    st.write("You are correct!")
if "English" in langs:
    st.write("English is not a programming language!")
if "Farsi" in langs:
    st.write("Farsi is not a programming language!")
