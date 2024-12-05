import streamlit as st
import requests
from modules.nav import SideBarLinks
import pandas as pd

# SideBar Links (if needed)
SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/i/filter"

# Streamlit Page Setup
st.title("View Interviews by Round")

# Instruction
st.write("Select a round to view the corresponding interviews.")

# Dropdown for selecting round
round = st.selectbox("Round:", ["1st Round", "2nd Round", "Final Round"])

# Button to fetch interviews
if st.button("Get Interviews"):
    try:
        # Send GET request to the backend API with the selected round
        response = requests.get(f"{API_URL}/round/{round}")
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
            st.write(f"Interviews for Round: {round}")
            st.dataframe(df)
        else:
            st.warning(f"No interviews found for Round: {round}.")

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to fetch interviews. Please try again.")
        st.error(e)
