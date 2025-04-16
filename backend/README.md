# Movie Sentiment Analysis Backend

FastAPI-based backend service for movie sentiment analysis.

## API Endpoints

### GET /

- Root endpoint
- Returns API information

### POST /analyze

- Analyze sentiment of a single review
- Request body:

```json
{
  "text": "Your movie review text here"
}
```

- Response:

```json
{
  "sentiment": "positive|negative",
  "confidence": 0.95
}
```

### POST /analyze-batch

- Analyze sentiment of multiple reviews
- Request body:

```json
{
  "reviews": ["First review text", "Second review text"]
}
```

- Response:

```json
{
  "results": [
    {
      "sentiment": "positive",
      "confidence": 0.95
    },
    {
      "sentiment": "negative",
      "confidence": 0.88
    }
  ]
}
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the server:

```bash
python app.py
```

The server will start on `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

No environment variables are required for basic operation.

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Success
- 500: Server error (with error details in response)
