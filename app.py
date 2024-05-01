import streamlit as st
from menu import menu
from utilities.real_estate_utils import *

#######################################
## ENTRY POINT TO REAL ESTATE SYSTEM ##
#######################################
apply_custom_css()
# initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role

st.title("Real Estate Management System")

# Role selection box
role_selected = st.selectbox(
    "Select your role:",
    [None, "Client", "Agent", "Agent Manager"],
    key="_role",
    on_change=set_role,
)

# Button to confirm role selection and proceed
if st.button("Confirm Role"):
    if st.session_state.role is not None:
        # If a role is selected and confirmed, render the appropriate menu
        menu()
    else:
        # If no role is selected and button is pressed, notify the user
        st.warning("Please select a role to proceed.")
else:
    # Initial message or any other instructions before role confirmation
    st.info("Please select and confirm your role to access the system.")