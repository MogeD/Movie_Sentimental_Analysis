# Movie Sentiment Analyzer

A powerful sentiment analysis system that helps movie industry professionals, streaming platforms, and content aggregators make data-driven decisions through AI-powered review analysis.

![Movie Sentiment Analyzer](docs/screenshot.png)

## Business Value

### Key Benefits

- **Real-time Analysis**: Process thousands of movie reviews instantly
- **Cost Efficiency**: Reduce manual review processing time and costs
- **Data-Driven Insights**: Make informed decisions based on audience sentiment
- **Scalable Solution**: Handle growing review volumes with ease

### Industry Applications

#### Movie Studios & Production Companies

- Understand audience reception
- Identify successful movie elements
- Optimize marketing strategies
- Make data-driven production decisions

#### Streaming Platforms

- Enhance content recommendation systems
- Improve content categorization
- Track audience sentiment trends
- Make informed content acquisition decisions

#### Review Aggregators

- Automate review analysis
- Provide accurate audience scores
- Scale review processing capabilities
- Generate comprehensive sentiment reports

## Technical Overview

### Core Features

- Deep learning model using LSTM and GloVe word embeddings
- Real-time sentiment analysis with confidence scoring
- Analysis history tracking
- Modern, responsive UI
- RESTful API backend
- Pre-trained deep learning model

### Technical Stack

#### Backend

- Python 3.8+
- TensorFlow 2.x for deep learning
- FastAPI for API service
- GloVe word embeddings (100-dimensional)

#### Frontend

- React 18+
- TypeScript
- Modern UI components
- Real-time API integration

## Model Performance

The sentiment analysis model achieves:

- Accuracy: ~84%
- Precision: 0.86 (negative), 0.82 (positive)
- Recall: 0.81 (negative), 0.87 (positive)
- F1-score: 0.83 (negative), 0.84 (positive)

## Getting Started

### Required Files

Before running the application, download these essential files:

1. GloVe Word Embeddings:

   - Download: [glove.6B.100d.txt](https://nlp.stanford.edu/data/glove.6B.zip)
   - Extract and place `glove.6B.100d.txt` in the project root
   - Size: ~331MB

2. Movie Dataset:

   - Download: [movie.csv](https://drive.google.com/file/your-file-id/view)
   - Place in the `data/` directory
   - Size: ~50MB

3. Pre-trained Model Files:
   - Download: [model_files.zip](https://drive.google.com/file/your-file-id/view)
   - Extract and place:
     - `lstm_glove_sentiment_model.h5` → `backend/models/`
     - `tokenizer.pkl` → `backend/models/`

### Installation

1. Install Git LFS:

```bash
# Windows (with Chocolatey)
choco install git-lfs

# macOS (with Homebrew)
brew install git-lfs

# Linux (Debian/Ubuntu)
sudo apt install git-lfs
```

2. Clone the repository:

```bash
git clone [repository-url]
cd Movie_Sentimental_Analysis
```

3. Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

4. Install frontend dependencies:

```bash
cd ../frontend
npm install
```

## Running the Application

1. Start the backend server:

```bash
cd backend
python app.py
```

API available at `http://localhost:8001`

2. Start the frontend development server:

```bash
cd frontend
npm start
```

Web interface available at `http://localhost:3000`

## API Documentation

Access the API documentation at:

- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

### Main Endpoints

- `POST /analyze`: Analyze a single movie review
  ```json
  {
    "text": "Your movie review here"
  }
  ```

## Development

### Backend Development

```bash
pip install -r requirements-dev.txt
pytest
```

### Frontend Development

```bash
npm install
npm start
npm run build
```

## Future Enhancements

- Aspect-based sentiment analysis (plot, acting, direction)
- Historical trend analysis
- Comparative analysis between movies
- Advanced analytics dashboard
- Batch processing capabilities
- Custom report generation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Your chosen license]

## Acknowledgments

- GloVe word embeddings from Stanford NLP
- Movie review dataset contributors
- Open source community
