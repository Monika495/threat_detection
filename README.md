# 🚀 Real-Time IoT Threat Detection System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Flask-Dashboard-green?style=for-the-badge&logo=flask" alt="Flask">
</p>

<p align="center">
  <b>AI-Powered Network Security • Real-Time Detection • Live Dashboard</b>
</p>

---

## 📋 Quick Navigation

| [🎯 Overview](#-overview) | [⚙️ How It Works](#️-how-it-works) | [🛠️ Tech Stack](#️-tech-stack) | [📁 Structure](#-structure) | [🚀 Quick Start](#-quick-start) |
|:---:|:---:|:---:|:---:|:---:|

---

## 🎯 Overview

A lightweight system that **watches network traffic in real-time**, uses **AI to detect threats**, and shows results on a **live dashboard**.

### ✨ What It Does

```python
✅ Listens to live network packets
✅ Classifies each packet as SAFE or THREAT using AI
✅ Assigns severity levels (Low/Medium/High)
✅ Displays everything on auto-refreshing dashboard
✅ Saves all data for later analysis
```

---

## ⚠️ The Problem It Solves

| Challenge | Our Solution |
|-----------|--------------|
| 🔴 IoT devices always connected | 🟢 24/7 monitoring |
| 🔴 Attacks during data flow | 🟢 Real-time detection |
| 🔴 Logs show damage after attack | 🟢 Proactive alerts |
| 🔴 Complex security setups | 🟢 Simple Python solution |

---

## ⚙️ How It Works

### Simple 3-Step Process

```
📡 STEP 1: CAPTURE
Network packets → Scapy sniffer

🤖 STEP 2: ANALYZE
AI Model (Random Forest) → SAFE or THREAT

📊 STEP 3: DISPLAY
Live Dashboard → Color-coded results
```

### What is a "Threat" Here?

> **Simple meaning:** A packet that looks abnormal (unusual size or pattern) compared to normal traffic. It's a **warning sign** to watch, not a confirmed attack.

---

## 🛠️ Tech Stack

| Technology | What It Does |
|------------|--------------|
| **Python** | Core programming |
| **Scapy** | Captures live packets |
| **Scikit-learn** | AI/ML framework |
| **Random Forest** | Threat classification |
| **Flask** | Dashboard backend |
| **HTML/CSS/JS** | Frontend display |
| **CSV** | Stores all logs |

---

## 📁 Structure

```
threat_detection/
│
├── 📄 app.py                 # Flask dashboard
├── 📄 realtime_sniffer.py     # Live packet capture
├── 📄 run_project.py          # One-click launcher
├── 📄 train_model.py          # Trains AI model
├── 📦 threat_detection_model.pkl  # Trained AI
│
├── 📂 templates/
│   └── 📄 index.html         # Dashboard UI
│
└── 📂 logs/
    └── 📄 network_logs.csv    # All detections
```

---

## 🚀 Quick Start

### 1️⃣ One Command (Everything)
```bash
python run_project.py
```

### 2️⃣ Step-by-Step
```bash
# Train model (first time only)
python train_model.py

# Start sniffer (terminal view)
python realtime_sniffer.py

# Launch dashboard (browser)
python app.py
```

### 3️⃣ View Dashboard
```
🌐 Open: http://127.0.0.1:5000
```

---

## 📊 Live Dashboard Features

```
┌─────────────────────────────────────┐
│    REAL-TIME THREAT DASHBOARD       │
├──────────┬──────────┬───────────────┤
│ Time     │ Status   │ Threat Level  │
├──────────┼──────────┼───────────────┤
│ 10:15:23 │ 🟢 SAFE  │ Low           │
│ 10:15:24 │ 🔴 THREAT│ High          │
│ 10:15:25 │ 🟢 SAFE  │ Low           │
└──────────┴──────────┴───────────────┘
✨ Auto-refreshes every 2 seconds
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Real-Time** | Analyzes packets instantly |
| **AI-Powered** | Random Forest classification |
| **Live Dashboard** | Updates every 2 seconds |
| **Threat Levels** | Low/Medium/High severity |
| **Data Logging** | All results saved to CSV |

---

## 📝 Notes

- ✅ Works on Windows/Linux/Mac
- ✅ No complex setup required
- ✅ Lightweight (runs on any laptop)
- ✅ Perfect for learning & demo

---

<p align="center">
  <b>Made with ❤️ for IoT Security</b><br>
  <sub>⭐ Star this repo if you find it useful!</sub>
</p>
