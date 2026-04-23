import streamlit as st
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)

st.title(' ChatBot Demo With Gemini')
input_text=st.text_input("Enter your question here")


output_parser=StrOutputParser()

chain=prompt|llm|output_parser   
  
if input_text:
    st.write(chain.invoke({'question':input_text})) 