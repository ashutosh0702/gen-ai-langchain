from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assistant . Please response to the suer queries"),
        ("user", "Question : {question}")
        
    ]
)

# Streamlit framework

st.title("LANGCHAIN Demo with Olama")
input_text = st.text_input("Search the topic you want")

# OpenAI LLM

llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    
    st.write(chain.invoke({"question" : input_text}))