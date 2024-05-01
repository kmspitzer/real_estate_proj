import streamlit as st
from menu import authenticated_menu
from utilities.db_utils import *
from utilities.real_estate_utils import *

# place holder for client view of properties
authenticated_menu()
st.title("Real Estate Management System")
st.write("## Properties")

apply_custom_css()

 # get agents for display on screen
st.write(db_get_properties_display().to_html(index=False), unsafe_allow_html=True)