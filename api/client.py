import streamlit as st
import requests

def get_llama3_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                            json={"input" : {"topic": input_text}})
                            
    return response.json()["output"]
    
def get_phi3_response(input_text):
    
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={"input" : {"topic": input_text}})
                             
    return response.json()["output"]
    
# Streamlit Framework

st.title("Langchain demo with llam3 and phi3")
input_text = st.text_input("Write a essay on ")
input_text1 = st.text_input("Write a poem on ")

if input_text:
    st.write(get_llama3_response(input_text))
    
if input_text1:
    st.write(get_phi3_response(input_text1))