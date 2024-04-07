import streamlit as st
from menu import menu

#######################################
## ENTRY POINT TO REAL ESTATE SYSTEM ##
#######################################

# initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# login selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "Client", "Agent", "Agent Manager"],
    key="_role",
    on_change=set_role,
)

# render dynamic menu
menu()