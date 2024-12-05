import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome, Kyrie.")
st.write('')
st.write('')
st.write('### What would you like to do today?')


# Button to navigate to "Job Applications"
if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1004 # Set the NUID to 1003
    st.switch_page('pages/54_Job_Applications.py')

if st.button('Interviews', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004 # Set the NUID to 1003
  st.switch_page('pages/17_Kyrie_Interviews.py')

if st.button('View Sankey Diagram', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1004  
    st.switch_page('pages/07_Sankey.py')
