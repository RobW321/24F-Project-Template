import streamlit as st
from modules.nav import SideBarLinks

# Sidebar navigation
SideBarLinks()

# Page title
st.title("About NUTracks")

# Section 1: Introduction
st.header("Introduction")
st.markdown(
    """
    In today’s competitive tech job market, students often find themselves applying to hundreds of co-ops and internships just to secure a single interview. This process tends to be overwhelming and unorganized, with many resorting to basic spreadsheets or notes apps that lack the tools needed to track progress efficiently.
    """
)

# Section 2: Purpose of NUTracks
st.header("Why NUTracks?")
st.markdown(
    """
    **NUTracks** is a data-driven job application tracker tailored specifically for co-op searches. It allows students to:
    - Organize, filter, and prioritize applications with ease.
    - Track their application statuses and success rates.
    - Gain insights into response times, interview stages, and compensation trends.
    """
)

# Section 3: Unique Features
st.header("What Makes NUTracks Different?")
st.markdown(
    """
    Unlike traditional solutions, NUTracks focuses on addressing the lack of guidance and transparency in the co-op search process. Key features include:
    - **Tailored tracking tools** for users like Joe (first-time applicants) and Josh (data-driven users).
    - **Actionable data insights** to help students make informed decisions about their applications.
    - **Visualization tools**, such as Sankey flow charts, for a clear depiction of application progress over time.
    """
)

# Section 4: Empowering Students
st.header("Empowering Students")
st.markdown(
    """
    NUTracks combines personalized tracking with collective data insights to help students navigate the co-op search process with confidence and clarity. By leveraging our tools, users can streamline their job search and increase their chances of success.
    """
)

# Section 5: Features Overview
st.header("Key Features")
st.markdown(
    """
    - Track the number of companies applied to and the status of each application.
    - Set priority levels based on data insights.
    - View a clear, visual timeline of applications through Sankey flow charts.
    """
)

# Section 6: Meet the Team
st.header("Meet the Team")
st.markdown(
    """
    Our team is made up of talented and dedicated individuals who worked together to bring NUTracks to life:
    - **Christian Bacalhau** ([ChristianBacalhau](https://github.com/ChristianBacalhau))
    - **Robel Wondwosen** ([RobW321](https://github.com/RobW321))
    - **Matthew Faust** ([MatthewFaust](https://github.com/MatthewFaust))
    - **Samson Ajayi** ([sajayi12](https://github.com/sajayi12))
    - **Gurshan Sidhu** ([gurshan-sidhu](https://github.com/gurshan-sidhu))
    - **Rohan Batra** ([StubblySeeker](https://github.com/StubblySeeker))
    """
)
