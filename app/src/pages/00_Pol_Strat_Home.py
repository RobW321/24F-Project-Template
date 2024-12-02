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

# Fake Data for Applications (mimicking SQL data)
applications = [
    {"name": "TechCorp", "status": "In Progress", "favorite": True, "page": "pages/01_TechCorp_Page.py"},
    {"name": "AutoWorks", "status": "Accepted", "favorite": True, "page": "pages/02_AutoWorks_Page.py"},
    {"name": "FinServ Inc.", "status": "Rejected", "favorite": False, "page": "pages/03_FinServ_Page.py"},
]

# Sort applications by favorite status
applications = sorted(applications, key=lambda x: not x['favorite'])

# Display each application as a button
for app in applications:
    # Format button text with details
    favorite_icon = "⭐" if app["favorite"] else "☆"
    status_icon = "✅" if app["status"] == "Accepted" else "❌" if app["status"] == "Rejected" else "⏳"
    button_text = f"{favorite_icon} {app['name']} - Status: {status_icon}"

    # Render button
    if st.button(button_text, type="primary", use_container_width=True, key=app["name"]):
        # Redirect to the application's specific page
        logger.info(f"Redirecting to page for {app['name']}")
        st.session_state['authenticated'] = True
        st.session_state['current_application'] = app['name']
        st.switch_page(app["page"])
