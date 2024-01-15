import time
import streamlit as st
import requests
import schedule


st.title("hello")
st.markdown("*Streamlit* is **really** ***cool***.")

# db_username = "Jane"

urls = [
"https://github.com/", 
"https://www.w3schools.com/", 
"https://streamlit.io/"
]

r = requests.get(url)

for i, url in enumerate(urls, start=1):
    print(f"{i}, {url}, r.status_code")
	time.sleep(8)

#def job():
#	r = requests.get('https://www.w3schools.com/')
#	return r.status_code
	
#schedule.every(60).seconds.do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)




