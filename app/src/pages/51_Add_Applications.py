import requests
import streamlit as st

# Backend API URL
API_URL = "http://localhost:5000/applications"

st.title("Add a Job Application")

# Form to collect application details
with st.form("application_form"):
    student_id = st.number_input("Student ID", min_value=1, step=1)
    job_id = st.number_input("Job ID", min_value=1, step=1)
    date_submitted = st.date_input("Date Submitted")
    status = st.selectbox("Application Status", ["Submitted", "In Progress", "Accepted", "Rejected"])
    priority = st.selectbox("Priority Level", [1, 2, 3], help="1 = High, 3 = Low")
    notes = st.text_area("Notes (Optional)")

    # Submit button
    submitted = st.form_submit_button("Add Application")

if submitted:
    # Payload for POST request
    payload = {
        "student_id": student_id,
        "job_id": job_id,
        "date_submitted": date_submitted.strftime("%Y-%m-%d"),
        "status": status,
        "priority": priority,
        "notes": notes,
    }

    try:
        # Send POST request to backend
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        st.success("Application added successfully!")
        st.json(response.json())  # Display response data

    except requests.exceptions.RequestException as e:
        st.error("Failed to add application. Please try again.")
        st.error(e)
