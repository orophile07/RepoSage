from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

def get_direct_llm():
    return ChatGroq(
        api_key=st.secrets("groq_api_key"),
        model_name="llama3-70b-8192"
    )
