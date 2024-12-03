import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Thomas!')

if st.button('Company Tracking', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/08_Progress.py')

if st.button('Jop Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/08_Progress.py')

if st.button('Visa Stats', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/08_Progress.py')