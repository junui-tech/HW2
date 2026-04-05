from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    polarity: float
    sentiment: str
    subjectivity: float
