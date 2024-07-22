# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:01:32 2024

@author: fs.egb
"""
import streamlit as st
from pathlib import Path
import pandas as pd
import glob
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define paths
HERE = Path(os.getcwd()).parent.parent

# Define paths to HTML files
html_file_path_product_owner = HERE / "reports" / "figures" / "product_cykles"
indirekt_file_path = HERE / "data" / "interim" / "indirekt_marketing.pkl"

# Create a sidebar for stakeholder selection
st.sidebar.title("Amazon Customer Reviews POC")
st.sidebar.subheader("Generating insights from health and personal care reviews")
stakeholder = st.sidebar.selectbox("Select which stakeholder", ["Product Owner", "Marketing Strategy"])

# Display the appropriate content based on the selected stakeholder
if stakeholder == "Product Owner":
    st.title("Dashboard for Product Owner")
    
    # Get list of HTML files in the directory
    html_files = glob.glob(str(html_file_path_product_owner / "*.html"))
    
    # Extract file names from full paths without the ".html" extension
    file_names = [Path(f).stem for f in html_files]
    
    # Selectbox for choosing an HTML file (displaying names without ".html")
    selected_file = st.selectbox("Select a File", file_names)
    
    # Map selected file name back to full file path (add ".html" extension back)
    if selected_file:
        full_file_path = html_file_path_product_owner / f"{selected_file}.html"
        with open(full_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=2000, scrolling=True, width  = 2000)

elif stakeholder == "Marketing Strategy":
    # Load the DataFrame
    df = pd.read_pickle(indirekt_file_path)
    
    st.title("Dashboard for Indirect Marketing Strategies")
    st.sidebar.subheader("How partners and family members review products")
    
    # Check if DataFrame is loaded correctly
    if df.empty:
        st.write("No data available.")
    else:
        # Create a select box for the "asin" column values
        topic_values = df['topics_reduced'].unique()
        selected_asin = st.selectbox("Select Family Relation", topic_values)
        
        # Filter and display the DataFrame based on the selected ASIN
        filtered_df = df[df['topics_reduced'] == selected_asin][['text','title']]
        st.write(filtered_df)
    


   



