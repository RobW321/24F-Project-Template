import requests
import streamlit as st



st.title("Your Job Applications")

API_URL = "http://web-api:4000/a/application"
student_nuid = 1001


# Fetch applications for the student
try:
    
    response = requests.get(f"{API_URL}/{student_nuid}")
    applications = response.json()

    if not applications:
        st.write("No applications found.")
    else:
        # Display applications in a table
        st.write("### Applications List")
        for app in applications:
            st.markdown(f"""
            **Application ID**: {app['ApplicationID']}  
            **Date Submitted**: {app['DateSubmitted']}  
            **Status**: {app['Status']}  
            **Priority**: {app['Priority']}  
            **Job**: {app['JobDescription']}  
            **Company**: {app['CompanyName']}  
            **Notes**: {app['Notes']}  
            ---  
            """)

except requests.exceptions.RequestException as e:
    st.error("Failed to fetch applications. Please try again later.")
    st.error(e)
