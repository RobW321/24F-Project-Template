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

if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_Kyrie_Job_Applications.py')

if st.button('Interviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Get_Interviews.py')

