import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title("Editing a Ticket")

with st.form("edit_ticket_form"):
    
    # Create the various input widgets needed for 
    # each piece of information you're eliciting from the user
    status = st.text_input("Ticket Status")
    priority = st.number_input("Priority")
    employeeID = st.number_input("EmployeeID")
    ticketID = st.number_input("TicketID to edit")
    
   
# Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Edit Ticket")
    
    # Validate all fields are filled when form is submitted
    if submit_button:
        if not status:
            st.error("Please enter a status description")
        elif  priority > 3:
            st.error("Please enter a valid priority (1-3) ")
        elif employeeID > 50:
            st.error("Please enter a valid employee id")
        elif ticketID > 50:
            st.error("Please enter a valid ticket ID")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            ticket_data = {
                "Status": status,
                "Priority": priority,
                "EmployeeID": employeeID,
                "TicketID": ticketID
            }
            
            # printing out the data - will show up in the Docker Desktop logs tab
            # for the web-app container 
            logger.info(f"Ticket form submitted with data: {ticket_data}")
            
            # Now, we try to make a POST request to the proper end point
            try:
                # using the requests library to POST to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.put('http://api:4000/t/edit', json=ticket_data)
                if response.status_code == 200:
                    st.success("Ticket edited successfully!")
                else:
                    st.error(f"Error adding product: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
