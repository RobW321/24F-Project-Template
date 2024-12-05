import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Dashboard')

if st.button('Tickets Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/65_TIckets_Home_page.py')

if st.button('Companies Dashboard', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/100_Companies_Dashboard.py')

if st.button('View Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Jobs.py')