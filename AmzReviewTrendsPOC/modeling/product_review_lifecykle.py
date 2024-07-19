# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:54:15 2024

@author: fs.egb


"""


import os
from pathlib import Path
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import plotly.io as pio

def merge_dataframes(HERE):
    # Define the base directory
    

    # Define the file paths
    hist_review_file_path = HERE / "data" / "interim" / "hist_review_data_with_topics.pkl"
    asin_file_path = HERE / "data" / "interim" / "asin.pkl"

    # Load the dataframes
    hist_review_df = pd.read_pickle(hist_review_file_path)
    asin_df = pd.read_pickle(asin_file_path)


    # Merge the dataframes on 'asin' and keep only the common entries
    merged_df = hist_review_df.merge(asin_df, right_on='asin', 
                                     left_on ="asin",
                         how='right')


    return merged_df



HERE = Path(os.getcwd()).parent.parent

# Call the function
df = merge_dataframes(HERE)



yoga_mat = df.query("asin == 'B00XQBHJOU'")



release_date = yoga_mat.loc[0]['Date First Available']


timestamps = yoga_mat.date.to_list()
text = yoga_mat.text.to_list()



# Initialize BERTopic
vectorizer_model = CountVectorizer(stop_words="english")
topic_model = BERTopic(verbose=True, vectorizer_model=vectorizer_model)
topics, probs = topic_model.fit_transform(text)
reduced_topics = topic_model.reduce_outliers(text, topics)


# # Print the topics
t = topic_model.get_topic_info()



topics_over_time = topic_model.topics_over_time(text, timestamps, nr_bins=20)
fig = topic_model.visualize_topics_over_time(topics_over_time, top_n_topics=20)





# Add the vertical line
fig.add_shape(
    type="line",
    x0=release_date,
    x1=release_date,
    y0=0,
    y1=1,
    xref='x',
    yref='paper',
    line=dict(color="Red", width=2)
)

# Update the layout for better visualization
fig.update_layout(
    title="Plot with Vertical Line",
    xaxis_title="Date",
    yaxis_title="Value",
)





html_file_path = HERE/"reports"/"figures"/"yoga_mat.html"

pio.write_html(fig, file=html_file_path, auto_open=True)

