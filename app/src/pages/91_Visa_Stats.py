import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Add sidebar links
SideBarLinks()

# Title
st.title("Company Sponsorship Percentages")

"""
Viewing the Sponsorship Percentages for All Companies
"""

# Fetch data from the Flask API
try:
    response = requests.get('http://api:4000/co/sponsorships')
    response.raise_for_status()  # Raise an error if the response status code is not 200
    data = response.json()
except Exception as e:
    st.error("Failed to fetch data from the API.")
    st.error(f"Error details: {e}")
    data = []

# Process and display data
if data:
    for company in data:
        company_name = company["CompanyName"]
        sponsorship_percentage = company["SponsorshipPercentage"]
        visa_type = company["VisaType"]

        # Display the company name, visa type, and progress bar
        st.write(f"### {company_name}")
        st.write(f"Visa Type: {visa_type}")
        
        # Custom progress bar with green color
        st.markdown(
            f"""
            <div style="width: 100%; background-color: #f0f0f0; border-radius: 5px;">
                <div style="width: {sponsorship_percentage}%; background-color: green; padding: 10px 0; border-radius: 5px; text-align: center; color: white;">
                    {sponsorship_percentage}%
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("---")  # Horizontal line for separation
else:
    st.write("No data available.")
