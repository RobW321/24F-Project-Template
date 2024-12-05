import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Editing a Job")

with st.form("edit_job_form"):

    job_description = st.text_input("Job Description")
    sponsorship_required = st.checkbox("Sponsorship Required")
    deadline = st.date_input("Deadline")  # Updated to a date input
    company_id = st.number_input("Company ID", min_value=1, step=1)
    job_id = st.number_input("Job ID to edit", min_value=1, step=1)

    submit_button = st.form_submit_button("Edit Job")

    if submit_button:
        if not job_description:
            st.error("Please enter a valid job description")
        elif not company_id:
            st.error("Please enter a valid company ID")
        elif not job_id:
            st.error("Please enter a valid Job ID")
        elif not deadline:
            st.error("Please enter a valid deadline")
        else:
            # Prepare data for the API
            job_data = {
                "job_description": job_description,
                "sponsorship_required": sponsorship_required,  # Match Flask API key
                "deadline": str(deadline),  # Convert to string for API compatibility
                "company_id": company_id,  # Match Flask API key
                "job_id": job_id  # Match Flask API key
            }

            logger.info(f"Job form submitted with data: {job_data}")

            # Make a PUT request to the API endpoint
            try:
                response = requests.put('http://api:4000/j/edit', json=job_data)  # Correct endpoint
                if response.status_code == 200:
                    st.success("Job edited successfully!")
                else:
                    st.error(f"Error editing job: {response.text}")  # Updated error message
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
