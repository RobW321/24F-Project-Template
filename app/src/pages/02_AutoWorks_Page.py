import streamlit as st

# Page Title
st.title("AutoWorks - Application Details")
from modules.nav import SideBarLinks

SideBarLinks()

# Retrieve application details
app_name = "AutoWorks"
status = st.session_state.get(f"{app_name}_status", "Accepted")
favorite = st.session_state.get(f"{app_name}_favorite", True)

# Update Status
st.write("### Update Status")
new_status = st.selectbox(
    "Select Status",
    ["In Progress", "Accepted", "Rejected"],
    index=["In Progress", "Accepted", "Rejected"].index(status)
)
if st.button("Update Status"):
    st.session_state[f"{app_name}_status"] = new_status
    st.success(f"Status updated to {new_status}")

# Update Favorite
st.write("### Update Favorite")
new_favorite = st.checkbox("Favorite", value=favorite)
if st.button("Update Favorite"):
    st.session_state[f"{app_name}_favorite"] = new_favorite
    st.success(f"Favorite updated to {'Yes' if new_favorite else 'No'}")
