# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:28:41 2024

@author: fs.egb
"""
import os
import pandas as pd
from pathlib import Path
#from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import plotly.io as pio
import json
#from umap import UMAP
from dotenv import load_dotenv



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

def save_dataframe(df, file_path):
    """Save the DataFrame with topics to a pickle file."""
    df.to_pickle(file_path)


# Load the DataFrame
df = load_data(HERE / "data" / "interim" / "hist_review_data_with_topics.pkl")


 
topics_data = Load_topics(HERE)

relations = [2,3,13]
    
relation_comment = (df.loc[df['topics_reduced'].isin(relations)]
                  
                  #  [['title', 'text']]
                    )
    

output_file_path = HERE / "data" / "interim" / "indirekt_marketing.pkl"


save_dataframe(relation_comment, output_file_path)





                                      
                                      
