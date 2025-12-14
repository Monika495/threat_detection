from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import joblib
from datetime import datetime
import csv
import os

model = joblib.load("threat_detection_model.pkl")

LOG_FILE = "logs/network_logs.csv"

# Create logs folder and file if not exist
if not os.path.exists("logs"):
    os.mkdir("logs")

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Source", "Destination", "Protocol", "Size", "Status", "Level"])

def analyze(packet):
    if packet.haslayer(IP):
        proto = "Other"
        if packet.haslayer(TCP): proto = "TCP"
        elif packet.haslayer(UDP): proto = "UDP"

        size = len(packet)

        df = pd.DataFrame([{
            "packet_size": size,
            "protocol_TCP": 1 if proto == "TCP" else 0,
            "protocol_UDP": 1 if proto == "UDP" else 0,
            "protocol_Other": 1 if proto == "Other" else 0
        }])

        prediction = model.predict(df)[0]

        status = "SAFE"
        level = "Low"

        if prediction == 1:
            status = "THREAT"
            if size > 1000:
                level = "High"
            elif size > 500:
                level = "Medium"

        print(f"[{status}] {proto} | Size: {size} | Level: {level}")

        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now(),
                packet[IP].src,
                packet[IP].dst,
                proto,
                size,
                status,
                level
            ])

print("🚀 Real-Time Monitoring Started...")
sniff(prn=analyze, store=False)
