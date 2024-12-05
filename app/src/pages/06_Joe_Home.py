import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, Joe.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Initialize Streamlit session state for student_nuid if not already set
if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None


# Button to navigate to "Job Applications"
if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1001  # Set the NUID to 1003
    st.switch_page('pages/54_Job_Applications.py')

