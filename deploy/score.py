# deploy/score.py
import json
import joblib
import os
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
MODEL = None

def load_model():
    global MODEL
    MODEL = joblib.load(os.path.join(os.getcwd(), "models", "blueops_model.pkl"))

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/predict", methods=["POST"])
def predict():
    global MODEL
    if MODEL is None:
        load_model()
    data = request.get_json(force=True)
    # expects features in body
    arr = np.array([data.get("feature_1",0), data.get("feature_2",0), data.get("feature_3",0)]).reshape(1,-1)
    pred = int(MODEL.predict(arr)[0])
    prob = float(MODEL.predict_proba(arr)[0].max())
    return jsonify({"prediction": pred, "probability": prob})

if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000)
