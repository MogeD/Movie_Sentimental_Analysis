# Movie Sentiment Analyzer

A modern web application for analyzing sentiment in movie reviews using deep learning, featuring a React frontend and FastAPI backend.

![Movie Sentiment Analyzer](docs/screenshot.png)

## Project Overview

This project implements a sentiment analysis system that can classify movie reviews as positive or negative. It features:

- Deep learning model using LSTM and GloVe word embeddings
- Modern React frontend with TypeScript
- FastAPI backend service
- Real-time sentiment analysis
- Analysis history tracking

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

## Required Files

Before running the application, you need to download some large files that are not included in the repository:

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
   - Extract and place the following files:
     - `lstm_glove_sentiment_model.h5` → `backend/models/`
     - `tokenizer.pkl` → `backend/models/`

## Installation

1. Install Git LFS:

```bash
# Windows (with Chocolatey)
choco install git-lfs

# macOS (with Homebrew)
brew install git-lfs

# Linux (Debian/Ubuntu)
sudo apt install git-lfs
```

2. Clone the repository with Git LFS:

```bash
# Initialize Git LFS
git lfs install

# Clone the repository
git clone [repository-url]
cd Movie_Sentimental_Analysis

# Pull LFS files
git lfs pull
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

5. Download and place the required model files:
   - Place `lstm_glove_sentiment_model.h5` in `backend/models/`
   - Place `tokenizer.pkl` in `backend/models/`

## Running the Application

1. Start the backend server:

```bash
cd backend
python app.py
```

The API will be available at `http://localhost:8001`

2. Start the frontend development server:

```bash
cd frontend
npm start
```

The web interface will be available at `http://localhost:3000`

## Project Structure

```
Movie_Sentimental_Analysis/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── models/             # Trained models directory
│   │   ├── lstm_glove_sentiment_model.h5
│   │   └── tokenizer.pkl
│   └── requirements.txt    # Backend dependencies
├── frontend/
│   ├── src/               # React source code
│   ├── public/            # Static assets
│   └── package.json       # Frontend dependencies
├── models/                # Model training artifacts
├── Word_Embeddings_model.ipynb  # Model training notebook
├── utils.py              # Utility functions
└── README.md             # Project documentation
```

## Features

- Real-time sentiment analysis of movie reviews
- Confidence score for predictions
- Analysis history tracking
- Modern, responsive UI
- RESTful API backend
- Pre-trained deep learning model

## Model Performance

The sentiment analysis model achieves:

- Accuracy: ~84%
- Precision: 0.86 (negative), 0.82 (positive)
- Recall: 0.81 (negative), 0.87 (positive)
- F1-score: 0.83 (negative), 0.84 (positive)

## API Documentation

The API documentation is available at:

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

1. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

2. Run tests:

```bash
pytest
```

### Frontend Development

1. Install dependencies:

```bash
npm install
```

2. Run development server:

```bash
npm start
```

3. Build for production:

```bash
npm run build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- GloVe word embeddings from Stanford NLP
- Movie review dataset contributors
- Open source community
