import time
import random
import csv
import os
from datetime import datetime

# Colored output for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def get_status_color(status):
    """Return color based on status"""
    if status == "DANGER":
        return Colors.RED + Colors.BOLD
    elif status == "WARNING":
        return Colors.YELLOW + Colors.BOLD
    else:
        return Colors.GREEN + Colors.BOLD

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

print(f"\n{Colors.CYAN}{Colors.BOLD}╔════════════════════════════════════╗{Colors.RESET}")
print(f"{Colors.CYAN}{Colors.BOLD}║    🛡️  VirtuSafe+ Backend Started   ║{Colors.RESET}")
print(f"{Colors.CYAN}{Colors.BOLD}╚════════════════════════════════════╝{Colors.RESET}\n")

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
counter = 0
while True:
    counter += 1

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


    # Animated Terminal Output
    print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
    print(f"{Colors.HEADER}{Colors.BOLD}📊 VirtuSafe+ Monitoring - Cycle #{counter}{Colors.RESET}")
    print(f"{Colors.BOLD}⏱ Time: {Colors.CYAN}{timestamp}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")

    print(f"{Colors.BLUE}🌡 Temperature:{Colors.RESET} {Colors.YELLOW}{digital_twin['temperature']:.2f}°C{Colors.RESET}")
    print(f"{Colors.BLUE}💨 Smoke Level:{Colors.RESET} {Colors.YELLOW}{digital_twin['smoke']:.2f}{Colors.RESET}")
    print(f"{Colors.BLUE}⚡ Power Usage:{Colors.RESET} {Colors.YELLOW}{digital_twin['power']:.2f} kW{Colors.RESET}")
    print(f"{Colors.BLUE}🌫 Gas Level:{Colors.RESET} {Colors.YELLOW}{digital_twin['gas']:.2f}%{Colors.RESET}")
    print(f"{Colors.BLUE}💨 CO2 Level:{Colors.RESET} {Colors.YELLOW}{digital_twin['co2']:.0f} ppm{Colors.RESET}")
    print(f"{Colors.BLUE}💧 Water Leak:{Colors.RESET} {Colors.RED if digital_twin['water_leak'] == 1 else Colors.GREEN}{'🚨 YES' if digital_twin['water_leak'] == 1 else '✓ NO'}{Colors.RESET}")
    print(f"{Colors.BLUE}🚶 Motion:{Colors.RESET} {Colors.RED if digital_twin['motion'] == 1 else Colors.GREEN}{'🔴 DETECTED' if digital_twin['motion'] == 1 else '⚪ NONE'}{Colors.RESET}")
    print(f"{Colors.BLUE}💦 Humidity:{Colors.RESET} {Colors.YELLOW}{digital_twin['humidity']:.1f}%{Colors.RESET}")

    print(f"\n{Colors.BOLD}{'─'*60}{Colors.RESET}")
    print(f"{Colors.BOLD}📊 Risk Score:{Colors.RESET} {get_status_color(status)}{risk_score}%{Colors.RESET}")
    print(f"{Colors.BOLD}🤖 AI Status:{Colors.RESET} {get_status_color(status)}{status}{Colors.RESET}")
    print(f"{Colors.BOLD}➡ Recommendation:{Colors.RESET} {Colors.CYAN}{recommendation}{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")


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
