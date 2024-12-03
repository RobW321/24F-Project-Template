import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Set up logger
logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.title("View Tickets")

# Backend API URL
API_URL = "http://localhost:8501/tickets"  # Replace with your backend URL

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

# Fetch and display tickets
st.header("Tickets")
try:
    # Make GET request to fetch tickets
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  # Raise error for bad status codes
    tickets = response.json()

    if tickets:
        for ticket in tickets:
            with st.expander(f"Ticket ID: {ticket['TicketID']}"):
                st.write(f"**Description**: {ticket['Description']}")
                st.write(f"**Status**: {ticket['Status']}")
                st.write(f"**Priority**: {ticket['Priority']}")
                st.write(f"**Type**: {ticket['TicketType']}")
                st.write(f"**Assigned Employee ID**: {ticket['EmployeeID']}")
                st.write(f"**Student NUID**: {ticket['StudentNUID']}")
    else:
        st.info("No tickets match the selected filters.")
except requests.exceptions.RequestException as e:
    st.error("Failed to fetch tickets. Please try again later.")
    logger.error(f"Error fetching tickets: {e}")
