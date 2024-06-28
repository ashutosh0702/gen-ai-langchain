from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_env

import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assistant . Please response to the suer queries"),
        ("user", "Question : {question}")
        
    ]
)

# Streamlit framework

st.title("LANGCHAIN Demo with OpenAI")
input_text = st.text_input("Search the topic you want")

# OpenAI LLM

llm = OpenAI(model="gpt-3.5-urbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    
    st.write(chain.invoke({"question" : input_text}))