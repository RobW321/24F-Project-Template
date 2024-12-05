import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()

# Set the API endpoint
API_URL = "http://api:4000/t/add"  # Update with the actual API URL

# Streamlit form for ticket input
st.title("Add a New Ticket")

with st.form("ticket_form"):
    description = st.text_input("Description")
    status = st.selectbox("Status", ["Open", "Closed", "In Progress"])
    priority = st.selectbox("Priority", [1, 2, 3])  # Assuming 1 is high, 3 is low
    ticket_type = st.text_input("Ticket Type")
    employee_id = st.number_input("Employee ID", min_value=1, step=1)
    student_nuid = st.number_input("Student NUID", min_value=1, step=1)

    # Submit button
    submitted = st.form_submit_button("Add Ticket")

if submitted:
    # Prepare data for the API
    ticket_data = {
        "Description": description,
        "Status": status,
        "Priority": priority,
        "TicketType": ticket_type,
        "EmployeeID": employee_id,
        "StudentNUID": student_nuid,
    }

    # Send data to the Flask API
    try:
        response = requests.put(API_URL, json=ticket_data)
        if response.status_code == 201:
            st.success("Ticket added successfully!")
        else:
            st.error(f"Failed to add ticket. Error: {response.json().get('error')}")
    except Exception as e:
        st.error(f"An error occurred: {e}")