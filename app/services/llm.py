# app/services/llm.py
from google import genai
import os
from google.genai import types
from dotenv import load_dotenv

from .prompts import build_prompt, DATA_ANALYST_PROMPT

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY", default="")
CLIENT = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.5-flash"

def generate_response(context: str, question: str, role_prompt: str = DATA_ANALYST_PROMPT):
    """
    Generate a response using Gemini with role-specific prompt,
    dataset context, and user question.
    """
    full_prompt = build_prompt(role_prompt, context, question)

    response = CLIENT.models.generate_content(
        model=MODEL_ID,
        contents=full_prompt,
        config={
            "temperature": 0.2,
            "max_output_tokens": 4000
        }
    )
    return response.text


