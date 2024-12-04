import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Thomas!')

if st.button('Add Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/51_Add_Applications.py')

if st.button('Delete Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/52_Delete_Applications.py')

if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None
    
if st.button(
    'View Applications',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1003
    # Navigate to the page displaying applications
    st.switch_page('pages/12_API_Test.py')

if st.button('Visa Stats', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/91_Visa_Stats.py')