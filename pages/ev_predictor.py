# pages/ev_predictor.py

import streamlit as st
import pickle
import pandas as pd

# -----------------------------------
# PAGE TITLE
# -----------------------------------
st.title("⚡ Smart EV Battery + Range Predictor")
st.write("Enter basic EV details to get **Battery Capacity (kWh)** and **Real-World Range (km)** predictions.")

# -----------------------------------
# LOAD MODELS
# -----------------------------------
with open("model/simple_ev_model.pkl", "rb") as f:
    model_bundle = pickle.load(f)

battery_model = model_bundle["battery_model"]
range_model = model_bundle["range_model"]
features = model_bundle["features"]

# -----------------------------------
# USER INPUTS
# -----------------------------------
st.subheader("📥 Input EV Specifications")

col1, col2 = st.columns(2)

with col1:
    vehicle_weight = st.number_input("Vehicle Weight (kg)", 800, 3500, 1400)
    motor_power = st.number_input("Motor Power (kW)", 20, 500, 100)
    aerodynamic_efficiency = st.slider("Aerodynamic Efficiency (0–1)", 0.10, 0.45, 0.30)

with col2:
    battery_type = st.selectbox("Battery Type", ["LFP", "NMC", "Unknown"])
    fast_charging_support = st.selectbox("Fast Charging Support", ["Yes", "No"])
    vehicle_type = st.selectbox("Vehicle Type", [
        "Hatchback", "Sedan", "SUV", "Pickup", "Van", "Unknown"
    ])

# Prepare input dataframe
input_df = pd.DataFrame([{
    "vehicle_weight": vehicle_weight,
    "motor_power": motor_power,
    "battery_type": battery_type,
    "fast_charging_support": fast_charging_support,
    "vehicle_type": vehicle_type,
    "aerodynamic_efficiency": aerodynamic_efficiency
}])


# -----------------------------------
# PREDICT
# -----------------------------------
st.write("---")
if st.button("🚀 Predict Now"):
    try:
        battery_pred = battery_model.predict(input_df)[0]
        range_pred = range_model.predict(input_df)[0]

        # RESULTS CARD
        st.markdown("""
            <div style="
                padding: 20px;
                background: #1e1e1e;
                border-radius: 12px;
                border: 1px solid #444;
                margin-top: 10px;">
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <h3 style="color:#4CC9F0;">🔋 Estimated Battery Capacity</h3>
        <h1 style="color:white;">{battery_pred:.1f} kWh</h1>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <h3 style="color:#80FF72;">🚗 Predicted Real-World Driving Range</h3>
        <h1 style="color:white;">{range_pred:.0f} km</h1>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")
