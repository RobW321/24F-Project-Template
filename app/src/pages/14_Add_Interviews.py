import streamlit as st
import requests
from modules.nav import SideBarLinks
from datetime import date

# SideBar Links (if needed)
SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/i/interviews"

# Streamlit Page Setup
st.title("Add a New Interview")

# Instruction
st.write("Fill out the form below to add a new interview.")

# Form to get user inputs
with st.form("add_interview_form"):
    interview_id = st.number_input("Interview ID (e.g. 96 and above):", min_value=1, step=1, format="%d")
    interview_date = st.date_input("Interview Date:", value=date.today())
    location = st.text_input("Location (Optional):")
    interview_type = st.selectbox("Interview Type:", ["Technical", "Behavioral"])
    round = st.selectbox("Round:", ["Round 1", "Round 2", "Final"])
    company_id = st.number_input("Company ID (e.g., 1):", min_value=1, step=1, format="%d")
    interviewer_id = st.number_input("Interviewer ID (e.g., 1):", min_value=1, step=1, format="%d")

    # Submit button for the form
    submitted = st.form_submit_button("Submit Interview")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "InterviewID": interview_id,
        "Dates": interview_date.isoformat(),
        "Locations": location,
        "InterviewType": interview_type,
        "Round": round,
        "CompanyID": company_id,
        "InterviewerID": interviewer_id,
    }

    try:
        # Send the payload to the backend API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()

        # Success message
        st.success("Interview added successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to add interview. Please try again.")
        st.error(e)
