""" Initialize the LLM using OPEN AI wrapper"""
from os import getenv
from typing import Optional
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
# from openai import ChatOpenAI

load_dotenv()


class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(self,
                 model_name: str,
                 openai_api_key: Optional[str] = None,
                 openai_api_base: str = "https://openrouter.ai/api/v1",
                 **kwargs):
        openai_api_key = openai_api_key or getenv("OPENROUTER_API_KEY")
        super().__init__(openai_api_base="https://openrouter.ai/api/v1",
                         openai_api_key=openai_api_key,
                         model_name=model_name, **kwargs)