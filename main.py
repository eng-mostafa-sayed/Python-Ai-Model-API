from fastapi import FastAPI

from app.model_service import predict_iris
from app.schemas import PredictionRequest


app = FastAPI(
    title="Local AI Model API",
    description="A simple FastAPI project for serving an AI model locally.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """Return a simple status message for the API."""
    return {
        "status": "ok",
        "message": "Local AI Model API is running",
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    """Run prediction on the features sent in the API request."""
    return predict_iris(request.features)
