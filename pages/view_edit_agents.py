import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

# place holder
agent_menu()
st.title("View/Edit Agents")

st.write(db_get_table("agents"))