from utils import SentimentAnalyzer

def main():
    # Initialize the sentiment analyzer
    analyzer = SentimentAnalyzer()
    
    # Example reviews
    reviews = [
        "This movie was absolutely fantastic! The acting was superb and the plot was engaging.",
        "I was really disappointed with this film. The story was confusing and the acting was poor.",
        "The movie had its moments, but overall it was just okay. Not great, not terrible.",
        "One of the best films I've seen this year. The cinematography was stunning!",
        "Waste of time and money. The plot made no sense and the characters were unlikable."
    ]
    
    # Analyze each review
    print("\nSentiment Analysis Results:")
    print("-" * 50)
    for review in reviews:
        sentiment, confidence = analyzer.predict_sentiment(review)
        print(f"\nReview: {review}")
        print(f"Sentiment: {sentiment}")
        print(f"Confidence: {confidence:.2%}")
        print("-" * 50)

if __name__ == "__main__":
    main() 