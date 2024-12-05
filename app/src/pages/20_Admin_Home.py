import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Dashboard')

if st.button('View Tickets', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/60_View_Tickets.py')


if st.button('Edit Tickets', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/62_Edit_Ticket.py')