import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.markdown(
    """
    <style>
        .title {
            font-size: 2.5em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.2em;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Jobs Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Manage all jobs with the tools below</div>', unsafe_allow_html=True)

# Add button sections with some spacing and styling
st.markdown(
    """
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.1em;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .button:hover {
            background-color: #45a049;
            box-shadow: 0px 5px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)


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