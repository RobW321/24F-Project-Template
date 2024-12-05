import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('App Administration Page')

if st.button('Delete all Closed Tickets', 
             type = 'primary',
             use_container_width=True):
            try:
                # using the requests library to put to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.delete('http://api:4000/t/delete')
                if response.status_code == 200:
                    st.success("Tickets deleted successfully!")
                else:
                    st.error(f"Error adding product: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
                
st.header('Delete Specific Ticket')

with st.form("delete_ticket_form"):
    
   
    ticketID = st.number_input("TicketID to delete")
    
   
# Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Delete Ticket")

    if submit_button:
        if ticketID > 50:
            st.error("Please enter a valid ticket ID")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            ticket_data = {
                "TicketID": ticketID
            }

            try:
                # using the requests library to put to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.delete('http://api:4000/t/deletebyid', json=ticket_data)
                if response.status_code == 200:
                    st.success("Ticket deleted successfully!")
                else:
                    st.error(f"Error deleting ticket: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")
  