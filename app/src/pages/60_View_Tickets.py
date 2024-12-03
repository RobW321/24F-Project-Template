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

# Query Parameters
params = {}
if status_filter != "All":
    params["status"] = status_filter
if priority_filter != "All":
    params["priority"] = priority_filter.split()[0]  # Extract priority number

# Fetch tickets from API or use fallback data
tickets = []
try:
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  # Raise error for non-2xx responses
    tickets = response.json()
except requests.exceptions.RequestException as e:
    st.write("**Important**: Could not connect to the API. Using dummy data.")
    logger.error(f"Error fetching tickets: {e}")
    tickets = [
        {"TicketID": 1, "Description": "Sample ticket 1", "Status": "Open", "Priority": 1, "TicketType": "System Error", "EmployeeID": 101, "StudentNUID": 1001},
        {"TicketID": 2, "Description": "Sample ticket 2", "Status": "In Progress", "Priority": 2, "TicketType": "Career Services", "EmployeeID": 102, "StudentNUID": 1002},
    ]

# Display tickets in a table
if tickets:
    st.write("## Tickets")
    st.dataframe(tickets)
else:
    st.info("No tickets found for the selected filters.")
