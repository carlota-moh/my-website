import requests
import streamlit as st

def load_url(url: str) -> dict:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

def load_css(style_file: str) -> None:
    """Load CSS styling"""
    with open(style_file, 'r') as f:
        st.markdown(f"<style>{f.read()}<style/>", unsafe_allow_html=True)