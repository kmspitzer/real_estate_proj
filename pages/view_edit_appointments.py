import streamlit as st
from menu import appointment_menu
from utilities.db_utils import *

# place holder
appointment_menu()
st.title("View/Edit Appointments")

st.write(db_get_table("appointments"))