from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs")
def logs():
    df = pd.read_csv("logs/network_logs.csv")
    return jsonify(df.tail(50).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
