# chatbot.py
import os
from groq import Groq
from dotenv import load_dotenv

# ✅ Load .env file automatically
load_dotenv()

# Read key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY missing! Please check your .env file or environment variables.")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def ask_groq(user_message: str) -> str:
    """Send user query to Groq and return AI response."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert EV assistant. Answer clearly and helpfully."},
                {"role": "user", "content": user_message}
            ]
        )
        # ✅ Return message safely
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
