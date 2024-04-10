import streamlit as st
from menu import client_menu
from pages.get_players import get_players
from pages.validate_client import validate_client
from pages.standardize_phone import standardize_phone_number
from utilities.db_utils import *

from config.re_config import state_list



#########################
## ADD NEW CLIENT FORM ##
#########################

# get agent names for association
df = db_get_table('agents')
agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')

# display the appropriate sidebar nav
client_menu()

# display form and collect data
with st.form("client_form"):
    st.write("## Add New Client")

    # name
    first_name = st.text_input("First Name", max_chars=50).strip()
    last_name = st.text_input("Last Name", max_chars=50).strip()

    # budget
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
    with col2:
        budget = st.text_input("Budget", value="")

    # move date
    preferred_move_date = st.date_input("Preferred Move Date", value=None)

    # address with state dropdown
    address_line_1 = st.text_input("Address Line 1", max_chars=90).strip()
    address_line_2 = st.text_input("Address Line 2", max_chars=50).strip()
    city = st.text_input("City", max_chars=30).strip()
    state = st.selectbox("State", state_list)
    zip = st.text_input("ZIP", max_chars=5).strip()

    # phone number
    phone = st.text_input("Phone", max_chars=15).strip()

    # client status
    status = st.selectbox("Status", ['', 'Prospective', 'In Progress', 'Closed'])

    # choose agent
    agent_name = st.selectbox("Agent Name", options=[''] + agent_names)

    # sold checkbox
    sold = st.checkbox("Sold")


    # form submission button
    submitted = st.form_submit_button("Submit Client")

    # when form is submitted, we edit
    if submitted:
        # collect the data into a dictionary
        data = {
                "first_name": first_name,
                "last_name": last_name,
                "budget": budget,
                "preferred_move_date": preferred_move_date,
                "address_line_1": address_line_1,
                "address_line_2": address_line_2,
                "city": city,
                "state": state,
                "zip": zip,
                "phone": phone,
                "status": status,
                "agent_name": agent_name,
                "sold": sold
        }

        # validate form input
        err_message = validate_client(data)

        if err_message:
            # validation error occurred -- display message
            st.error(err_message)
        else:
            # format phone number
            data['phone'] = standardize_phone_number(data['phone'])

            # get the agent_id from mapping
            data['agent_id'] = agent_mapping.get(agent_name)

            # call function to insert the record into the database
            success = insert_client(data)
            
            if success:
                st.success(f"Client added.")
            else:
                st.error("An error occurred while adding the client.")