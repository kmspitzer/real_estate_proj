import streamlit as st
from menu import client_menu
from utilities.db_utils import *

from pages.client_form import client_form
from pages.choose_client import choose_client


# initialize session state variables
if 'client_data' not in st.session_state:
    st.session_state['client_data'] = None
if 'view_client' not in st.session_state:
    st.session_state['view_client'] = False

# display client sidebar
client_menu()

# display titles
st.title("Real Estate Management System")

# button to reset the view and select another client
if st.button('Refresh Clients'):
    st.session_state['client_data'] = None
    st.session_state['view_client'] = False

# display and handle the first form if no client is currently being viewed/edited
if st.session_state['client_data'] is None or not st.session_state['view_client']:
    data = choose_client()
    if data:
        st.session_state['client_data'] = data
        st.session_state['view_client'] = True

# display the client form if an client has been selected
if st.session_state['client_data'] and st.session_state['view_client']:
    client_form("Update", st.session_state['client_data'])
