import streamlit as st
from modules.nav import SideBarLinks
import plotly.graph_objects as go


SideBarLinks()


# Streamlit page title
st.title("Circular Progress Bars")

# Function to create a donut chart
def create_donut_chart(percentage, title, color):
    fig = go.Figure(
        data=[go.Pie(
            values=[percentage, 100 - percentage],
            labels=["", ""],
            hole=0.7,
            marker=dict(colors=[color, "#2C2C2C"]),
            textinfo='none'
        )]
    )
    fig.update_layout(
        annotations=[
            dict(
                text=f"{percentage}%",
                x=0.5, y=0.5,
                font=dict(size=24, color=color),
                showarrow=False
            )
        ],
        title=dict(
            text=title,
            font=dict(size=20, color="white", family="Arial, sans-serif"),
            x=0.5,  # Center the title horizontally
            xanchor="center",  # Explicitly center the title
            y=.9  # Position the title at the top
        ),
        showlegend=False,
        margin=dict(t=70, b=20, l=20, r=20),  # Adjusted margins
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent background
        plot_bgcolor="rgba(0,0,0,0)"    # Transparent plot area
    )
    return fig

# Graph 1: Visa Interviews
fig1 = create_donut_chart(20, "Graph 1: Visa Interviews", "#FF4500")

# Graph 2: Success Rate
fig2 = create_donut_chart(65, "Graph 2: Success Rate", "#32CD32")

# Display the graphs in two columns
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
