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
        Perform inference on the input text.
        """
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        
        if polarity > self.neutral_threshold:
            sentiment = "positive"
        elif polarity < -self.neutral_threshold:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        return {
            "text": text,
            "polarity": polarity,
            "sentiment": sentiment
        }

# Instantiate a single predictor to be reused across requests (useful for caching/heavy models)
sentiment_predictor = SentimentPredictor()
