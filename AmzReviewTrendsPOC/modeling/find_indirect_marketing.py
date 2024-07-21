# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:28:41 2024

@author: fs.egb
"""
import os
import pandas as pd
from pathlib import Path
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import plotly.io as pio
import json
#from umap import UMAP
from dotenv import load_dotenv


import openai


# Load environment variables from .env file
load_dotenv()

# Define the base directory
HERE = Path(os.getcwd()).parent.parent

def load_data(file_path):
    """Load the DataFrame from a pickle file."""
    return pd.read_pickle(file_path)

def extract_texts(df):
    """Extract the 'text' column from the DataFrame and convert to a list of strings."""
    return df['text'].astype(str).tolist()

def initialize_topic_model():
    """Initialize the BERTopic model with a CountVectorizer."""
    vectorizer_model = CountVectorizer(stop_words="english")
    return BERTopic(vectorizer_model=vectorizer_model)

def fit_topic_model(topic_model, texts):
    """Fit the BERTopic model on the texts."""
    topics, probabilities = topic_model.fit_transform(texts)
    return topics, probabilities

def reduce_outliers(topic_model, texts, topics):
    """Reduce outliers in the topic model."""
    return topic_model.reduce_outliers(texts, topics)


def Load_topics(HERE):
    topics_path =  HERE/"models"/ "bert_basic" /"topics.json"

    # Open and load the JSON file
    try:
        with open(topics_path, 'r') as file:
            topics_data = json.load(file)
        
    except FileNotFoundError:
        print("File not found. Please check the provided path.")
        
    return topics_data


# Load the DataFrame
df = load_data(HERE / "data" / "raw" / "hist_review_data.pkl")


 
topics_data = Load_topics(HERE)
    
    






# Path to the JSON file containing topics
topics_path = '/path/to/your/models/bert_basic/topics.json'


prompt="Correct this to standard English:\n\nShe no went to the market.",


openai.api_key = os.environ.get("OPENAI_KEY")


response = openai.Completion.create(
  model="code-davinci-002",
  prompt=  prompt,
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)




                                      
                                      
