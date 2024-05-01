import streamlit as st
from menu import appointment_menu
from utilities.db_utils import *

from pages.appointment_form import appointment_form
from pages.choose_appointment import choose_appointment


# initialize session state variables
if 'appt_data' not in st.session_state:
    st.session_state['appt_data'] = None
if 'view_appt' not in st.session_state:
    st.session_state['view_appt'] = False

# display agent sidebar
appointment_menu()

# display titles
st.title("Real Estate Management System")

# button to reset the view and select another appointment
if st.button('Refresh Appointments'):
    st.session_state['appt_data'] = None
    st.session_state['view_appt'] = False

# display and handle the first form if no appointment is currently being viewed/edited
if st.session_state['appt_data'] is None or not st.session_state['view_appt']:
    data = choose_appointment()
    if data:
        st.session_state['appt_data'] = data
        st.session_state['view_appt'] = True

# display the appointment form if an agent has been selected
if st.session_state['appt_data'] and st.session_state['view_appt']:
    appointment_form("Update", st.session_state['appt_data'])
