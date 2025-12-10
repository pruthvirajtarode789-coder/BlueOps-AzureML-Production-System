# Deploy guide (minimal)

## Option A — Docker push to any registry & run container
1. Build:
   docker build -t <your-registry>/blueops:latest .
2. Push and run in cloud provider.

## Option B — Azure Container Instance / Azure ML
1. Build image (or use Azure ML CLI).
2. Make sure `models/blueops_model.pkl` is added to the image.
3. Use `deploy/score.py` as the entrypoint and expose port 8000.

## Option C — Render / Heroku (similar)
- Use the Dockerfile and ensure PORT env / CMD adapt. For Render, set start command to `uvicorn api.app:app --host 0.0.0.0 --port 8000`.
