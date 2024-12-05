import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

# Set the page layout
st.set_page_config(layout='wide')

# Add sidebar links
SideBarLinks()

# Add a title with styling
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

st.markdown('<div class="title">Company Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Manage all companies with the tools below</div>', unsafe_allow_html=True)

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

st.markdown('<div class="button-container">', unsafe_allow_html=True)

if st.button('View Companies', type='primary', use_container_width=True):
    st.switch_page('pages/97_Company_View.py')

if st.button('Add Companies', type='primary', use_container_width=True):
    st.switch_page('pages/96_Company_Add.py')

if st.button('Delete Companies', type='primary', use_container_width=True):
    st.switch_page('pages/95_Company_Delete.py')

if st.button('Update Companies', type='primary', use_container_width=True):
    st.switch_page('pages/98_Company_Update.py')

st.markdown('</div>', unsafe_allow_html=True)

# Add footer for a professional touch
st.markdown(
    """
    <style>
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9em;
            color: #888;
        }
    </style>
    <div class="footer">
         Company Management System
    </div>
    """,
    unsafe_allow_html=True
)
