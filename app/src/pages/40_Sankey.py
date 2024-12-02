import streamlit as st
from modules.nav import SideBarLinks
import plotly.graph_objects as go

SideBarLinks()

# Streamlit page title
st.title("Sankey Diagram Example")

# Fake data for the Sankey diagram
data = {
    "sources": [0, 0, 1, 1, 2],
    "targets": [1, 2, 3, 4, 4],
    "values": [8, 4, 2, 6, 3],
    "labels": ["Start", "Process A", "Process B", "Outcome A", "Outcome B"]
}

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=data["labels"]
    ),
    link=dict(
        source=data["sources"],
        target=data["targets"],
        value=data["values"]
    )
)])

# Display the Sankey diagram in Streamlit
st.plotly_chart(fig)
