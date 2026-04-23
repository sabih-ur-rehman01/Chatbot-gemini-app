# Chatbot-gemini-app
This is a simple Streamlit-based chatbot application built using LangChain and the Groq API. The app allows users to enter questions and receive AI-generated responses in real time.  The project demonstrates how to integrate a language model into a web interface using Streamlit, making it easy to interact with AI directly from a browser.

Features:
Interactive chatbot UI using Streamlit
Integration with Groq LLM (openai/gpt-oss-120b)
Uses LangChain for prompt management and chaining
Environment variable support with .env file
Simple and beginner-friendly implementation

Tech Stack:
Python
Streamlit
LangChain
Groq API
python-dotenv

How It Works:
Loads API key from .env file
Creates a prompt template for chatbot interaction
Sends user input to the Groq language model
Displays the generated response on the Streamlit interface
