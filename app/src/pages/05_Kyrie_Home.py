import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
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
st.markdown("<div class='title'>Welcome to Kyrie's Dashboard!</div>", unsafe_allow_html=True)

# Add the page subtitle
st.markdown('<div class="subtitle">Manage your applications with ease using the tools below.</div>', unsafe_allow_html=True)
# Button to navigate to "Job Applications"
if st.button('Job Applications', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1004 # Set the NUID to 1004
    st.switch_page('pages/54_Job_Applications.py')

if st.button('Interviews', 
             type='primary',
             use_container_width=True):
  st.session_state.student_nuid = 1004 # Set the NUID to 1003
  st.switch_page('pages/17_Kyrie_Interviews.py')

if st.button('View Sankey Diagram', 
             type='primary',
             use_container_width=True):
    st.session_state.student_nuid = 1004  
    st.switch_page('pages/07_Sankey.py')
