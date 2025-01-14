# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ Ticket Management ------------------------
def EditTicketNav():
    st.sidebar.page_link("pages/62_Edit_Ticket.py", label="Edit Ticket", icon="✏️")


def ReassignTicketNav():
    st.sidebar.page_link("pages/61_Reassign_Ticket.py", label="Reassign Ticket", icon="🔄")


def ViewTicketsNav():
    st.sidebar.page_link("pages/60_View_Tickets.py", label="View Tickets", icon="📋")


def SakaiHomePage():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="Admin Home", icon="👤")


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

def JoeHomePage():
    st.sidebar.page_link("pages/06_Joe_Home.py", label="Joe Home", icon="👤")

def JoshHomePage():
    st.sidebar.page_link("pages/07_Josh_Home.py", label="Josh Home", icon="👤")

def ThomasHomePage():
    st.sidebar.page_link("pages/09_Thomas_Home.py", label="Thomas Home", icon="👤")

def KyrieHomePage():
    st.sidebar.page_link("pages/05_Kyrie_Home.py", label="Kyrie Home", icon="👤")



#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def PolStratAdvHomeNav():
    st.sidebar.page_link(
        "pages/00_Pol_Strat_Home.py", label="Political Strategist Home", icon="👤"
    )


def WorldBankVizNav():
    st.sidebar.page_link(
        "pages/01_World_Bank_Viz.py", label="World Bank Visualization", icon="🏦"
    )


def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demonstration", icon="🗺️")


## ------------------------ Examples for Role of usaid_worker ------------------------
def ApiTestNav():
    st.sidebar.page_link("pages/12_Get_Applications.py", label="Test the API", icon="🛜")


def PredictionNav():
    st.sidebar.page_link(
        "pages/11_Prediction.py", label="Regression Prediction", icon="📈"
    )


def ClassificationNav():
    st.sidebar.page_link(
        "pages/13_Classification.py", label="Classification Demo", icon="🌺"
    )




def ThomasHome():
    st.sidebar.page_link(
        "pages/09_Thomas_Home.py", label="Thomas Home", icon="🏦"
    )
















## ------------------------ Examples for Role of usaid_worker ------------------------

























# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=True):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=250)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    ## if show_home:
        # Show the Home page link (the landing page)

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "usaid_worker":
            PredictionNav()
            ApiTestNav()
            ClassificationNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            SakaiHomePage()

        if st.session_state["role"] == "joe_student":
            JoeHomePage()

        if st.session_state["role"] == "josh_student":
            JoshHomePage()
        
        if st.session_state["role"] == "thomas_student":
            ThomasHomePage()

        if st.session_state["role"] == "kyrie_student":
            KyrieHomePage()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")

def AboutPage():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")
        
