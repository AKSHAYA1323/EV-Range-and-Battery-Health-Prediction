# chatbot.py
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    try:
        import streamlit as st
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except:
        pass

if not GROQ_API_KEY:
    def ask_groq(_):
        return "❌ GROQ_API_KEY missing!"
else:
    # FIX 1: Add a 20-second timeout to the client initialization
    client = Groq(api_key=GROQ_API_KEY, timeout=20.0)

    def ask_groq(user_message: str) -> str:
        try:
            # FIX 2: Use the most stable model ID
            # "llama-3.3-70b-versatile" is correct, but sometimes 
            # "llama3-70b-8192" is faster for testing.
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[
                    {"role": "system", "content": "You are an expert EV assistant. Keep answers concise."},
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ API Error: {str(e)}"