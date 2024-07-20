# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:01:32 2024

@author: fs.egb
"""

import streamlit as st
from pathlib import Path
import os



HERE = Path(os.getcwd()).parent.parent

# Define paths to HTML files
html_file_path_product_owner = HERE/Path("reports/figures/yoga_mat.html")


# Create a sidebar for stakeholder selection
st.sidebar.title("Select Role")
stakeholder = st.sidebar.selectbox("Select which stakeholder ", ["Product Owner", "Management"])

# Display the appropriate HTML file based on the selected stakeholder
if stakeholder == "Product Owner":
    st.title("Dashboard for Product Owner")
    with open(html_file_path_product_owner, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1200, scrolling=True)

elif stakeholder == "Management":
    st.title("Dashboard for Management")
    st.write("Hi Katrin")



