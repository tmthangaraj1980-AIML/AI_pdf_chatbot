"""
Gemini LLM Configuration
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import GOOGLE_API_KEY


def load_llm():

    llm = ChatGoogleGenerativeAI(

        model="gemini-2.5-flash",

        google_api_key=GOOGLE_API_KEY,

        temperature=0.3

    )

    return llm