import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Set up logger
logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Fetch and display tickets
st.header("Tickets")
try:
    # Make GET request to fetch tickets
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  # Raise error for bad status codes
    tickets = response.json()
    logger.info(f"Fetched tickets: {tickets}")

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
    st.error(f"Failed to fetch tickets: {e}")
    logger.error(f"Error fetching tickets: {e}")
