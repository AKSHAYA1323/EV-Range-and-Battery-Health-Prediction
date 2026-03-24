import streamlit as st
import pickle
import pandas as pd
from chatbot import ask_groq  # Ensure chatbot.py is in your folder

# 1. Page Config
st.set_page_config(page_title="EV Intelligence", page_icon="⚡", layout="wide")

# 2. Unified CSS
st.markdown("""
<style>
    /* HIDE SIDEBAR COMPLETELY */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Main Background */
    .stApp { 
        background: radial-gradient(circle at center, #0B0E2A 0%, #050714 100%); 
        color: #FFFFFF; 
    }
    
    /* Landing Page Elements */
    .main-container { display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 3rem; }
    .top-badge { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 5px 15px; font-size: 0.8rem; color: #8E94B2; margin-bottom: 20px; display: inline-block; }
    .main-title { font-size: 4rem; font-weight: 800; text-align: center; margin-bottom: 10px; }
    .title-white { color: #FFFFFF; }
    .title-blue { color: #4ADEDE; text-shadow: 0 0 30px rgba(74, 222, 222, 0.3); }
    
    /* Card Styles */
    .card-container {
        background: linear-gradient(145deg, #0F1229, #080A1A);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px; padding: 40px; height: 320px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .icon-box { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; margin-bottom: 25px; font-size: 1.5rem; }

    /* Predictor Result Styles */
    .result-box { background: rgba(17, 17, 35, 0.8); border: 1px solid #4ADEDE; border-radius: 15px; padding: 20px; text-align: center; margin-top: 20px; }
    .result-value { font-size: 2.5rem; font-weight: 800; color: #FFFFFF; margin: 0; }

    /* Custom Button Styling */
    div.stButton > button { 
        background: transparent; 
        border: none; 
        color: #4ADEDE !important; 
        font-weight: 600; 
        padding: 0px;
    }
    div.stButton > button:hover {
        color: #FFFFFF !important;
        text-decoration: underline;
    }
    
    /* Special Predict Button Style */
    .predict-btn > div.stButton > button {
        background: linear-gradient(90deg, #6366f1, #a855f7) !important;
        color: white !important; 
        padding: 15px 20px !important; 
        border-radius: 12px !important; 
        width: 100%;
        text-decoration: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Session State Logic
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def navigate(page_name):
    st.session_state.page = page_name

# -------------------- ROUTING LOGIC --------------------

# --- PAGE: HOME ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class="main-container">
            <div class="top-badge">⚡ Unified EV Analytics Platform</div>
            <h1 class="main-title"><span class="title-white">EV</span> <span class="title-blue">Intelligence</span></h1>
            <p style="color:#8E94B2; text-align:center; max-width:600px; margin: 0 auto 50px auto;">
                Predict range, analyze battery performance, and get instant answers to all your EV questions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    with col2:
        st.markdown('<div class="card-container"><div class="icon-box">🔋</div><div><h3>EV Predictor</h3><p style="color:#8E94B2;">Predict range and capacity based on specs.</p></div></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="go_pred"): navigate('predictor')
    with col3:
        st.markdown('<div class="card-container"><div class="icon-box">🤖</div><div><h3>EV Chatbot</h3><p style="color:#8E94B2;">Ask EV questions and get instant responses.</p></div></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="go_chat"): navigate('chatbot')

# --- PAGE: PREDICTOR ---
elif st.session_state.page == 'predictor':
    if st.button("← Back to Dashboard"): navigate('home')
    st.title("🔋 EV Predictor")
    
    try:
        with open("model/simple_ev_model.pkl", "rb") as f:
            model_bundle = pickle.load(f)
        battery_model, range_model = model_bundle["battery_model"], model_bundle["range_model"]
        
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Vehicle Weight (kg)", value=1400)
            aero = st.slider("Aerodynamic Efficiency", 0.10, 0.45, 0.30)
            fast_c = st.selectbox("Fast Charging Support", ["Yes", "No"])
        with col2:
            power = st.number_input("Motor Power (kW)", value=100)
            b_type = st.selectbox("Battery Type", ["LFP", "NMC", "Unknown"])
            v_type = st.selectbox("Vehicle Type", ["Sedan", "Hatchback", "SUV", "Pickup", "Van"])

        st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
        if st.button("🚀 Predict Now"):
            input_df = pd.DataFrame([{"vehicle_weight": weight, "motor_power": power, "battery_type": b_type, "fast_charging_support": fast_c, "vehicle_type": v_type, "aerodynamic_efficiency": aero}])
            b_pred, r_pred = battery_model.predict(input_df)[0], range_model.predict(input_df)[0]
            
            res1, res2 = st.columns(2)
            res1.markdown(f'<div class="result-box"><p>Battery Capacity</p><p class="result-value">{b_pred:.1f} kWh</p></div>', unsafe_allow_html=True)
            res2.markdown(f'<div class="result-box"><p>Real-World Range</p><p class="result-value">{r_pred:.0f} km</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error("Model files not found. Check if 'model/simple_ev_model.pkl' exists.")

# --- PAGE: CHATBOT ---
elif st.session_state.page == 'chatbot':
    if st.button("← Back to Dashboard"): navigate('home')
    st.title("🤖 EV Smart Assistant")
    
    user_input = st.text_input("💬 Ask your EV question:", placeholder="Example: How do LFP batteries work?")
    if st.button("Send Message"):
        if user_input.strip():
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", ask_groq(user_input)))

    for sender, msg in st.session_state.chat_history:
        bubble_color = "#4ADEDE" if sender == "You" else "#6C9CFF"
        st.markdown(f'<div style="border-left: 3px solid {bubble_color}; padding-left: 15px; margin: 10px 0;"><b>{sender}</b><br>{msg}</div>', unsafe_allow_html=True)