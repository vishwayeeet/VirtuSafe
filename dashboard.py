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
# Dark Theme Styling with Animations
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* { font-family: 'Poppins', sans-serif; }

body { 
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Animated gradient background */
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glowing effect */
@keyframes glow {
    0% { text-shadow: 0 0 5px rgba(0, 217, 255, 0.5); }
    50% { text-shadow: 0 0 20px rgba(0, 217, 255, 0.8), 0 0 30px rgba(0, 217, 255, 0.6); }
    100% { text-shadow: 0 0 5px rgba(0, 217, 255, 0.5); }
}

/* Card animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

/* Card styles */
.card {
    background: linear-gradient(135deg, rgba(22, 27, 34, 0.9), rgba(30, 40, 60, 0.9));
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 217, 255, 0.2);
    animation: slideIn 0.6s ease-out;
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: 0 12px 40px rgba(0, 217, 255, 0.3);
    border: 1px solid rgba(0, 217, 255, 0.4);
    transform: translateY(-5px);
}

/* Status indicators */
.status-safe { 
    color: #00D9FF;
    font-weight: bold;
    animation: glow 2s ease-in-out infinite;
}

.status-warning { 
    color: #FFB800;
    font-weight: bold;
    animation: glow 1.5s ease-in-out infinite;
}

.status-danger { 
    color: #FF3D3D;
    font-weight: bold;
    animation: glow 1s ease-in-out infinite;
}

/* System online indicator */
.system-online {
    display: inline-block;
    animation: float 2s ease-in-out infinite;
}

/* Risk meter animation */
.risk-meter {
    animation: slideIn 0.8s ease-out;
}

/* Metric cards */
.metric-card {
    background: linear-gradient(135deg, rgba(30, 40, 60, 0.8), rgba(20, 30, 50, 0.8));
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(0, 217, 255, 0.2);
    animation: slideIn 0.6s ease-out;
    transition: all 0.3s ease;
}

.metric-card:hover {
    border: 1px solid rgba(0, 217, 255, 0.4);
    box-shadow: 0 0 20px rgba(0, 217, 255, 0.2);
}

/* Room cards with animation */
.room-card {
    background: linear-gradient(135deg, rgba(30, 40, 60, 0.9), rgba(20, 30, 50, 0.9));
    padding: 20px;
    border-radius: 14px;
    margin: 10px;
    border-left: 5px solid;
    animation: slideIn 0.6s ease-out;
    transition: all 0.3s ease;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.room-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 32px rgba(0, 217, 255, 0.2);
}

.room-card h4 {
    margin: 0 0 10px 0;
    font-size: 1.1em;
    font-weight: 600;
}

.room-card p {
    margin: 0;
    font-size: 1em;
    font-weight: 600;
}

/* Button animations */
button {
    transition: all 0.3s ease !important;
}

button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 8px 24px rgba(255, 20, 147, 0.3) !important;
}

/* Recommendation box */
.recommendation-box {
    background: linear-gradient(135deg, rgba(30, 40, 60, 0.9), rgba(20, 30, 50, 0.9));
    border-left: 4px solid #00D9FF;
    padding: 20px;
    border-radius: 8px;
    animation: slideIn 0.8s ease-out;
}

/* Header animations */
h1, h2, h3 {
    animation: slideIn 0.6s ease-out;
}

/* Title styling */
.main-title {
    background: linear-gradient(135deg, #00D9FF, #00BCD4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: glow 2s ease-in-out infinite;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("<h1 class='main-title'>🛡️ VirtuSafe+ – AI Digital Twin Safety Platform</h1>", unsafe_allow_html=True)
st.caption("✨ Real‑time Monitoring • 🤖 Predictive AI • ⚡ Multi-Hazard Safety System")
st.markdown("<div class='system-online'><span style='color:#00D9FF;font-weight:bold;'>● SYSTEM ONLINE</span></div>", unsafe_allow_html=True)

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
    st.markdown("""
    <div class='metric-card'>
        <div style='font-size: 2em; margin-bottom: 10px;'>🌡</div>
        <div style='color: #888; font-size: 0.9em;'>Temperature (°C)</div>
        <div style='font-size: 1.8em; color: #00D9FF; font-weight: bold;'>{:.1f}°C</div>
    </div>
    """.format(temperature), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <div style='font-size: 2em; margin-bottom: 10px;'>💨</div>
        <div style='color: #888; font-size: 0.9em;'>Smoke Level</div>
        <div style='font-size: 1.8em; color: #00BCD4; font-weight: bold;'>{:.1f}</div>
    </div>
    """.format(smoke), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <div style='font-size: 2em; margin-bottom: 10px;'>⚡</div>
        <div style='color: #888; font-size: 0.9em;'>Power (kW)</div>
        <div style='font-size: 1.8em; color: #00D9FF; font-weight: bold;'>{:.2f}</div>
    </div>
    """.format(power), unsafe_allow_html=True)

with col4:
    status_color = "#FF3D3D" if status == "DANGER" else "#FFB800" if status == "WARNING" else "#00D9FF"
    st.markdown("""
    <div class='metric-card'>
        <div style='font-size: 2em; margin-bottom: 10px;'>🤖</div>
        <div style='color: #888; font-size: 0.9em;'>Status</div>
        <div style='font-size: 1.8em; color: {}; font-weight: bold;'>{}</div>
    </div>
    """.format(status_color, status), unsafe_allow_html=True)

# -------------------------------
# Risk Meter
# -------------------------------
st.markdown("## 🚨 Risk Level")
risk_color = "#FF3D3D" if risk_score >= 70 else "#FFB800" if risk_score >= 40 else "#00D9FF"
st.markdown(f"""
<div class='risk-meter'>
    <div style='background: linear-gradient(to right, #00D9FF, #00BCD4, #FFB800, #FF3D3D); height: 8px; border-radius: 10px; margin-bottom: 10px;'></div>
    <div style='font-size: 1.5em; color: {risk_color}; font-weight: bold;'>Risk Score: {risk_score}%</div>
</div>
""", unsafe_allow_html=True)
st.progress(min(risk_score, 100))

# -------------------------------
# Extended Sensors Panel
# -------------------------------
st.markdown("## 🔍 Extended Sensor Monitoring")

c1, c2, c3, c4 = st.columns(4)

c1.markdown("""
<div class='metric-card'>
    <div style='font-size: 2em; margin-bottom: 10px;'>🌫</div>
    <div style='color: #888; font-size: 0.9em;'>Gas Level</div>
    <div style='font-size: 1.8em; color: #00BCD4; font-weight: bold;'>{:.1f}%</div>
</div>
""".format(gas), unsafe_allow_html=True)

c2.markdown("""
<div class='metric-card'>
    <div style='font-size: 2em; margin-bottom: 10px;'>💨</div>
    <div style='color: #888; font-size: 0.9em;'>CO₂ Level</div>
    <div style='font-size: 1.8em; color: #00D9FF; font-weight: bold;'>{:.0f} ppm</div>
</div>
""".format(co2), unsafe_allow_html=True)

c3.markdown("""
<div class='metric-card'>
    <div style='font-size: 2em; margin-bottom: 10px;'>💧</div>
    <div style='color: #888; font-size: 0.9em;'>Water Leak</div>
    <div style='font-size: 1.8em; color: {}; font-weight: bold;'>{}</div>
</div>
""".format("#FF3D3D" if water_leak else "#00D9FF", "🚨 YES" if water_leak else "✓ NO"), unsafe_allow_html=True)

c4.markdown("""
<div class='metric-card'>
    <div style='font-size: 2em; margin-bottom: 10px;'>💦</div>
    <div style='color: #888; font-size: 0.9em;'>Humidity</div>
    <div style='font-size: 1.8em; color: #00BCD4; font-weight: bold;'>{:.1f}%</div>
</div>
""".format(humidity), unsafe_allow_html=True)

# -------------------------------
# Recommendation
# -------------------------------
st.markdown("## 🧠 AI Recommendation")
rec_color = "#FF3D3D" if status == "DANGER" else "#FFB800" if status == "WARNING" else "#00D9FF"
st.markdown(f"""
<div class='recommendation-box' style='border-left-color: {rec_color};'>
    <div style='font-size: 1.1em; color: white;'>{recommendation}</div>
</div>
""", unsafe_allow_html=True)

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
        color = "#FF3D3D"
    elif state == "WARNING":
        indicator = "🟠 WARNING"
        color = "#FFB800"
    else:
        indicator = "🟢 SAFE"
        color = "#00D9FF"

    with (col_a if i % 2 == 0 else col_b):
        st.markdown(
            f"""
            <div class='room-card' style='border-left-color: {color};'>
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
