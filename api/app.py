# api/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from api.model_manager import ModelManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BlueOps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model manager (loads model from models/)
model_manager = ModelManager(model_path="models/blueops_model.pkl")

class PredictRequest(BaseModel):
    # adapt fields to your feature set
    feature_1: float
    feature_2: float
    feature_3: float

class PredictResponse(BaseModel):
    prediction: int
    probability: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    features = [req.feature_1, req.feature_2, req.feature_3]
    pred, prob = model_manager.predict(features)
    return {"prediction": int(pred), "probability": float(prob)}
