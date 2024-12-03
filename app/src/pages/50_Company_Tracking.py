import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Thomas!')

if st.button('View Company Sponsorship History', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/93_Sponsorship_History.py')

if st.button('Sort Companies By Sponsorship Count', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/94_Sponsorship_Count.py')
