import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout='wide')

SideBarLinks()

st.title('Welcome Thomas!')

# Initialize session state for NUID if not already set
if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None

# Button to navigate to "Company Sponsorship History"
if st.button('Company Sponsorship History', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1003  # Set the NUID to 1003
    st.switch_page('pages/93_Sponsorship_History.py')

# Button to navigate to "Job Applications"
if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1003  # Set the NUID to 1003
    st.switch_page('pages/54_Job_Applications.py')

# Button to navigate to "Visa Stats"
if st.button('Visa Stats', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1003  # Set the NUID to 1003
    st.switch_page('pages/91_Visa_Stats.py')
