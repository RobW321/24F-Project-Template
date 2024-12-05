import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd

SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/a/applications"

# Streamlit Page Setup
st.title("View Applications by Status")

# Instruction
st.write("Select a status to view the corresponding applications.")

# Dropdown for selecting status
status = st.selectbox("Status:", ["In Progress", "Accepted", "Rejected"])

# Button to fetch applications
if st.button("Get Applications"):
    try:
        # Send GET request to the backend API
        response = requests.get(f"{API_URL}/status/{status}")
        response.raise_for_status()

        # Process the data
        applications = response.json()
        if applications:
            # Convert the JSON data to a Pandas DataFrame
            df = pd.DataFrame(applications, columns=[
                "ApplicationID", "DateSubmitted", "Status", "Priority", "Notes", "JobDescription", "CompanyName"
            ])
            
            # Display the DataFrame as a Streamlit Data Table
            st.write(f"Applications with Status: {status}")
            st.dataframe(df)
        else:
            st.warning(f"No applications found with Status: {status}.")

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to fetch applications. Please try again.")
        st.error(e)
