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



# Load the DataFrame
df = load_data(HERE / "data" / "raw" / "hist_review_data.pkl")

# Extract the 'text' column
texts = extract_texts(df)

# Initialize BERTopic
topic_model = initialize_topic_model()

# Fit the model on the texts
topics, probabilities = fit_topic_model(topic_model, texts)

# Reduce outliers
reduced_topics = reduce_outliers(topic_model, texts, topics)





# Find the topics that Qualify for 