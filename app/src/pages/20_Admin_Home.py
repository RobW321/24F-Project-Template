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


if st.button('View Companies', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/97_Company_View.py')

if st.button('Add Companies', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/96_Company_Add.py')

if st.button('Delete Companies', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/95_Company_Delete.py')

if st.button('Update Companies', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/98_Company_Update.py')

if st.button('View Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Jobs.py')