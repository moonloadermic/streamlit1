import time
import streamlit as st
import requests


st.title("hello")
st.markdown("*Streamlit* is **really** ***cool***.")

# db_username = "Jane"

r = requests.get('https://www.w3schools.com/')

st.write("website status: ", r.status_code)
st.markdown(r.status_code)




