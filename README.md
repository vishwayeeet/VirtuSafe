# VirtuSafe+

An AI-powered Digital Twin system for building safety monitoring and risk assessment.

## Overview

VirtuSafe+ is a comprehensive safety management platform that uses AI-driven risk assessment to monitor multiple environmental parameters in real-time. It combines IoT sensor data with machine learning algorithms to detect potential hazards and provide actionable safety insights.

## Features

- **Digital Twin Simulation**: Real-time monitoring of multiple sensors including:
  - Temperature monitoring
  - Smoke detection
  - Power consumption tracking
  - Gas level monitoring
  - CO2 level tracking
  - Water leak detection
  - Motion detection
  - Humidity monitoring

- **AI Risk Engine**: Intelligent risk scoring system that evaluates multiple parameters and assigns risk levels
- **Dashboard Interface**: Interactive Streamlit-based dashboard for visualization and monitoring
- **Data Logging**: Historical data tracking in CSV format for analysis and reporting

## Project Structure

```
├── main.py           # Backend digital twin simulation and AI risk engine
├── dashboard.py      # Streamlit web dashboard for visualization
├── data_log.csv      # Historical sensor data and logs
├── README.md         # Project documentation
└── .gitignore        # Git ignore configuration
```

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- CSV module (built-in)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vishwayeeet/VirtuSafe.git
cd VirtuSafe
```

2. Install dependencies:
```bash
pip install streamlit pandas
```

## Usage

1. Start the backend (data generation and logging):
```bash
python main.py
```

2. In another terminal, launch the dashboard:
```bash
streamlit run dashboard.py
```

3. Open your browser and navigate to the dashboard URL (typically `http://localhost:8501`)

## How It Works

- **Backend (main.py)**: Simulates IoT sensors and runs the AI decision engine to calculate risk scores based on sensor readings
- **Dashboard (dashboard.py)**: Provides a real-time visualization interface with status indicators and alerts
- **Data Logging**: All sensor readings and risk assessments are logged to `data_log.csv` for historical analysis

## Risk Assessment

The AI risk engine evaluates multiple parameters:
- High temperature (>60°C)
- High smoke levels (>40 ppm)
- High gas levels (>70 ppm)
- Elevated CO2 (>1500 ppm)
- Water leaks
- Motion detection
- High humidity (>80%)

## Author

Vishwajeet Kumar

## License

MIT License
