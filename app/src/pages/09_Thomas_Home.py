import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Thomas!')

if st.button('Company Sponsorship History', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/93_Sponsorship_History.py')

if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/54_Job_Applications.py')

if st.button('Visa Stats', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/91_Visa_Stats.py')