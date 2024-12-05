import requests
import streamlit as st
from datetime import date

# Backend API URL
API_URL = "http://api:4000/a/applications"

# Streamlit Page Setup
st.title("Add New Job Application")

# Instruction
st.write("Fill out the form below to add a new job application to the database.")

# User Input Form
with st.form("add_application_form"):
    # Prompt user for application details
    student_nuid = st.number_input("Student NUID (e.g., 1001):", min_value=1, step=1, format="%d")
    job_id = st.number_input("Job ID (e.g., 1):", min_value=1, step=1, format="%d")
    date_submitted = st.date_input("Date Submitted:", value=date.today())
    status = st.selectbox("Application Status:", ["In Progress", "Accepted", "Rejected"])
    priority = st.slider("Priority (1 = High, 3 = Low):", min_value=1, max_value=3)
    notes = st.text_area("Notes (Optional):")

    # Submit Button
    submitted = st.form_submit_button("Add Application")

if submitted:
    # Construct the payload to send to the backend
    payload = {
        "StudentNUID": int(student_nuid),
        "JobID": int(job_id),
        "DateSubmitted": date_submitted.isoformat(),
        "Status": status,
        "Priority": int(priority),
        "Notes": notes,
    }

    try:
        # Make POST request to backend API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Success Message
        st.success("Application added successfully!")
        st.write("Here is the application you added:")
        st.json(payload)
    except requests.exceptions.RequestException as e:
        # Error Handling
        st.error("Failed to add application. Please try again.")
        st.error(f"Error: {e}")
