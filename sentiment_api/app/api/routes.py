from fastapi import APIRouter
from app.schemas.prediction import TextRequest, SentimentResponse
from app.services.sentiment_predictor import sentiment_predictor

router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: TextRequest):
    """
    Analyze the sentiment of the provided English text.
    Returns the polarity (-1.0 to 1.0) and sentiment (positive/negative/neutral).
    """
    # Delegate the actual prediction logic to the service layer
    prediction = sentiment_predictor.predict(request.text)
    return SentimentResponse(**prediction)
