import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Kyrie Irving Home Page')

st.title(f"Welcome, Kyrie.")
st.write('')
st.write('')
st.write('### What would you like to do today?')