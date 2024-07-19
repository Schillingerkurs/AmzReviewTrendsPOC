# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:15:09 2024

@author: fs.egb
"""


import pandas as pd
import os
from dotenv import load_dotenv
import missingno as msno
import matplotlib.pyplot as plt
from pathlib import Path
import requests
import gzip
import json
import pandas as pd
from io import BytesIO
import re

from get_product_info_from_asin import add_product_info


# Define HERE as parent directory of current working directory
HERE = Path(os.getcwd()).parent.parent

# Load environment variables from .env file
load_dotenv()



def load_jsonl_gz_from_url(url):
    """
    Downloads a .jsonl.gz file from the specified URL and loads it into a pandas DataFrame.

    Parameters:
    url (str): The URL of the .jsonl.gz file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the .jsonl.gz file.
    """
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()
    
    # Use BytesIO to handle the response content in memory
    with BytesIO(response.content) as bytes_io:
        # Open the .gz file
        with gzip.GzipFile(fileobj=bytes_io) as gz_file:
            # Read the lines from the .jsonl file
            lines = gz_file.readlines()
    
    # Parse each line as a JSON object and create a list of dictionaries
    data = [json.loads(line) for line in lines]
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    return df



def clean_text_formatting(df, column):
    # Define the patterns to remove
    patterns = ['br', 'itbr', 'itbr br', 'productbr', 'consbr', 'br br', 'prosbr', 'br overall', 'review', 'br consbr']
    
    # Compile a regex pattern for these specific strings
    combined_pattern = re.compile('|'.join([re.escape(p) for p in patterns]), re.IGNORECASE)
    
    # Define a function to apply the regex substitution
    def remove_patterns(text):
        return combined_pattern.sub('', text)
    
    # Apply the function to the specified column
    df[column] = df[column].apply(remove_patterns)
    
    return df





df = (load_jsonl_gz_from_url(os.environ.get("REV_HIST_DATA_PATH"))
      # Looks like the timestamps are in Unix (in miliseconds)
      .assign(date = lambda x:  pd.to_datetime(x['timestamp'], unit='ms'))
      # Assume Pacific Standard Time  as the records are from UCSD  ( GMT-7)
      .assign(date = lambda x:  x['date'].dt.tz_localize('-07:00'))    
      )



# df = clean_text_formatting(df, 'text')



# file_path = HERE/"data"/"raw"/"hist_review_data.pkl"


# df.to_pickle(file_path)






