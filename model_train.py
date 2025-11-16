# model_train.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

# ==============================================
#  LOAD YOUR ORIGINAL EV DATASET
# ==============================================
df = pd.read_csv("ev_data.csv")

# ==============================================
# CREATE NEW SIMPLIFIED FEATURES
# ==============================================

# 1. Vehicle Weight (approx from length/width/height)
df["vehicle_weight"] = (
    df["length_mm"] * df["width_mm"] * df["height_mm"]
) / 2_000_000  # simple proportional weight

# 2. Motor Power (approx from top speed and torque)
df["motor_power"] = (df["top_speed_kmh"] * df["torque_nm"].fillna(180)) / 1000

# 3. Fast Charging Support (Yes/No)
df["fast_charging_support"] = df["fast_charging_power_kw_dc"].fillna(0).apply(
    lambda x: "Yes" if x > 20 else "No"
)

# 4. Aerodynamic Efficiency (rough estimation)
df["aerodynamic_efficiency"] = (
    df["height_mm"] / df["length_mm"]
).clip(0.15, 0.45)  # typical EV aero values

# 5. Battery Type
df["battery_type"] = df["battery_type"].fillna("Unknown")

# 6. Vehicle Type
df["vehicle_type"] = df["car_body_type"].fillna("Unknown")

# ===============================
# Define Model Inputs & Outputs
# ===============================
features = [
    "vehicle_weight",
    "motor_power",
    "battery_type",
    "fast_charging_support",
    "vehicle_type",
    "aerodynamic_efficiency"
]

target_battery = "battery_capacity_kWh"
target_range = "range_km"

X = df[features]
y1 = df[target_battery]
y2 = df[target_range]

# Preprocessing
numeric_cols = ["vehicle_weight", "motor_power", "aerodynamic_efficiency"]
categorical_cols = ["battery_type", "fast_charging_support", "vehicle_type"]

preprocess = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

# Two separate models
battery_model = Pipeline([
    ("preprocess", preprocess),
    ("model", RandomForestRegressor(n_estimators=180))
])

range_model = Pipeline([
    ("preprocess", preprocess),
    ("model", RandomForestRegressor(n_estimators=200))
])

# Train
battery_model.fit(X, y1)
range_model.fit(X, y2)

# Save combined model
final_model = {
    "battery_model": battery_model,
    "range_model": range_model,
    "features": features
}

with open("model/simple_ev_model.pkl", "wb") as f:
    pickle.dump(final_model, f)

print("🎉 Training complete! Model saved as simple_ev_model.pkl")
