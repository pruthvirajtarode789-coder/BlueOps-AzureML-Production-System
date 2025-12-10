# BlueOps — Azure ML Production System (Client-ready)

BlueOps is a production-ready MLOps demo: end-to-end pipeline from data -> training -> model -> REST API -> Streamlit UI -> Azure ML deployment.

## Features
- Synthetic/real dataset generator for quick demos
- Training script producing a scikit-learn model (`models/blueops_model.pkl`)
- FastAPI server (serves `/predict` and `/health`)
- Streamlit UI for demo & admin
- Dockerfile + Azure ML scoring script + conda env for deployment
- Docs & diagrams in `docs/`

## Quick local run (dev)

### 1. Create and activate venv:
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Generate sample data and train:
```bash
python data/generate_sample_data.py
python training/train_model.py
```

This writes `models/blueops_model.pkl`.

### 3. Start the API:
```bash
uvicorn api.app:app --reload --port 8000
```

Test with:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"feature_1\":0.1,\"feature_2\":5.0,\"feature_3\":1.2}"
```

### 4. Start the UI (in separate shell):
```bash
streamlit run app/streamlit_app.py
```

UI connects to API URL `http://127.0.0.1:8000` by default.

## Docker & Deploy

Dockerfile included. Build image and test:
```bash
docker build -t blueops-app:latest .
docker run -p 8501:8501 blueops-app:latest      # depends on ENTRYPOINT
```

Azure ML deployment steps & `deploy/` content (`score.py`, conda env) included — see `deploy/README_DEPLOY.md`.

## Files overview

- **api/** — FastAPI service
- **app/** — Streamlit frontend
- **training/** — training pipeline
- **deploy/** — azure scoring, conda env for model deployment
- **models/** — saved model artifacts
- **data/** — data generator
- **docs/** — documentation and diagrams

## Notes

- Replace synthetic data with your real datasets for production.
- Add logging, monitoring, model versioning (MLflow, Azure Model Registry) for enterprise readiness.

---

## Quick Azure ML (CLI) deployment guide (high-level)

### Option A — Deploy container to Azure Container Instance (quick)
1. Build image and push to Azure Container Registry (ACR).
2. Create ACI from image; set port 8000. (Use Azure Portal or `az container create`).

### Option B — Deploy model via Azure ML CLI v2 (recommended enterprise)
1. Install Azure CLI and Azure ML extension:
   ```bash
   az login
   az extension add -n ml
   ```

2. Register model (if you want to use Azure ML Model registry):
   ```bash
   az ml model create -n blueops_model --path models/blueops_model.pkl --type custom_model
   ```

3. Create inference configuration using `deploy/conda_env.yml` and `deploy/score.py`.
4. Use `az ml online-endpoint create` and `az ml online-deployment create` commands to deploy the container.

See Azure ML docs for exact CLI commands — they are straightforward and present many options.

---

**Next steps:** Copy files, create venv, run local checklist above, and deploy!
