import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Add an application')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

import logging
logger = logging.getLogger(__name__)




# Title
st.title('Add and Track Your Job Applications')

# Backend API URL
API_URL = "http://localhost:8501/applications"  # Replace with your backend URL

# Two-column layout for the form
col1, col2 = st.columns(2)

# Input form for adding a new application
with st.form("application_form"):
    with col1:
        student_id = st.number_input("Student ID", min_value=1, step=1, help="Your unique student ID")
        job_id = st.number_input("Job ID", min_value=1, step=1, help="The ID of the job you're applying for")
        priority = st.selectbox("Priority Level", [1, 2, 3], help="1 = High, 3 = Low")
    with col2:
        date_submitted = st.date_input("Date Submitted")
        status = st.selectbox("Application Status", ["Submitted", "In Progress", "Accepted", "Rejected"], index=0)
        notes = st.text_area("Notes", help="Add any additional notes about the application")

    # Submit button for the form
    submitted = st.form_submit_button("Add Application")

# Handle form submission
if submitted:
    # Data payload for the POST request
    data = {
        "student_id": student_id,
        "job_id": job_id,
        "date_submitted": date_submitted.strftime("%Y-%m-%d"),
        "status": status,
        "priority": priority,
        "notes": notes
    }

    try:
        # Make POST request to the backend
        response = requests.post(API_URL, json=data)
        response.raise_for_status()  # Raise error for bad status codes
        st.success("Application added successfully!")
        logger.info(f"Added application: {data}")

    except requests.exceptions.RequestException as e:
        st.error("Failed to add application. Please try again later.")
        logger.error(f"Error adding application: {e}")

# Display all applications
st.write("### Current Applications")
try:
    # Fetch the updated list of applications
    response = requests.get(API_URL)
    response.raise_for_status()
    applications = response.json()

    # Display applications in a table
    for app in applications:
        st.write(f"- **Job ID**: {app['job_id']} | **Status**: {app['status']} | **Priority**: {app['priority']} | **Notes**: {app['notes']}")

except requests.exceptions.RequestException as e:
    st.error("Failed to load applications. Please try again later.")
    logger.error(f"Error fetching applications: {e}")

