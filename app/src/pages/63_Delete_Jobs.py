import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Job Administration Page')
st.header('Delete Specific Job')

# Form to delete a specific job
with st.form("delete_job_form"):
    job_id = st.number_input("Job ID to delete", min_value=1, step=1)

    # Submit button
    submit_button = st.form_submit_button("Delete Job")

    if submit_button:
        # Validate the job ID
        if job_id <= 0:
            st.error("Please enter a valid Job ID")
        else:
            # Prepare data for the API
            job_data = {"job_id": job_id}

            try:
                response = requests.delete('http://api:4000/j/deletebyid', json=job_data)
                if response.status_code == 200:
                    st.success("Job deleted successfully!")
                else:
                    st.error(f"Error deleting job: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")