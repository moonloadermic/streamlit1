import time
import streamlit as st
import requests


st.title("hello")
st.markdown("*Streamlit* is **really** ***cool***.")

r = requests.get('https://www.w3schools.com/')

st.write("url", r.status_code)
st.markdown(r.status_code)




