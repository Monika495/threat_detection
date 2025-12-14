import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Create sample training data
data = {
    "packet_size": np.random.randint(40, 1500, 1000),
    "protocol_TCP": np.random.randint(0, 2, 1000),
    "protocol_UDP": np.random.randint(0, 2, 1000),
    "protocol_Other": np.random.randint(0, 2, 1000),
    "is_threat": np.random.randint(0, 2, 1000)
}

df = pd.DataFrame(data)

X = df.drop("is_threat", axis=1)
y = df["is_threat"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "threat_detection_model.pkl")
print("✅ Model trained and saved successfully")
