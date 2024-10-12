from textblob import TextBlob

def analyze_review_sentiment(review_text):
    analysis = TextBlob(review_text)
    sentiment = analysis.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
review = "The product quality is amazing!"
sentiment = analyze_review_sentiment(review)
print(f"Review Sentiment: {sentiment}")
