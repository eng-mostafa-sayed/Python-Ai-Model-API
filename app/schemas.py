from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """Request body for the prediction endpoint."""

    text: str
