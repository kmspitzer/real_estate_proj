import streamlit as st
from menu import client_menu
from utilities.db_utils import *


# client hub
client_menu()
st.title("Real Estate Management System")
st.write("## Clients")

