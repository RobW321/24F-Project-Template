import streamlit as st
import requests
from modules.nav import SideBarLinks
from datetime import date

SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/a/applications"

# Streamlit Page Setup
st.title("Add a New Job Application")

# Instruction
st.write("Fill out the form below to add a new application.")

# Form to get user inputs
with st.form("add_application_form"):
    student_nuid = st.number_input("Student NUID (e.g., 1001):", min_value=1, step=1, format="%d")
    job_id = st.number_input("Job ID (e.g., 1):", min_value=1, step=1, format="%d")
    date_submitted = st.date_input("Date Submitted:", value=date.today())
    status = st.selectbox("Status:", ["In Progress", "Accepted", "Rejected"])
    priority = st.slider("Priority (1 = High, 3 = Low):", min_value=1, max_value=3)
    notes = st.text_area("Notes (Optional):")

    # Submit button for the form
    submitted = st.form_submit_button("Submit Application")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "StudentNUID": student_nuid,
        "JobID": job_id,
        "DateSubmitted": date_submitted.isoformat(),
        "Status": status,
        "Priority": priority,
        "Notes": notes,
    }

    try:
        # Send the payload to the backend API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()

        # Success message
        st.success("Application added successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to add application. Please try again.")
        st.error(e)
