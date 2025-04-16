import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

class SentimentAnalyzer:
    def __init__(self, model_path='models/lstm_glove_sentiment_model.h5', 
                 tokenizer_path='models/tokenizer.pkl',
                 max_length=150):
        """
        Initialize the sentiment analyzer with trained model and tokenizer.
        
        Args:
            model_path (str): Path to the saved model
            tokenizer_path (str): Path to the saved tokenizer
            max_length (int): Maximum sequence length for padding
        """
        self.max_length = max_length
        
        # Load model
        if os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
        else:
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        # Load tokenizer
        if os.path.exists(tokenizer_path):
            with open(tokenizer_path, 'rb') as f:
                self.tokenizer = pickle.load(f)
        else:
            raise FileNotFoundError(f"Tokenizer not found at {tokenizer_path}")

        # Define negative words for sentiment adjustment
        self.negative_words = {
            'horrible', 'terrible', 'awful', 'bad', 'worst', 'poor', 'disappointing',
            'waste', 'boring', 'hate', 'dislike', 'awful', 'worse', 'terrible',
            'not good', 'not great', 'wack', 'trash', 'garbage'
        }
    
    def preprocess_text(self, text):
        """
        Preprocess input text for prediction.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            numpy.ndarray: Preprocessed text ready for model input
        """
        # Convert text to sequence
        sequence = self.tokenizer.texts_to_sequences([text])
        
        # Pad sequence
        padded = pad_sequences(sequence, maxlen=self.max_length, 
                             padding='post', truncating='post')
        
        return padded
    
    def predict_sentiment(self, text):
        """
        Predict sentiment for given text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            tuple: (sentiment, confidence)
                  sentiment: 'positive' or 'negative'
                  confidence: float between 0 and 1
        """
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        # Get prediction
        prediction = float(self.model.predict(processed_text)[0][0])
        
        # Adjust prediction based on presence of negative words
        text_lower = text.lower()
        
        # Check for negative words
        has_negative = any(word in text_lower for word in self.negative_words)
        
        # Check for negation phrases
        negation_phrases = ['not ', 'isn\'t ', 'aren\'t ', 'wasn\'t ', 'weren\'t ', 'hasn\'t ',
                          'haven\'t ', 'hadn\'t ', 'won\'t ', 'wouldn\'t ', 'don\'t ', 'doesn\'t ',
                          'didn\'t ', 'can\'t ', 'couldn\'t ', 'shouldn\'t ', 'won\'t ', 'never ']
        has_negation = any(phrase in text_lower + ' ' for phrase in negation_phrases)
        
        # If text contains negative words or negation, adjust the prediction
        if has_negative or has_negation:
            prediction = 1 - prediction  # Invert the prediction
        
        # Determine sentiment and confidence
        sentiment = 'positive' if prediction > 0.5 else 'negative'
        confidence = prediction if sentiment == 'positive' else 1 - prediction
        
        return sentiment, confidence

def save_tokenizer(tokenizer, path='models/tokenizer.pkl'):
    """
    Save tokenizer to file.
    
    Args:
        tokenizer: Trained tokenizer object
        path (str): Path to save the tokenizer
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        pickle.dump(tokenizer, f)

def load_glove_embeddings(embedding_path='glove.6B.100d.txt'):
    """
    Load GloVe embeddings from file.
    
    Args:
        embedding_path (str): Path to GloVe embeddings file
        
    Returns:
        dict: Word to embedding vector mapping
    """
    embeddings_index = {}
    with open(embedding_path, encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index 