import time
import random
import csv
from datetime import datetime

# -------------------------------
# Digital Twin (All Sensors)
# -------------------------------
digital_twin = {
    "temperature": 25.0,
    "smoke": 5.0,
    "power": 1.2,
    "gas": 10.0,
    "co2": 500,
    "water_leak": 0,
    "motion": 0,
    "humidity": 40
}

history = {
    "temperature": [],
    "smoke": [],
    "power": [],
    "gas": [],
    "co2": [],
    "humidity": []
}

print("\nVirtuSafe+ Backend Started...\n")

# -------------------------------
# AI Risk Engine
# -------------------------------
def ai_decision_engine(twin):

    risk_score = 0

    if twin["temperature"] > 60:
        risk_score += 25
    if twin["smoke"] > 40:
        risk_score += 25
    if twin["gas"] > 70:
        risk_score += 15
    if twin["co2"] > 1500:
        risk_score += 10
    if twin["water_leak"] == 1:
        risk_score += 15
    if twin["motion"] == 1:
        risk_score += 10
    if twin["humidity"] > 80:
        risk_score += 10

    if risk_score >= 70:
        return "DANGER", risk_score, "Immediate evacuation required"

    elif risk_score >= 40:
        return "WARNING", risk_score, "Check environment and reduce risk"

    else:
        return "SAFE", risk_score, "All systems normal"


# -------------------------------
# Create CSV File
# -------------------------------
with open("data_log.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Time",
        "Temperature",
        "Smoke",
        "Power",
        "Gas",
        "CO2",
        "Water_Leak",
        "Motion",
        "Humidity",
        "Risk_Score",
        "AI_Status",
        "Recommendation"
    ])


# -------------------------------
# Real-Time Loop
# -------------------------------
while True:

    # Simulate Sensors
    digital_twin["temperature"] += random.uniform(-0.5, 2.0)
    digital_twin["smoke"] += random.uniform(-0.3, 0.8)
    digital_twin["power"] += random.uniform(-0.1, 0.5)
    digital_twin["gas"] += random.uniform(-1, 3)
    digital_twin["co2"] += random.uniform(-20, 80)
    digital_twin["humidity"] += random.uniform(-1, 2)

    digital_twin["water_leak"] = random.choice([0, 0, 0, 1])
    digital_twin["motion"] = random.choice([0, 0, 1])


    # Store History
    for key in history:
        history[key].append(digital_twin[key])

        if len(history[key]) > 5:
            history[key].pop(0)


    # AI Decision
    status, risk_score, recommendation = ai_decision_engine(digital_twin)


    # Timestamp
    timestamp = datetime.now().strftime("%H:%M:%S")


    # Terminal Output
    print(f"⏱ {timestamp}")

    print(f"🌡 Temp: {digital_twin['temperature']:.2f} °C")
    print(f"💨 Smoke: {digital_twin['smoke']:.2f}")
    print(f"⚡ Power: {digital_twin['power']:.2f} kW")
    print(f"🌫 Gas: {digital_twin['gas']:.2f} %")
    print(f"💨 CO2: {digital_twin['co2']:.0f} ppm")
    print(f"💧 Water Leak: {digital_twin['water_leak']}")
    print(f"🚶 Motion: {digital_twin['motion']}")
    print(f"💦 Humidity: {digital_twin['humidity']:.1f} %")

    print(f"📊 Risk Score: {risk_score}%")
    print(f"🤖 Status: {status}")
    print(f"➡ Recommendation: {recommendation}")

    print("-" * 60)


    # Save to CSV
    with open("data_log.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            digital_twin["temperature"],
            digital_twin["smoke"],
            digital_twin["power"],
            digital_twin["gas"],
            digital_twin["co2"],
            digital_twin["water_leak"],
            digital_twin["motion"],
            digital_twin["humidity"],
            risk_score,
            status,
            recommendation
        ])


    time.sleep(2)
