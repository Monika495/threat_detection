import subprocess
import time
import os

# Step 1: Run sniffer
print("🚀 Starting Real-Time Sniffer...")
sniffer = subprocess.Popen(["python", "realtime_sniffer.py"])

# Give sniffer 2 seconds to start
time.sleep(2)

# Step 2: Run Flask dashboard
print("🌐 Starting Flask Dashboard...")
dashboard = subprocess.Popen(["python", "app.py"])

# Step 3: Wait for both to finish (they won't until you stop them manually)
try:
    sniffer.wait()
    dashboard.wait()
except KeyboardInterrupt:
    print("\n🛑 Stopping everything...")
    sniffer.terminate()
    dashboard.terminate()
