# chatbot.py
from groq import Groq
import os

# Load API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is missing! Set it in your environment variables.")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def ask_groq(user_message: str) -> str:
    """Send a message to Groq Llama 3.3 model and return response."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Recommended and working
            messages=[
                {"role": "system", "content": "You are an expert EV assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # ✔ FIXED — correct way to extract content
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
