# data/generate_sample_data.py
import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

def create_sample(n=200):
    rng = np.random.RandomState(42)
    feature_1 = rng.normal(0,1,n)
    feature_2 = rng.normal(5,2,n)
    feature_3 = rng.uniform(0,10,n)
    # synthetic label (binary)
    logit = 0.3*feature_1 - 0.2*feature_2 + 0.05*feature_3
    prob = 1/(1+np.exp(-logit))
    label = (prob > 0.5).astype(int)
    df = pd.DataFrame({
        "feature_1": feature_1,
        "feature_2": feature_2,
        "feature_3": feature_3,
        "label": label
    })
    df.to_csv("data/sample_transactions.csv", index=False)
    print("Wrote data/sample_transactions.csv")

if __name__ == "__main__":
    create_sample(500)
