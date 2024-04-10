import streamlit as st
from menu import authenticated_menu
from utilities.db_utils import *

# place holder for client view of properties
authenticated_menu()
st.title("Properties")

st.write(db_get_table("properties"))