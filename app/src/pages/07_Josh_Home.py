import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Josh!')

if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/54_Job_Applications.py')
