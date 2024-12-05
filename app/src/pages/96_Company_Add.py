import streamlit as st
import requests
from datetime import date
from modules.nav import SideBarLinks

SideBarLinks()

# Backend API URL
API_URL = "http://api:4000/co/add"

# Streamlit Page Setup
st.title("Add a New Company")

# Instruction
st.write("Fill out the form below to add a new company.")

# Form to get user inputs
with st.form("add_company"):
    company_id = st.number_input("CompanyID (e.g., 1):", min_value=1, step=1, format="%d")
    company_name = st.text_area("Company Name:",)
    industry = st.text_area("Industry:",)
    location = st.text_area("Location:")
    sponsor_id = st.number_input("SponsorID (e.g., 1):", min_value=1, step=1, format="%d")


    # Submit button for the form
    submitted = st.form_submit_button("Submit Company")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "CompanyID": company_id,
        "CompanyName": company_name,
        "Industry": industry,
        "Location": location,
        "SponsorID": sponsor_id,
    }

    try:
        # Send the payload to the backend API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()

        # Success message
        st.success("Company added successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to add company. Please try again.")
        st.error(e)
