import streamlit as st
from datetime import datetime
from menu import appointment_menu
from pages.appointment_form import appointment_form
from utilities.db_utils import *




#######################
##  ADD APPOINTMENT  ##
#######################
# display the appropriate sidebar nav
appointment_menu()

data = {
        "agent_name": "",
        "client_name": "",
        "property_address": "",
        "tour_date": "today",
        "tour_time": "now",
        "outcome": ""
}

appointment_form("Add", data)
