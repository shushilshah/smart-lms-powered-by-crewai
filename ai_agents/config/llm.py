from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model= "gemini/gemini-2.5-flash-lite",
        api_key= os.getenv("GEMINI_API_KEY"),
        temperature= 0.3
    )