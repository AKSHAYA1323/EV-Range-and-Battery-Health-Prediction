import streamlit as st
from chatbot import ask_groq # Keep your existing import logic

# Must be the first Streamlit command
st.set_page_config(page_title="EV Intelligence", page_icon="⚡", layout="wide")

# -------------------- UI THEME & DESIGN --------------------
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at center, #0B0E2A 0%, #050714 100%);
        color: #FFFFFF;
    }
    
    /* Landing Page Elements */
    .main-container { display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 3rem; }
    .top-badge { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 5px 15px; font-size: 0.8rem; color: #8E94B2; margin-bottom: 20px; }
    .main-title { font-size: 4rem; font-weight: 800; text-align: center; margin-bottom: 10px; }
    .title-blue { color: #4ADEDE; text-shadow: 0 0 30px rgba(74, 222, 222, 0.3); }
    .subtitle { color: #8E94B2; text-align: center; max-width: 600px; margin-bottom: 50px; font-size: 1.1rem; }

    /* Card Design */
    .card-box {
        background: linear-gradient(145deg, #0F1229, #080A1A);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px;
        height: 320px;
        transition: 0.3s;
    }
    .icon-square { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; font-size: 1.5rem; }

    /* Chat Bubbles */
    .chat-container { padding: 14px; border-radius: 14px; margin: 8px 0; max-width: 85%; }
    .user-bubble { background: rgba(74, 222, 222, 0.1); border: 1px solid #4ADEDE; margin-left: auto; }
    .bot-bubble { background: rgba(130,150,255,0.1); border: 1px solid #6C9CFF; margin-right: auto; }
    
    /* Buttons */
    div.stButton > button {
        background: transparent; border: none; color: #4ADEDE !important; font-weight: 600; padding: 0;
    }
    .back-btn > div.stButton > button { color: #8E94B2 !important; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE LOGIC --------------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def navigate_to(page_name):
    st.session_state.page = page_name

# -------------------- HOME PAGE --------------------
if st.session_state.page == 'home':
    st.markdown("""
        <div class="main-container">
            <div class="top-badge">⚡ Unified EV Analytics Platform</div>
            <h1 class="main-title">EV <span class="title-blue">Intelligence</span></h1>
            <p class="subtitle">Predict range, analyze battery performance, and get instant answers to all your EV questions.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    
    with col2:
        st.markdown('<div class="card-box"><div class="icon-square">🔋</div><h3>EV Predictor</h3><p style="color:#8E94B2;">Predict range and battery capacity based on specs.</p></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="go_pred"): navigate_to('predictor')

    with col3:
        st.markdown('<div class="card-box"><div class="icon-square">🤖</div><h3>EV Chatbot</h3><p style="color:#8E94B2;">Ask EV-related questions and get instant, knowledgeable responses.</p></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="go_chat"): navigate_to('chatbot')

# -------------------- CHATBOT PAGE --------------------
elif st.session_state.page == 'chatbot':
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard"): navigate_to('home')
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.title("🤖 EV Smart Assistant")
    st.caption("Powered by Groq Llama 3.3")

    user_input = st.text_input("💬 Ask your EV question:", placeholder="How do LFP batteries work?")

    if st.button("Send Message"):
        if user_input.strip():
            st.session_state.chat_history.append(("You", user_input))
            reply = ask_groq(user_input) # Logic from chatbot.py
            st.session_state.chat_history.append(("Bot", reply))

    for sender, msg in st.session_state.chat_history:
        bubble = "user-bubble" if sender == "You" else "bot-bubble"
        st.markdown(f'<div class="chat-container {bubble}"><b>{sender}</b><br>{msg}</div>', unsafe_allow_html=True)

# -------------------- PREDICTOR PAGE (Placeholder) --------------------
elif st.session_state.page == 'predictor':
    if st.button("← Back to Dashboard"): navigate_to('home')
    st.title("🔋 EV Predictor")
    st.write("Predictor logic goes here...")