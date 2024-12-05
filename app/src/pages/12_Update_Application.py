import streamlit as st
import requests
from datetime import date

# Backend API URL
API_URL = "http://api:4000/a/applications"

# Streamlit Page Setup
st.title("Update an Existing Job Application")

# Instruction
st.write("Fill out the form below to update an application.")


if "student_nuid" in st.session_state and st.session_state.student_nuid is not None:
    student_nuid = st.session_state.student_nuid

# Form to get user inputs
with st.form("update_application_form"):
    application_id = st.number_input("Application ID (e.g., 1):", min_value=1, step=1, format="%d")
    date_submitted = st.date_input("Date Submitted:", value=date.today())
    status = st.selectbox("Status:", ["In Progress", "Accepted", "Rejected"])
    priority = st.slider("Priority (1 = High, 3 = Low):", min_value=1, max_value=3)
    notes = st.text_area("Notes (Optional):")

    # Submit button for the form
    submitted = st.form_submit_button("Update Application")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "DateSubmitted": date_submitted.isoformat(),
        "Status": status,
        "Priority": priority,
        "Notes": notes,
    }

    try:
        # Send the payload to the backend API
        response = requests.put(f"{API_URL}/{application_id}/{student_nuid}", json=payload)
        response.raise_for_status()

        # Success message
        st.success("Application updated successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to update application. Please try again.")
        st.error(e)
