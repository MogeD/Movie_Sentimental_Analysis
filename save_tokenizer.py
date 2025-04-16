import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from utils import save_tokenizer

def main():
    # Load the dataset
    df = pd.read_csv('data/movie.csv')
    
    # Initialize and fit tokenizer
    tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
    tokenizer.fit_on_texts(df['text'])
    
    # Save the tokenizer
    save_tokenizer(tokenizer)
    print("Tokenizer saved successfully!")

if __name__ == "__main__":
    main() 