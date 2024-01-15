import time
import streamlit as st
import requests
import schedule


st.title("hello")
st.markdown("*Streamlit* is **really** ***cool***.")

# db_username = "Jane"

def job():
	r = requests.get('https://www.w3schools.com/')
	return r.status_code
	
schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)




