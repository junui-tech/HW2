from textblob import TextBlob

class SentimentPredictor:
    def __init__(self, neutral_threshold: float = 0.05):
        """
        Initialize the sentiment Predictor.
        In a real MLOps pipeline, this is where you might load a trained PyTorch/TensorFlow model from disk or MLflow.
        """
        self.neutral_threshold = neutral_threshold

    def predict(self, text: str) -> dict:
        """
        Perform inference on the input text after autocorrecting typos.
        """
        # 1. 문장 교정 (Autocorrect)
        original_blob = TextBlob(text)
        corrected_blob = original_blob.correct()
        corrected_text = str(corrected_blob)
        
        # 2. 교정된 문장 기준으로 감성 분석 진행
        polarity = corrected_blob.sentiment.polarity
        subjectivity = corrected_blob.sentiment.subjectivity
        
        if polarity > self.neutral_threshold:
            sentiment = "positive"
        elif polarity < -self.neutral_threshold:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        return {
            "text": text,
            "corrected_text": corrected_text,
            "polarity": polarity,
            "sentiment": sentiment,
            "subjectivity": subjectivity
        }

# Instantiate a single predictor to be reused across requests (useful for caching/heavy models)
sentiment_predictor = SentimentPredictor()
