# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:54:23 2024

@author: fs.egb
"""

import os
import pandas as pd
from pathlib import Path
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import plotly.io as pio



HERE = Path(os.getcwd()).parent.parent




# Load the DataFrame
df = pd.read_pickle(HERE/ "data"/"raw"/ "hist_review_data.pkl")


# # Extract the 'text' column
# texts = df['text'].astype(str).tolist()

# # Initialize BERTopic
# vectorizer_model = CountVectorizer(stop_words="english")
# topic_model = BERTopic(vectorizer_model=vectorizer_model)





# # # Fit the model on the texts
# topics, probabilities = topic_model.fit_transform(texts)




# # Reduce outliers ( i.e. the -1 topic)
# reduced_topics = topic_model.reduce_outliers(texts, topics)



# # # Save the resulting topics and probabilities to the DataFrame
# df['topic'] = topics
# df["topics_reduced"] = reduced_topics
# df['probability'] = probabilities
# # Save the DataFrame with topics to a new file
# output_file_path = os.path.join(HERE, "data", "interim", "hist_review_data_with_topics.pkl")
# df.to_pickle(output_file_path)



# # # Print the topics
# t = topic_model.get_topic_info()


# fig = topic_model.visualize_topics()
# html_file_path = HERE/"reports"/"figures"/"bert_topics.html"

# pio.write_html(fig, file=html_file_path, auto_open=True)


# embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
# topic_model.save( HERE/"models"/"bert_basic", serialization="safetensors", save_ctfidf=True, save_embedding_model=embedding_model)



