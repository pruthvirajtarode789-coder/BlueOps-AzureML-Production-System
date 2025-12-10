# training/train_model.py
import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from data_prep import load_sample, prepare_features

os.makedirs("models", exist_ok=True)

def main():
    df = load_sample("data/sample_transactions.csv")
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = LogisticRegression(solver="liblinear")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:,1]
    print(classification_report(y_test, preds))
    try:
        auc = roc_auc_score(y_test, probs)
        print("AUC:", auc)
    except Exception:
        pass
    joblib.dump(model, "models/blueops_model.pkl")
    print("Model saved to models/blueops_model.pkl")

if __name__ == "__main__":
    main()
