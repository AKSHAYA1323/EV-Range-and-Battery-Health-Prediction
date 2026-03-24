import streamlit as st
import pickle
import pandas as pd
from chatbot import ask_groq  # Connecting your chatbot logic

# Must be the first command
st.set_page_config(page_title="EV Intelligence", page_icon="⚡", layout="wide")

# -------------------- UNIFIED NEON UI DESIGN --------------------
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top, #0d0d2b 0%, #020205 100%);
        color: #E0E0FF;
    }

    /* Landing Page Elements */
    .main-container { display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 3rem; }
    .top-badge { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 5px 15px; font-size: 0.8rem; color: #8E94B2; margin-bottom: 20px; }
    
    .main-title {
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 800;
        background: linear-gradient(to right, #ffffff, #4ADEDE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    /* Card Styling */
    .card-box {
        background: linear-gradient(145deg, #0F1229, #080A1A);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px;
        height: 320px;
        transition: 0.3s;
    }
    .icon-square { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; font-size: 1.5rem; }

    /* Predictor Specific Styles */
    .result-box {
        background: rgba(17, 17, 35, 0.8);
        border: 1px solid rgba(88, 101, 242, 0.4);
        border-radius: 15px;
        padding: 30px;
        text-align: center;
    }
    .result-value { font-size: 3rem; font-weight: 800; color: #ffffff; margin: 0; }
    .unit { font-size: 1rem; color: #6366f1; }

    /* Buttons */
    .stButton > button {
        background: transparent; border: none; color: #4ADEDE !important; font-weight: 600;
    }
    /* Action Button for Predictor */
    .predict-btn > div.stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1, #a855f7) !important;
        color: white !important;
        padding: 15px !important;
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- NAVIGATION LOGIC --------------------
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
            <h1 class="main-title">EV Intelligence</h1>
            <p style="text-align:center; color:#94a3b8; margin-bottom:50px;">Predict range, analyze battery performance, and get instant answers.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    with col2:
        st.markdown('<div class="card-box"><div class="icon-square">🔋</div><h3>EV Predictor</h3><p style="color:#8E94B2;">Predict range and battery capacity based on specs.</p></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="nav_pred"): navigate_to('predictor')
    with col3:
        st.markdown('<div class="card-box"><div class="icon-square">🤖</div><h3>EV Chatbot</h3><p style="color:#8E94B2;">Ask EV-related questions and get instant responses.</p></div>', unsafe_allow_html=True)
        if st.button("Explore →", key="nav_chat"): navigate_to('chatbot')

# -------------------- PREDICTOR PAGE --------------------
elif st.session_state.page == 'predictor':
    if st.button("← Back"): navigate_to('home')
    st.markdown('<h1 class="main-title">Smart EV Predictor</h1>', unsafe_allow_html=True)
    
    # Model Loading
    try:
        with open("model/simple_ev_model.pkl", "rb") as f:
            model_bundle = pickle.load(f)
        battery_model = model_bundle["battery_model"]
        range_model = model_bundle["range_model"]
    except:
        st.error("Model files not found. Check 'model/simple_ev_model.pkl'")

    col1, col2 = st.columns(2)
    with col1:
        v_weight = st.number_input("Vehicle Weight (kg)", value=1400)
        aero = st.slider("Aerodynamic Efficiency", 0.10, 0.45, 0.30)
        fast_c = st.selectbox("Fast Charging Support", ["Yes", "No"])
    with col2:
        m_power = st.number_input("Motor Power (kW)", value=100)
        b_type = st.selectbox("Battery Type", ["LFP", "NMC", "Unknown"])
        v_type = st.selectbox("Vehicle Type", ["Sedan", "Hatchback", "SUV", "Pickup", "Van"])

    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    if st.button("🚀 Predict Now"):
        input_df = pd.DataFrame([{
            "vehicle_weight": v_weight, "motor_power": m_power, "battery_type": b_type,
            "fast_charging_support": fast_c, "vehicle_type": v_type, "aerodynamic_efficiency": aero
        }])
        
        b_pred = battery_model.predict(input_df)[0]
        r_pred = range_model.predict(input_df)[0]

        st.write("##")
        res1, res2 = st.columns(2)
        with res1:
            st.markdown(f'<div class="result-box"><p>Battery Capacity</p><p class="result-value">{b_pred:.1f}</p><p class="unit">kWh</p></div>', unsafe_allow_html=True)
        with res2:
            st.markdown(f'<div class="result-box"><p>Real-World Range</p><p class="result-value">{r_pred:.0f}</p><p class="unit">km</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CHATBOT PAGE --------------------
elif st.session_state.page == 'chatbot':
    if st.button("← Back"): navigate_to('home')
    st.markdown('<h1 class="main-title">EV Smart Assistant</h1>', unsafe_allow_html=True)
    
    u_input = st.text_input("💬 Ask your EV question:", placeholder="Example: How does regenerative braking work?")
    if st.button("Send Message"):
        if u_input.strip():
            st.session_state.chat_history.append(("You", u_input))
            reply = ask_groq(u_input)
            st.session_state.chat_history.append(("Bot", reply))

    for sender, msg in st.session_state.chat_history:
        color = "#4ADEDE" if sender == "You" else "#a5b4fc"
        st.markdown(f'<div style="border-left:3px solid {color}; padding:10px; margin:5px 0; background:rgba(255,255,255,0.02);"><b>{sender}</b><br>{msg}</div>', unsafe_allow_html=True)