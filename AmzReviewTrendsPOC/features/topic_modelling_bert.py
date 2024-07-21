# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:54:23 2024

Author: fs.egb

Description: This script processes historical review data using BERTopic for topic modeling. 
It loads the data, fits a BERTopic model, reduces outliers, saves the resulting topics, 
and visualizes the topics.



This is for the whole sample!
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

def save_dataframe(df, file_path):
    """Save the DataFrame with topics to a pickle file."""
    df.to_pickle(file_path)

def visualize_topics(topic_model, file_path):
    """Visualize the topics and save the visualization as an HTML file."""
    fig = topic_model.visualize_topics()
    pio.write_html(fig, file=file_path, auto_open=True)

def save_topic_model(topic_model, model_path, embedding_model):
    """Save the BERTopic model."""
    topic_model.save(model_path, serialization="safetensors", save_ctfidf=True, save_embedding_model=embedding_model)




def main():
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

    # Save the resulting topics and probabilities to the DataFrame
    df['topic'] = topics
    df["topics_reduced"] = reduced_topics
    df['probability'] = probabilities

    # Save the DataFrame with topics to a new file
    output_file_path = HERE / "data" / "interim" / "hist_review_data_with_topics.pkl"
    save_dataframe(df, output_file_path)

    # Print the topics
    topic_info = topic_model.get_topic_info()
    print(topic_info)

    # Visualize the topics
    html_file_path = HERE / "reports" / "figures" / "bert_topics.html"
    visualize_topics(topic_model, html_file_path)

    # Save the BERTopic model
    embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
    model_path = HERE / "models" / "bert_basic"
    save_topic_model(topic_model, model_path, embedding_model)

if __name__ == "__main__":
    main()

