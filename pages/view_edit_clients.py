import streamlit as st
from menu import client_menu
from utilities.db_utils import *

# place holder
client_menu()
st.title("Clients")

st.write(db_get_table("clients"))