import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title("Viewing Sponsorship History")

"""
Viewing the Sponsorship History for All Companies with Applications
"""
data = {} 
try:
  data = requests.get('http://api:4000/co/companies').json()

  st.table(data)
except:
  st.write("**Important**: Could not connect to sample api, so using dummy data.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}



