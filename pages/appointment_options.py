import streamlit as st
from menu import appointment_menu
from utilities.db_utils import *


# appointment hub
appointment_menu()
st.title("Real Estate Management System")
st.write("## Appointments")