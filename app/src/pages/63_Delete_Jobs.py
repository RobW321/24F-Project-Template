import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.header('Delete Specific Job')

with st.form("delete_job_form"):
    
   
    JobID = st.number_input("JobID to Delete")
    
   
# Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Delete Job")

    if submit_button:
        if JobID > 50:
            st.error("Please enter a valid Job ID")
        else:
            # We only get into this else clause if all the input fields have something 
            # in them. 
            #
            # Package the data up that the user entered into 
            # a dictionary (which is just like JSON in this case)
            job_data = {
                "JobID": JobID
            }

            try:
                # using the requests library to put to /p/product.  Passing
                # product_data to the endpoint through the json parameter.
                # This particular end point is located in the products_routes.py
                # file found in api/backend/products folder. 
                response = requests.delete('http://api:4000/j/deletebyid', json=job_data)
                if response.status_code == 200:
                    st.success("Job deleted successfully!")
                else:
                    st.error(f"Error deleting job: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to server: {str(e)}")