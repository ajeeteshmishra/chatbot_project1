## streamlit UI

import streamlit as st
import requests

st.title("Chatbot..💬")
st.text("Search your query here..")
search_bar = st.text_input("Search",placeholder="Input Text",label_visibility='collapsed')
search_button = st.button("Submit")

if search_button:
  #chat_response = generate_response(search_bar)
  chat_response = requests.post('http://localhost:8000/chatbot',json={"query":search_bar})
  st.text("Chat Response..")
  st.write(chat_response.json())