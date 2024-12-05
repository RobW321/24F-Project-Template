import streamlit as st
import requests
from modules.nav import SideBarLinks


SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/a/applications"

# Streamlit Page Setup
st.title("Delete a Job Application")

# Instruction
st.write("Provide the Application ID to delete a job application.")

# Form to get user input
with st.form("delete_application_form"):
    application_id = st.number_input("Application ID (e.g., 1):", min_value=1, step=1, format="%d")
    submitted = st.form_submit_button("Delete Application")

# If the form is submitted
if submitted:
    try:
        # Send the DELETE request to the backend API
        response = requests.delete(f"{API_URL}/{application_id}")
        response.raise_for_status()

        # Success message
        st.success("Application deleted successfully!")
        st.write(f"Deleted Application ID: {application_id}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            st.error("Application not found.")
        else:
            st.error("Failed to delete application. Please try again.")
            st.error(http_err)
    except requests.exceptions.RequestException as e:
        st.error("Failed to delete application. Please try again.")
        st.error(e)
