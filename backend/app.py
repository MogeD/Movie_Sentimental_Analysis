from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sys
import os

# Add the parent directory to the path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import SentimentAnalyzer

app = FastAPI(
    title="Movie Sentiment Analysis API",
    description="API for analyzing sentiment in movie reviews using LSTM and GloVe embeddings",
    version="1.0.0"
)

# Add CORS middleware with more permissive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=False,  # Must be False for allow_origins=["*"]
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the sentiment analyzer
analyzer = SentimentAnalyzer()

class Review(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

class BatchReview(BaseModel):
    reviews: List[str]

class BatchResponse(BaseModel):
    results: List[SentimentResponse]

@app.get("/")
async def root():
    return {"message": "Movie Sentiment Analysis API"}

@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(review: Review):
    try:
        sentiment, confidence = analyzer.predict_sentiment(review.text)
        return SentimentResponse(sentiment=sentiment, confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-batch", response_model=BatchResponse)
async def analyze_batch_sentiment(batch: BatchReview):
    try:
        results = []
        for review in batch.reviews:
            sentiment, confidence = analyzer.predict_sentiment(review)
            results.append(SentimentResponse(sentiment=sentiment, confidence=confidence))
        return BatchResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 