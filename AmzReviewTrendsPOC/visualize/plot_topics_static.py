
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:00:00 2024

Author: fs.egb

Description: This script loads a previously saved BERTopic model and 

plots statics figures of the topics
"""

import os
from pathlib import Path
from bertopic import BERTopic
import pandas as pd
import plotly.io as pio

# Define the base directory
HERE = Path(os.getcwd()).parent.parent

def load_topic_model(model_path, embedding_model):
    """Load the BERTopic model from the specified path."""
    return BERTopic.load(model_path, embedding_model=embedding_model)

def load_data(file_path):
    """Load the DataFrame from a pickle file."""
    return pd.read_pickle(file_path)

def transform_texts(topic_model, texts):
    """Transform new texts using the loaded topic model."""
    topics, probabilities = topic_model.transform(texts)
    return topics, probabilities

# def visualize_topics(topic_model, file_path):
#     """Visualize the topics and save the visualization as an HTML file."""
#     fig = topic_model.visualize_topics()
#     pio.write_html(fig, file=file_path, auto_open=True)






def main():
    # Paths
    model_path = HERE / "models" / "bert_basic"
    embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
    data_file_path = HERE / "data" / "raw" / "hist_review_data.pkl"
    output_html_path = HERE / "reports" / "figures" / "bert_topics_loaded.html"

    # Load the BERTopic model
c
    
    
    
    # Visualize the topics
    html_file_path = HERE / "reports" / "figures" / "bert_topics_static.html"
    
    fig = topic_model.visualize_topics()
    visualize_topics(topic_model, html_file_path)
    
    
    
    

    # # Load the DataFrame
    # df = load_data(data_file_path)

    # # Extract the 'text' column
    # texts = df['text'].astype(str).tolist()

    # # Transform the texts using the loaded model
    # topics, probabilities = transform_texts(topic_model, texts)

    # # Save the resulting topics and probabilities to the DataFrame
    # df['topic_loaded'] = topics
    # df['probability_loaded'] = probabilities

    # # Print the topics
    # topic_info = topic_model.get_topic_info()
    # print(topic_info)

    # # Visualize the topics
    # fig = visualize_topics(topic_model, output_html_path)

# if __name__ == "__main__":
#     main()
