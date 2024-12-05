import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd
from datetime import date

# SideBar Links (if needed)
SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/i/filterDate"

# Streamlit Page Setup
st.title("View Interviews by Date")

# Instruction
st.write("Select a date to view the corresponding interviews.")

# Date picker for selecting interview date
interview_date = st.date_input("Interview Date:", value=date.today())

# Button to fetch interviews
if st.button("Get Interviews"):
    try:
        # Send GET request to the backend API with the selected date
        response = requests.get(f"{API_URL}/interview_date/{interview_date}")
        response.raise_for_status()

        # Process the data
        interviews = response.json()
        if interviews:
            # Convert the JSON data to a Pandas DataFrame
            df = pd.DataFrame(interviews, columns=[
                "InterviewID", "InterviewDate", "Location", "InterviewType", "Round", 
                "CompanyName", "InterviewerName", "InterviewerEmail"
            ])
            
            # Display the DataFrame as a Streamlit Data Table
            st.write(f"Interviews on {interview_date}")
            st.dataframe(df)
        else:
            st.warning(f"No interviews found for {interview_date}.")

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to fetch interviews. Please try again.")
        st.error(e)
