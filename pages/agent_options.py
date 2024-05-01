import streamlit as st
from menu import agent_menu
from utilities.db_utils import *


# agent hub
agent_menu()
st.title("Real Estate Management System")
st.write("## Agents")