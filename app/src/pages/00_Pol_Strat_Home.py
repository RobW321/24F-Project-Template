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
applications = [
    {"name": "Nvidia", "url": "Nvidia.com/jobs", "status": "accepted", "favorite": True},
    {"name": "Google", "url": "Google.com/openings", "status": "pending", "favorite": True},
    {"name": "Apple", "url": "Apple.com/careers", "status": "rejected", "favorite": False},
    {"name": "Epic", "url": "Epic.com/careers", "status": "accepted", "favorite": False},
    {"name": "Facebook", "url": "Facebook.com/job", "status": "pending", "favorite": False},
    {"name": "Steam", "url": "Steam.com/jobs", "status": "pending", "favorite": True},
    {"name": "Amazon", "url": "Amazon.com/careers", "status": "rejected", "favorite": False},
    {"name": "AMD", "url": "AMD.com/internships", "status": "rejected", "favorite": False},
    {"name": "Samsung", "url": "Samsung.com/careers", "status": "pending", "favorite": False},
]

# Sort applications by favorite status
applications = sorted(applications, key=lambda x: not x['favorite'])

# Add sorting header
col1, col2 = st.columns([6, 1])  # Adjust widths as needed
with col1:
    st.write("Sort By: **Favorites**, Status")  # Placeholder for sorting logic
with col2:
    st.write(" ")

# Display applications in a table-like layout
for app in applications:
    # Outline each row with a box
    with st.container():
        cols = st.columns([1, 4, 3, 1])  # Adjust column widths for alignment

        # Favorite toggle (star)
        with cols[0]:
            if st.button("⭐" if app["favorite"] else "☆", key=f"fav_{app['name']}"):
                app["favorite"] = not app["favorite"]  # Toggle favorite status

        # Application name and URL
        with cols[1]:
            st.markdown(f"<div style='border: 1px solid #ccc; padding: 5px;'>"
                        f"<a href='{app['url']}' target='_blank'>{app['name']}</a>"
                        f"</div>",
                        unsafe_allow_html=True)

        # Single status button
        with cols[2]:
            current_status = app["status"]
            if current_status == "accepted":
                button_label = "✅ Accepted"
            elif current_status == "rejected":
                button_label = "❌ Rejected"
            else:
                button_label = "⏳ Pending"

            # Clickable button to toggle status
            if st.button(button_label, key=f"status_{app['name']}"):
                # Cycle through statuses: pending -> accepted -> rejected
                if current_status == "pending":
                    app["status"] = "accepted"
                elif current_status == "accepted":
                    app["status"] = "rejected"
                elif current_status == "rejected":
                    app["status"] = "pending"

        # Border styling for each row
        with cols[3]:
            st.write("")
