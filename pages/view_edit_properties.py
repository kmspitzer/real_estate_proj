import streamlit as st
from menu import property_menu
from utilities.db_utils import *

from pages.property_form import property_form
from pages.choose_property import choose_property


# initialize session state variables
if 'property_data' not in st.session_state:
    st.session_state['property_data'] = None
if 'view_property' not in st.session_state:
    st.session_state['view_property'] = False

# display agent sidebar
property_menu()

# display titles
st.title("Real Estate Management System")

# button to reset the view and select another agent
if st.button('Refresh Properties'):
    st.session_state['property_data'] = None
    st.session_state['view_property'] = False

# display and handle the first form if no client is currently being viewed/edited
if st.session_state['property_data'] is None or not st.session_state['view_property']:
    data = choose_property()
    if data:
        st.session_state['property_data'] = data
        st.session_state['view_property'] = True

# display the agent form if an agent has been selected
if st.session_state['property_data'] and st.session_state['view_property']:
    property_form("Update", st.session_state['property_data'])