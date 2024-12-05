import streamlit as st
import requests
from datetime import date

# Backend API URL
API_URL = "http://api:4000/i/interviews"


# Streamlit Page Setup
st.title("Update an Existing Interview")

# Instruction
st.write("Fill out the form below to update an interview.")

# Form to get user inputs
with st.form("update_interview_form"):
    interview_id = st.number_input("Interview ID (e.g., 1):", min_value=1, step=1, format="%d")
    interview_type = st.selectbox("Interview Type:", ["Technical", "Behavioral"])
    round = st.selectbox("Round:", ["Round 1", "Round 2", "Final"])
    interview_date = st.date_input("Interview Date:", value=date.today())
    location = st.text_input("Location (Optional):")

    # Submit button for the form
    submitted = st.form_submit_button("Update Interview")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "InterviewType": interview_type,
        "Round": round,
        "Dates": interview_date.isoformat(),
        "Locations": location,
    }

    try:
        # Send the payload to the backend API
        response = requests.put(f"{API_URL}/{interview_id}", json=payload)
        response.raise_for_status()

        # Success message
        st.success("Interview updated successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to update interview. Please try again.")
        st.error(e)