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
st.markdown('<div class="title">Welcome to the Application Dashboard!</div>', unsafe_allow_html=True)

# Add the page subtitle
st.markdown('<div class="subtitle">Manage your applications with ease using the tools below.</div>', unsafe_allow_html=True)

if st.button(
    'View Applications',
    type='primary',
    use_container_width=True
):
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Get_Applications.py')

if st.button('Add Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Add_Applications.py')

if st.button('Edit Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Update_Application.py')

if st.button('Delete Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Delete_Application.py')


if "student_nuid" not in st.session_state:
    st.session_state.student_nuid = None
    

if st.button(
    'Filter Applications by Priority',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Filter_Application.py')

if st.button(
    'Filter Applications by Status',
    type='primary',
    use_container_width=True
):
    # Set the student_nuid value in session state
    # Navigate to the page displaying applications
    st.switch_page('pages/12_Filter_By_Status_Application.py')

    

