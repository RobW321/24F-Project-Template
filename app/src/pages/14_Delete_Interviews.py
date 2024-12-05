import streamlit as st
import requests
from modules.nav import SideBarLinks

# SideBar Links (if needed)
SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/i/delete"

# Streamlit Page Setup
st.title("Delete an Interview")

# Instruction
st.write("Provide the Interview ID to delete an interview.")

# Form to get user input
with st.form("delete_interview_form"):
    interview_id = st.number_input("Interview ID (e.g., 1):", min_value=1, step=1, format="%d")
    submitted = st.form_submit_button("Delete Interview")

# If the form is submitted
if submitted:
    try:
        # Send the DELETE request to the backend API
        response = requests.delete(f"{API_URL}/{interview_id}")
        response.raise_for_status()

        # Success message
        st.success("Interview deleted successfully!")
        st.write(f"Deleted Interview ID: {interview_id}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            st.error("Interview not found.")
        else:
            st.error("Failed to delete interview. Please try again.")
            st.error(http_err)
    except requests.exceptions.RequestException as e:
        st.error("Failed to delete interview. Please try again.")
        st.error(e)
