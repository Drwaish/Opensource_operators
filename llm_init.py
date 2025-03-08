""" Initialize the LLM using OPEN AI wrapper"""
from os import getenv
from typing import Optional
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = getenv("Google_API_KEY")
model = getenv("Google_MODEL")
def get_llm() -> ChatGoogleGenerativeAI:
    """Initialize the LLM using using googlel model
    
    Parameters
    ----------
    """
    return ChatGoogleGenerativeAI(api_key=api_key or getenv("Google_API_KEY"), model=model or getenv("GOOGLE_MODEL"))
