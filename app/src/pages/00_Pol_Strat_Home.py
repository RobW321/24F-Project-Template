import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

# Set up Streamlit page
st.set_page_config(layout='wide')

# Sidebar Links
SideBarLinks()

# Title
st.title(f"Welcome, {st.session_state.get('first_name', 'Guest')}.")
st.write("### Current Applications")

# Example data: List of applications
if 'applications' not in st.session_state:
    st.session_state['applications'] = [
        {"name": "Nvidia", "url": "https://www.nvidia.com/jobs", "status": "accepted", "favorite": True, "page": "pages/01_Nvidia_Page.py"},
        {"name": "Google", "url": "https://www.google.com/openings", "status": "pending", "favorite": True, "page": "pages/02_Google_Page.py"},
        {"name": "Apple", "url": "https://www.apple.com/careers", "status": "rejected", "favorite": False, "page": "pages/03_Apple_Page.py"},
        {"name": "Epic", "url": "https://www.epic.com/careers", "status": "accepted", "favorite": False, "page": "pages/04_Epic_Page.py"},
        {"name": "Facebook", "url": "https://www.facebook.com/job", "status": "pending", "favorite": False, "page": "pages/05_Facebook_Page.py"},
        {"name": "Steam", "url": "https://www.steam.com/jobs", "status": "pending", "favorite": True, "page": "pages/06_Steam_Page.py"},
        {"name": "Amazon", "url": "https://www.amazon.com/careers", "status": "rejected", "favorite": False, "page": "pages/07_Amazon_Page.py"},
        {"name": "AMD", "url": "https://www.amd.com/internships", "status": "rejected", "favorite": False, "page": "pages/08_AMD_Page.py"},
        {"name": "Samsung", "url": "https://www.samsung.com/careers", "status": "pending", "favorite": False, "page": "pages/09_Samsung_Page.py"},
    ]

# Sort applications by favorite status
applications = sorted(st.session_state['applications'], key=lambda x: not x['favorite'])

# Display each application as a button
for app in applications:
    # Format button text with details
    favorite_icon = "⭐" if app["favorite"] else "☆"
    status_icon = "✅" if app["status"] == "accepted" else "❌" if app["status"] == "rejected" else "⏳"
    button_text = f"{favorite_icon} {app['name']} - Status: {status_icon}"

    # Render button
    if st.button(button_text, type="primary", use_container_width=True, key=app["name"]):
        # Redirect to the application's specific page
        logger.info(f"Redirecting to page for {app['name']}")
        st.session_state['authenticated'] = True
        st.session_state['current_application'] = app['name']
        st.switch_page(app["page"])
