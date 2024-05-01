import streamlit as st
from datetime import datetime
from menu import agent_menu
from pages.agent_form import agent_form
from utilities.db_utils import *

from config.re_config import state_list



########################
## ADD NEW AGENT FORM ##
########################


# display the appropriate sidebar nav
agent_menu()
st.title("Real Estate Management System")

data = {
        "agent_id": "",
        "first_name": "",
        "last_name": "",
        "address_line_1": "",
        "address_line_2": "",
        "city": "",
        "state": "",
        "zip": "",
        "phone": "",
        "start_date": "today"
}

agent_form("Add", data)
