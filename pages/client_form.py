import streamlit as st
from datetime import datetime
from pages.get_players import get_players
from pages.validate_client import validate_client
from pages.standardize_phone import standardize_phone_number
from utilities.db_utils import *

from config.re_config import state_list, status_list


def client_form(action, data):
    ##################
    ##  CLIENT FORM ##
    ##################
    # get the index for the state dropdown
    default_state_index = state_list.index(data['state']) if data['state'] in state_list else 0

    # if no date is specified, we default to today
    move_date_str = data.get('preferred_move_date', '')  # Fallback to '' if not present
    if move_date_str:
        # convert string to datetime.date object
        if isinstance(move_date_str, date):
            move_date_default = move_date_str
        else:
            # only parse if start_date_str is a string
            move_date_default = datetime.strptime(move_date_str, '%Y-%m-%d').date()
    else:
        # can be empty
        move_date_default = None

    # get agent names for association and determine index for dropdown
    agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')
    default_agent_index = agent_names.index(data['agent_name']) + 1 if data['agent_name'] in agent_names else 0
    default_status_index = status_list.index(data['status']) if data['status'] in status_list else 0

    # display form and collect data
    with st.form("client_form"):
        st.write(f"## {action} Client")

         # name
        first_name = st.text_input("First Name", value=data['first_name'], max_chars=50).strip()
        last_name = st.text_input("Last Name", value=data['last_name'], max_chars=50).strip()

        # budget
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
        with col2:
            budget = st.text_input("Budget", value=data["budget"])

        # move date
        preferred_move_date = st.date_input("Preferred Move Date", value=move_date_default)

        # address with state dropdown
        address_line_1 = st.text_input("Address Line 1", value=data['address_line_1'], max_chars=90).strip()
        address_line_2 = st.text_input("Address Line 2", value=data['address_line_2'], max_chars=50).strip()
        city = st.text_input("City", value=data['city'], max_chars=30).strip()
        state = st.selectbox("State", state_list, index=default_state_index)
        zip = st.text_input("ZIP", value=data['zip'], max_chars=5).strip()

        # phone number
        phone = st.text_input("Phone", value=data['phone'], max_chars=15).strip()

        # client status
        status = st.selectbox("Status", status_list, index=default_status_index)

        # choose agent
        agent_name = st.selectbox("Agent Name", options=[''] + agent_names, index=default_agent_index)

        # sold checkbox
        sold = st.checkbox("Sold", value=data['sold'])

        # form submission button
        submitted = st.form_submit_button("Submit Client")

        # when form is submitted, we edit
        if submitted:
            # collect the data into a dictionary
            if action == "Update":
                # format key from original data
                data = {
                    "client_id": data["client_id"]
                }

            # format data items from input
            data["first_name"] = first_name
            data["last_name"] = last_name
            data["budget"] = budget
            data["preferred_move_date"] = preferred_move_date
            data["address_line_1"] = address_line_1
            data["address_line_2"] = address_line_2
            data["city"] = city
            data["state"] = state
            data["zip"] = zip
            data["phone"] = phone
            data["status"] = status
            data["agent_name"] = agent_name
            data["sold"] = sold

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
                print(data['agent_id'])

                if action == "Add":
                    # call function to insert the record into the database
                    success = insert_client(data)
                    report_action = "added"
                else:
                    # call function to update the record in the database
                    success = update_client(data)
                    report_action = "updated"
                    
                if success:
                    st.success(f"Client {report_action}.")
                else:
                    st.error("An error occurred while adding the client.")