import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Welcome Thomas!')

if st.button('Circular Progress', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/08_Progress.py')