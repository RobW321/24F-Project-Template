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

# Ensure the session state for NUID is initialized
if "student_nuid" not in st.session_state:
    st.error("No NUID found in session state. Please navigate from the home page.")
    st.stop()

# Retrieve the NUID from session state
student_nuid = st.session_state.student_nuid

# Form to get user inputs
with st.form("add_application_form"):
    # Display NUID as a static field since it's taken from the session state
    st.text(f"Student NUID: {student_nuid}")
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
        "StudentNUID": student_nuid,  # Use NUID from session state
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
