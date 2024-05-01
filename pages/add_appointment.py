import streamlit as st
from datetime import datetime
from menu import appointment_menu
from pages.appointment_form import appointment_form
from utilities.db_utils import *




#######################
##  ADD APPOINTMENT  ##
#######################
# display the appropriate sidebar nav and
# system title
appointment_menu()
st.title("Real Estate Management System")

# initialize data object for new appointment
data = {
        "agent_name": "",
        "client_name": "",
        "property_address": "",
        "tour_date": "today",
        "tour_time": "now",
        "outcome": ""
}

# display appointment form
appointment_form("Add", data)
