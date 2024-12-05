import streamlit as st
import requests
from datetime import date

# Backend API URL
API_URL = "http://api:4000/co/edit"

# Streamlit Page Setup
st.title("Update an Existing Company Application")

# Instruction
st.write("Fill out the form below to update an company.")

# Form to get user inputs
with st.form("update_company_form"):
    company_id = st.number_input("Company ID (e.g., 1):", min_value=1, step=1, format="%d")
    company_name = st.text_area("Company Name:")
    industry = st.text_area("Industry:")
    location = st.text_area("Location:")

    # Submit button for the form
    submitted = st.form_submit_button("Update Company")

# If the form is submitted
if submitted:
    # Prepare the payload
    payload = {
        "CompanyID": company_id,
        "CompanyName": company_name,
        "Industry": industry,
        "Location": location,
    }

    try:
        # Send the payload to the backend API
        response = requests.put(f"{API_URL}", json=payload)
        response.raise_for_status()

        # Success message
        st.success("Company updated successfully!")
        st.json(payload)

    except requests.exceptions.RequestException as e:
        # Error message
        st.error("Failed to update company. Please try again.")
        st.error(e)
