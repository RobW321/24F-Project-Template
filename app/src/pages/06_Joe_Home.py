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


if st.button('Add An Application', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Add_Applications.py')

if st.button(
    'View Applications',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1001
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Get_Applications.py')
    
if st.button(
    'Edit Applications',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1001
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Update_Application.py')
    
if st.button(
    'Delete Applications',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1001
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Delete_Application.py')
    
if st.button(
    'Filter Applications by Priority',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1001
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Filter_Application.py')
    
    
if st.button(
    'Filter Applications by Status',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1001
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Filter_By_Status_Application.py')
