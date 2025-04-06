import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Download NLTK resources
nltk.download("vader_lexicon")

def analyze_sentiments(reviews):
    # Initialize analyzers
    sia = SentimentIntensityAnalyzer()
    transformer_analyzer = pipeline("sentiment-analysis")

    data = []
    for review in reviews:
        # NLTK VADER analysis
        vader_scores = sia.polarity_scores(review)
        vader_polarity = "Positive" if vader_scores["compound"] > 0.05 else "Negative" if vader_scores["compound"] < -0.05 else "Neutral"

        # Transformer-based analysis
        transformer_result = transformer_analyzer(review)[0]
        transformer_polarity = transformer_result["label"]
        transformer_score = transformer_result["score"]

        data.append({
            "Review": review,
            "VADER_Score": vader_scores["compound"],
            "VADER_Polarity": vader_polarity,
            "Transformer_Polarity": transformer_polarity,
            "Transformer_Score": transformer_score
        })

    return pd.DataFrame(data)