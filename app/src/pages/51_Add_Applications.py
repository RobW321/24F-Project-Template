import requests
import streamlit as st

# Backend API URL
API_URL = "http://api:4000/a/applications"

st.title("Add New Job Application")

# Input fields for application details
with st.form("Add Application Form"):
    student_nuid = value=1001  # Default NUID for Joe Wellington
    job_id = st.number_input("Job ID", min_value=1, step=1)
    date_submitted = st.date_input("Date Submitted")
    status = st.selectbox("Application Status", ["In Progress", "Accepted", "Rejected"])
    priority = st.number_input("Priority (1-3)", min_value=1, max_value=3, step=1)
    notes = st.text_area("Notes (Optional)")

    # Submit button
    submitted = st.form_submit_button("Submit Application")

# Handle form submission
if submitted:
    try:
        # Prepare data for POST request
        application_data = {
            "StudentNUID": student_nuid,
            "JobID": job_id,
            "DateSubmitted": date_submitted.strftime('%Y-%m-%d'),
            "Status": status,
            "Priority": priority,
            "Notes": notes,
        }

        # Send POST request to backend
        response = requests.post(API_URL, json=application_data)
        response.raise_for_status()

        st.success("Application added successfully!")

    except requests.exceptions.RequestException as e:
        st.error("Failed to add application. Please try again.")
        st.error(e)
