import streamlit as st

def menu():
    st.sidebar.page_link("app.py", label="About me")
    st.sidebar.page_link("pages/projects.py", label="Projects")