import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Kyrie!')

if st.button(
    'View Interviews',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    st.session_state.student_nuid = 1004
    # Navigate to the page displaying applications
    st.switch_page('pages/14_Get_Interviews.py')

if st.button('Add Interviews', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/14_Add_Interviews.py')

if st.button('Edit Interviews', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/14_Update_Interviews.py')

if st.button('Delete Interviews', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/14_Delete_Interviews.py')

if st.button('Filter Interviews By Round', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/14_Filter_By_Round_Interviews.py')

if st.button('Filter Interviews By Date', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004
  st.switch_page('pages/14_Filter_By_Date_Interviews.py')

if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None
    