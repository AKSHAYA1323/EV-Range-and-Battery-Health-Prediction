import streamlit as st
from chatbot import ask_groq

st.set_page_config(page_title="EV Chatbot", page_icon="🔋")

# --- FIXED CSS WITH DARK TEXT + HIGH CONTRAST BUBBLES ---
custom_css = """
<style>
.chat-container {
    padding: 12px;
    border-radius: 12px;
    margin-top: 8px;
    margin-bottom: 8px;
    max-width: 80%;
    font-size: 16px;
    color: #1a1a1a; /* DARK TEXT */
}

.user-bubble {
    background-color: #d4f8d4; /* light green */
    margin-left: auto;
    border: 1px solid #9be89b;
}

.bot-bubble {
    background-color: #f0f4ff; /* light blue */
    margin-right: auto;
    border: 1px solid #bcd3ff;
}

.sender {
    font-weight: 600;
    margin-bottom: 4px;
    color: #000000; /* dark text color */
}

/* Input box style */
input[type="text"] {
    color: #000000 !important;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- TITLE ---
st.title("⚡ EV Smart Assistant")
st.caption("Your intelligent EV expert — Ask anything about electric vehicles.")

# --- SESSION STATE ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- USER INPUT ---
user_input = st.text_input(
    "💬 Type your EV question:",
    placeholder="Example: 'What is the difference between LFP and NMC batteries?'",
)

if st.button("Send"):
    if user_input.strip():

        # Add user query
        st.session_state.chat_history.append(("You", user_input))

        # Get LLM response
        reply = ask_groq(user_input)

        # Add bot reply
        st.session_state.chat_history.append(("Bot", reply))

# --- SHOW CHAT HISTORY ---
st.write("### 💬 Conversation")

for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(
            f"""
            <div class="chat-container user-bubble">
                <div class="sender">🧍 You</div>
                {msg}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="chat-container bot-bubble">
                <div class="sender">🤖 EV Bot</div>
                {msg}
            </div>
            """,
            unsafe_allow_html=True
        )
