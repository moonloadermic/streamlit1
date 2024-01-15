import time
import streamlit as st
import requests


st.title("hello")
st.markdown("*Streamlit* is **really** ***cool***.")

r = requests.get('https://www.w3schools.com/')
print(r.status_code)
print(r.url)
st.write(r.status_code)
st.write(r.url)
st.markdown(r.status_code)




