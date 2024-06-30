from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI
from langserve import add_routes

from fastapi import FastAPI
from dotenv import load_dotenv
import os
import streamlit as st
import uvicorn

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
# os.environ['LANGCHAIN_TRACING_V2'] = "true"
# os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    escription="Langchain simple example server"
    
)

model1 = Ollama(model="llama3")
model2 = Ollama(model="phi3")

prompt1 = ChatPromptTemplate.from_template("Write me an eassy of 100 words about {topic}")
prompt2 = ChatPromptTemplate.from_template("Write me an poem of 100 words about {topic}")

add_routes(
    app,
    prompt1|model1,
    path="/essay"
)

add_routes(
    app,
    prompt2|model2,
    path="/poem"
)



# Need to run this command pip install sse_starlette

if __name__ == "__main__":
    
    uvicorn.run(app, host="localhost",port=8000)