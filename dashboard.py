import streamlit as st
import random
import time
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="VirtuSafe+ | AI Digital Twin",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# Dark Theme Styling
# -------------------------------
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
.card {
    background: #161b22;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
}
.status-safe { color: #00ff99; font-weight: bold; }
.status-warning { color: #ffcc00; font-weight: bold; }
.status-danger { color: #ff4b4b; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.title("🛡️ VirtuSafe+ – AI Digital Twin Safety Platform")
st.caption("Real‑time Monitoring • Predictive AI • Multi-Hazard Safety System")
st.markdown("<span style='color:#00ff99;font-weight:bold;'>● SYSTEM ONLINE</span>", unsafe_allow_html=True)

# -------------------------------
# Start / Stop Control
# -------------------------------
if "running" not in st.session_state:
    st.session_state.running = False

col_start, col_stop = st.columns(2)

with col_start:
    if st.button("▶️ START SYSTEM"):
        st.session_state.running = True

with col_stop:
    if st.button("⏸️ STOP SYSTEM"):
        st.session_state.running = False

# -------------------------------
# Simulated Sensors
# -------------------------------
temperature = random.uniform(25, 70)
smoke = random.uniform(5, 50)
power = random.uniform(1, 5)
gas = random.uniform(0, 100)
co2 = random.uniform(400, 2000)
water_leak = random.choice([0, 1])
motion = random.choice([0, 1])
humidity = random.uniform(30, 90)

# -------------------------------
# Multi-Factor Risk Engine
# -------------------------------
risk_score = 0

if temperature > 60: risk_score += 25
if smoke > 40: risk_score += 25
if gas > 70: risk_score += 15
if co2 > 1500: risk_score += 10
if water_leak == 1: risk_score += 15
if motion == 1: risk_score += 10
if humidity > 80: risk_score += 10

if risk_score >= 70:
    status = "DANGER"
    status_class = "status-danger"
    recommendation = "Immediate evacuation and safety action required"
elif risk_score >= 40:
    status = "WARNING"
    status_class = "status-warning"
    recommendation = "Check environment and reduce risk"
else:
    status = "SAFE"
    status_class = "status-safe"
    recommendation = "All systems normal"

# -------------------------------
# Main KPI Cards
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🌡 Temperature (°C)", f"{temperature:.1f}")

with col2:
    st.metric("💨 Smoke Level", f"{smoke:.1f}")

with col3:
    st.metric("⚡ Power (kW)", f"{power:.2f}")

with col4:
    st.markdown(f"<h3>🤖 Status</h3><h2 class='{status_class}'>{status}</h2>", unsafe_allow_html=True)

# -------------------------------
# Risk Meter
# -------------------------------
st.markdown("## 🚨 Risk Level")
st.progress(min(risk_score, 100))
st.markdown(f"### Risk Score: **{risk_score}%**")

# -------------------------------
# Extended Sensors Panel
# -------------------------------
st.markdown("## 🔍 Extended Sensor Monitoring")

c1, c2, c3, c4 = st.columns(4)

c1.metric("🌫 Gas (%)", f"{gas:.1f}")
c2.metric("💨 CO₂ (ppm)", f"{co2:.0f}")
c3.metric("💧 Water Leak", "YES" if water_leak else "NO")
c4.metric("💦 Humidity (%)", f"{humidity:.1f}")

# -------------------------------
# Recommendation
# -------------------------------
st.markdown("## 🧠 AI Recommendation")
st.info(recommendation)

# -------------------------------
# Simple Digital Map Prototype
# -------------------------------
st.markdown("## 🗺️ Digital Safety Map (Prototype)")

zones = {
    "Living Room": "SAFE",
    "Kitchen": "SAFE",
    "Bedroom": "SAFE",
    "Bathroom": "SAFE"
}

if status == "DANGER":
    zones["Kitchen"] = "DANGER"
elif status == "WARNING":
    zones["Living Room"] = "WARNING"

col_a, col_b = st.columns(2)

for i, (room, state) in enumerate(zones.items()):
    if state == "DANGER":
        indicator = "🔴 ALERT"
        color = "#ff4b4b"
    elif state == "WARNING":
        indicator = "🟠 WARNING"
        color = "#ffcc00"
    else:
        indicator = "🟢 SAFE"
        color = "#00ff99"

    with (col_a if i % 2 == 0 else col_b):
        st.markdown(
            f"""
            <div style="
                background:#161b22;
                padding:15px;
                border-radius:12px;
                margin:10px;
                border-left:5px solid {color};
            ">
            <h4>{room}</h4>
            <p>{indicator}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------
# Auto Refresh Control
# -------------------------------
if st.session_state.running:
    time.sleep(2)
    st.rerun()
else:
    st.warning("⏸️ System Paused")
