import streamlit as st
from menu import property_menu
from utilities.db_utils import *


# properties hub
property_menu()
st.title("Real Estate Management System")
st.write("## Properties")
