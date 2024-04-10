import streamlit as st
from menu import client_menu
from pages.client_form import client_form
from utilities.db_utils import *



####################
## ADD NEW CLIENT ##
####################

# display the appropriate sidebar nav
client_menu()

data = {
        "first_name": "",
        "last_name": "",
        "budget": "",
        "preferred_move_date": "",
        "address_line_1": "",
        "address_line_2": "",
        "city": "",
        "state": "",
        "zip": "",
        "phone": "",
        "status": "",
        "agent_name": "",
        "sold": False
}

client_form("Add", data)