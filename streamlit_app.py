import time
import streamlit as st
import requests
"""
## NO

## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

st.title("Test Selenium")
st.markdown("*Streamlit* is **really** ***cool***.")

r = requests.get('https://w3schools.com')
print(r.status_code)
print(r.url)
st.write(r.status_code)




