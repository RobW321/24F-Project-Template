import requests
import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()

st.title(f"Your Interviews:")

# Fetch the student_nuid from session state
if "student_nuid" in st.session_state and st.session_state.student_nuid is not None:
    student_nuid = st.session_state.student_nuid

    # Fetch interviews for the student
    try:
        API_URL = "http://api:4000/i/interviews"
        response = requests.get(f"{API_URL}/{student_nuid}")
        response.raise_for_status()
        interviews = response.json()

        if not interviews:
            st.write("No interviews found.")
        else:
            # Convert interviews to a structured format for the table
            data = [
                {
                    "Interview ID": interview.get("InterviewID", "N/A"),
                    "Interview Type": interview.get("InterviewType", "N/A"),
                    "Round": interview.get("Round", "N/A"),
                    "Company": interview.get("CompanyName", "N/A"),
                    "Interviewer": interview.get("InterviewerName", "N/A"),
                    "Interviewer Email": interview.get("InterviewerEmail", "N/A")
                }
                for interview in interviews
            ]

            # Display interviews as a table
            st.table(data)

    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch interviews. Please try again later.")
        st.error(e)

else:
    st.error("No student NUID found in session state. Please navigate from the main page.")