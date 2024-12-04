import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Setup logger
logger = logging.getLogger(__name__)

# Add sidebar links
SideBarLinks()

st.write("# View Tickets")

"""
Retrieve and display ticket data from the REST API. If the backend isn't running,
the app will display a message and fallback to dummy data.

Use the filters in the sidebar to refine your results.
"""

# Define Backend API URL
API_URL = "http://api:4000/tickets"  # Replace with the actual backend URL

# Sidebar Filters
st.sidebar.header("Filter Tickets")
status_filter = st.sidebar.selectbox("Filter by Status", ["All", "Open", "In Progress", "Closed"], index=0)
priority_filter = st.sidebar.selectbox("Filter by Priority", ["All", "1 (High)", "2 (Medium)", "3 (Low)"], index=0)

data = {} 
try:
  data = requests.get('http://api:4000/tickets').json()
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

st.dataframe(data)


