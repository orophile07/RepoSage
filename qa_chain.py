from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

def get_direct_llm():
    return ChatGroq(
        api_key=st.secrets["GROQ_API_KEY"],
        model_name="llama3-70b-8192"
    )
