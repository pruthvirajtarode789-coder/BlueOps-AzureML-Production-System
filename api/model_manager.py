# api/model_manager.py
import joblib
import os
import numpy as np
from typing import Tuple

class ModelManager:
    def __init__(self, model_path="models/blueops_model.pkl"):
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}. Run training first.")
        self.model = joblib.load(self.model_path)

    def predict(self, features) -> Tuple[int, float]:
        # features: list or array
        arr = np.array(features).reshape(1, -1)
        pred = int(self.model.predict(arr)[0])
        prob = float(self.model.predict_proba(arr)[0].max())
        return pred, prob
