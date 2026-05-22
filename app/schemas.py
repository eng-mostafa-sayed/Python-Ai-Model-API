from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """Request body for the prediction endpoint."""

    study_hours: float
    attendance_percentage: float
    previous_grade: float
