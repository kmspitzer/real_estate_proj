import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

from pages.agent_form import agent_form
from pages.choose_agent import choose_agent


# initialize session state variables
if 'agent_data' not in st.session_state:
    st.session_state['agent_data'] = None
if 'view_agent' not in st.session_state:
    st.session_state['view_agent'] = False

# display agent sidebar
agent_menu()

# display titles
st.title("Real Estate Management System")

# button to reset the view and select another agent
if st.button('Refresh Agents'):
    st.session_state['agent_data'] = None
    st.session_state['view_agent'] = False

# display and handle the first form if no agent is currently being viewed/edited
if st.session_state['agent_data'] is None or not st.session_state['view_agent']:
    data = choose_agent()
    if data:
        st.session_state['agent_data'] = data
        st.session_state['view_agent'] = True

# display the agent form if an agent has been selected
if st.session_state['agent_data'] and st.session_state['view_agent']:
    agent_form("Update", st.session_state['agent_data'])
