🚀 Real-Time IoT Threat Detection System
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Scikit--Learn-ML-orange
https://img.shields.io/badge/Flask-Dashboard-green
https://img.shields.io/badge/Scapy-Packet%2520Sniffer-red

📋 Table of Contents
Overview

Problem Statement

How It Works

Technology Stack

Project Structure

Installation

Usage

Features

How the AI Model Works

Real-Time Dashboard

Contributing

License

🎯 Overview
The Real-Time IoT Threat Detection System is an intelligent network monitoring solution that uses Machine Learning to detect potentially malicious network traffic in real-time. Unlike traditional security systems that analyze logs after attacks occur, this system identifies threats as they happen, providing immediate visibility into network anomalies.

What Makes It Special?
🕒 Real-Time Detection: Analyzes packets the moment they flow through your network

🤖 AI-Powered: Uses Random Forest algorithm to classify traffic patterns

📊 Live Dashboard: Web-based interface showing threats as they occur

🔍 Lightweight: Runs on local machines without complex infrastructure

📈 Severity Scoring: Assigns threat levels (Low/Medium/High) based on packet characteristics

⚠️ Problem Statement
The Challenge
IoT devices and computers are constantly connected to the internet

Cyber attacks can happen during active data transmission

Traditional security systems analyze logs after damage is done

Need for proactive, real-time threat detection

Our Solution
A system that:

Listens to live network traffic

Uses AI to classify packets as SAFE or THREAT

Displays results instantly on an interactive dashboard

Stores historical data for analysis

🔄 How It Works
Step-by-Step Flow






Step 1: AI Model Training (One-time setup)
Random Forest algorithm processes sample network data

Learns patterns from SAFE and THREAT packets

Model saved as threat_detection_model.pkl

Step 2: Live Packet Capture
Scapy library listens to all network interfaces

Captures packets in real-time as they're sent/received

Step 3: Feature Extraction
From each packet, we extract:

📦 Packet size

🔌 Protocol type (TCP/UDP/Other)

🌐 Source & Destination IP addresses

Step 4: AI Classification
Packet features fed into trained model

Instant prediction: SAFE (0) or THREAT (1)

Based on learned patterns from training

Step 5: Threat Level Assignment
Low: Small abnormal packets

Medium: Medium-sized suspicious packets

High: Very large, potentially malicious packets

Step 6: Data Storage
All results saved to logs/network_logs.csv:

Timestamp

Source & Destination IP

Protocol

Status (SAFE/THREAT)

Threat Level

Step 7: Live Dashboard
Flask backend serves real-time data

Auto-refreshing table every 2 seconds

Color-coded threats (Green=SAFE, Red=THREAT)

🛠 Technology Stack
Technology	Purpose
Python 3.8+	Core programming language
Scapy	Live packet capture and manipulation
Scikit-learn	Machine Learning framework
Random Forest	Classification algorithm
Pandas/NumPy	Data processing and analysis
Flask	Web backend and REST API
HTML/CSS/JS	Frontend dashboard
Joblib	Model serialization
Npcap	Windows packet capture driver
📁 Project Structure
text
threat_detection/
│
├── 📄 app.py                    # Flask dashboard server
├── 📄 realtime_sniffer.py        # Live packet capture & analysis
├── 📄 run_project.py             # Launcher for both components
├── 📄 train_model.py             # ML model trainer
├── 📦 threat_detection_model.pkl # Trained AI model
│
├── 📂 templates/
│   └── 📄 index.html             # Dashboard frontend
│
├── 📂 logs/
│   └── 📄 network_logs.csv       # Detected threats log
│
└── 📄 README.md                   # Documentation
💻 Installation
Prerequisites
Python 3.8 or higher

Npcap (Windows) or libpcap (Linux/Mac)

Git

Step-by-Step Setup
Clone the repository

bash
git clone https://github.com/yourusername/iot-threat-detection.git
cd iot-threat-detection
Create virtual environment (recommended)

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Install packet capture driver

Windows: Download and install Npcap

Linux: sudo apt-get install libpcap-dev

Mac: brew install libpcap

Create requirements.txt

txt
scapy
pandas
numpy
scikit-learn
joblib
flask
🚀 Usage
Method 1: Quick Start (All-in-One)
bash
python run_project.py
This launches both the sniffer and dashboard simultaneously.

Method 2: Step-by-Step
Train the AI Model (first time only)

bash
python train_model.py
✅ Expected output: "Model trained and saved successfully"

Start Real-Time Sniffer

bash
python realtime_sniffer.py
🖥️ Terminal shows live packet analysis

Launch Dashboard (in another terminal)

bash
python app.py
🌐 Open browser to http://127.0.0.1:5000

Stopping the System
Press Ctrl+C in any terminal to stop the processes.

✨ Features
Real-Time Detection
Zero-latency packet analysis

Instant classification as packets arrive

Live terminal feedback

Intelligent Classification
SAFE: Normal network behavior

THREAT: Anomalous patterns requiring attention

Severity Levels: Low/Medium/High based on packet size

Interactive Dashboard
Auto-refreshing table (2-second intervals)

Color-coded threats for quick identification

Shows last 50 events

Responsive design for all devices

Data Persistence
All detections logged to CSV

Historical data for analysis

Easy integration with other tools

🤖 How the AI Model Works
Training Data Features
The Random Forest model is trained on:

packet_size: Length of packet in bytes

protocol_TCP: 1 if TCP, else 0

protocol_UDP: 1 if UDP, else 0

protocol_Other: 1 if other protocol, else 0

Threat Detection Logic
The model identifies threats based on:

Unusual packet sizes (too large or too small)

Abnormal protocol combinations

Patterns matching known attack signatures

Sample Training Process
python
# 1000 sample packets with random features
data = {
    "packet_size": 40-1500 bytes,
    "protocol_TCP": 0 or 1,
    "protocol_UDP": 0 or 1,
    "protocol_Other": 0 or 1,
    "is_threat": 0 or 1  # Label
}
📊 Real-Time Dashboard
Dashboard Interface
text
┌─────────────────────────────────────────────────┐
│           IoT Threat Detection Dashboard        │
├──────────┬──────────┬──────────┬──────┬────────┤
│ Time     │ Source   │ Dest     │ Proto│ Status │
├──────────┼──────────┼──────────┼──────┼────────┤
│ 10:15:23 │ 192.168.1.5│ 8.8.8.8 │ TCP  │ SAFE   │
│ 10:15:24 │ 10.0.0.12 │ 1.1.1.1 │ UDP  │ THREAT │
└──────────┴──────────┴──────────┴──────┴────────┘
Color Coding
🟢 Green: SAFE packets

🔴 Red: THREAT packets

🟡 Yellow/Orange: Medium severity threats

🟢 Green text: Low severity

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request
