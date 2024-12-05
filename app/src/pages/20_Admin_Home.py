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
        /* Title Styling */
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 10px;
        }

        /* Subtitle Styling */
        .subtitle {
            font-size: 1.2em;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }

        /* Button Container Styling */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        /* Individual Button Styling */
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.1em;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        /* Button Hover Effects */
        .button:hover {
            background-color: #45a049;
            box-shadow: 0px 5px 8px rgba(0, 0, 0, 0.2);
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9em;
            color: #888;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the page title
st.markdown('<div class="title">Welcome to Admin Dashboard!</div>', unsafe_allow_html=True)

# Add the page subtitle
st.markdown('<div class="subtitle">Manage your work with ease using the tools below.</div>', unsafe_allow_html=True)

if st.button('Tickets Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/65_TIckets_Home_page.py')

if st.button('Companies Dashboard', 
            type='primary',
            use_container_width=True):
  st.switch_page('pages/100_Companies_Dashboard.py')

if st.button('View Jobs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/63_Jobs.py')