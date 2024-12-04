import requests
import streamlit as st

API_URL = "http://api:4000/a/applications"

student_nuid = 1001

st.title(f"Applications for User {student_nuid}")

# Fetch applications for the student
try:
    response = requests.get(f"{API_URL}/{student_nuid}")
    response.raise_for_status()
    applications = response.json()

    if not applications:
        st.write("No applications found.")
    else:
        # Convert applications to a structured format for the table
        data = [
            {
                "Application ID": app["ApplicationID"],
                "Date Submitted": app["DateSubmitted"],
                "Status": app["Status"],
                "Priority": app["Priority"],
                "Job": app["JobDescription"],
                "Company": app["CompanyName"],
                "Notes": app["Notes"],
            }
            for app in applications
        ]

        # Display applications as a table
        st.write("### Applications List")
        st.table(data)

except requests.exceptions.RequestException as e:
    st.error("Failed to fetch applications. Please try again later.")
    st.error(e)