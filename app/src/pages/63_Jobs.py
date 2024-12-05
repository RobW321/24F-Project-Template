import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()



if st.button('All Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_View_Jobs.py')

if st.button('Edit Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Edit_Jobs.py')

if st.button('Delete Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Delete_Jobs.py')