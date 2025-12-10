# training/data_prep.py
import pandas as pd
import numpy as np
import os

def load_sample(path="data/sample_transactions.csv"):
    return pd.read_csv(path)

def prepare_features(df):
    # Very small example — replace with real feature engineering
    X = df[["feature_1","feature_2","feature_3"]].fillna(0)
    y = df["label"]
    return X, y

if __name__ == "__main__":
    print("Run generate_sample_data.py to create data.")
