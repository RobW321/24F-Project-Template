import logging
import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from modules.nav import SideBarLinks

# Set up logging
logger = logging.getLogger(__name__)

# Add sidebar links
SideBarLinks()

if "student_nuid" in st.session_state and st.session_state.student_nuid is not None:
    student_nuid = st.session_state.student_nuid

# Title
st.title("Dynamic Sankey Diagram")

"""
Viewing the Flow of Applications Across Status Categories
"""

# Fetch data from the Flask API

API_URL = "http://api:4000/a/flowchart"

try:
    response = requests.get(f"{API_URL}/{student_nuid}")
    response.raise_for_status()  # Raise an error if the response status code is not 200
    data = response.json()
except Exception as e:
    st.error("Failed to fetch data from the API.")
    st.error(f"Error details: {e}")
    data = []

# Process and display data
if data:
    # Convert API data into a Pandas DataFrame
    df = pd.DataFrame(data, columns=["FlowChartID", "NumApplications", "NumProgress", "NumRejected", "NumAccepted"])

    # Check if the DataFrame contains the necessary columns
    required_columns = ["NumApplications", "NumProgress", "NumRejected", "NumAccepted"]
    if not all(column in df.columns for column in required_columns):
        st.error("API data does not contain the required columns.")
    else:
        # Aggregate data
        total_applications = df["NumApplications"].sum()
        num_progress = df["NumProgress"].sum()
        num_rejected = df["NumRejected"].sum()
        num_accepted = df["NumAccepted"].sum()

        # Display totals
        st.write("### Total Numbers")
        st.write(f"**Total Applications:** {total_applications}")
        st.write(f"**In Progress:** {num_progress}")
        st.write(f"**Rejected:** {num_rejected}")
        st.write(f"**Accepted:** {num_accepted}")

        # Sankey Diagram Data
        labels = ["Total Applications", "In Progress", "Rejected", "Accepted"]
        source = [0, 0, 0]  # Total Applications is the source
        target = [1, 2, 3]  # Targets are In Progress, Rejected, Accepted
        values = [num_progress, num_rejected, num_accepted]

        # Generate Sankey Diagram
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=labels,
            ),
            link=dict(
                source=source,
                target=target,
                value=values,
            )
        )])

        fig.update_layout(title_text="Application Flow Sankey Diagram", font_size=10)

        # Display Sankey Diagram
        st.plotly_chart(fig)
else:
    st.write("No data available.")