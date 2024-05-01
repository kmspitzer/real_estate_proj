import streamlit as st
from datetime import datetime, date
from pages.validate_agent import validate_agent
from pages.standardize_phone import standardize_phone_number
from utilities.db_utils import *

from config.re_config import state_list


def agent_form(action, data):
    ################
    ## AGENT FORM ##
    ################
    default_state_index = state_list.index(data['state']) if data['state'] in state_list else 0

    start_date_str = data.get('start_date', 'today')  # Fallback to 'today' if not present
    if start_date_str == 'today':
        start_date_default = datetime.today().date()
    else:
        # Convert string to datetime.date object
        if isinstance(start_date_str, date):
            start_date_default = start_date_str
        else:
            # Only parse if start_date_str is a string
            start_date_default = datetime.strptime(start_date_str, '%Y-%m-%d').date()

    # display form and collect data
    with st.form("agent_form"):
        st.write(f"## {action} Agent")

        # name
        first_name = st.text_input("First Name", value=data['first_name'], max_chars=50).strip()
        last_name = st.text_input("Last Name", value=data['last_name'], max_chars=50).strip()

        # address with state dropdown
        address_line_1 = st.text_input("Address Line 1", value=data['address_line_1'], max_chars=90).strip()
        address_line_2 = st.text_input("Address Line 2", value=data['address_line_2'], max_chars=50).strip()
        city = st.text_input("City", value=data['city'], max_chars=30).strip()
        # Find the index of the state in state_list. If not found, default to 0 (or any other default index)

        # Use the index parameter to set the default selection
        state = st.selectbox("State", state_list, index=default_state_index)

        zip = st.text_input("ZIP", value=data['zip'], max_chars=5).strip()

        # phone number
        phone = st.text_input("Phone", value=data['phone'], max_chars=15).strip()

        start_date = st.date_input("Start Date", start_date_default)


        # form submission button
        db_submitted = st.form_submit_button(f"{action} Agent")

        # when form is submitted, we edit
        if db_submitted:
            # gather input into dictionary
            data = {
                    "agent_id": data['agent_id'],
                    "first_name": first_name,
                    "last_name": last_name,
                    "address_line_1": address_line_1,
                    "address_line_2": address_line_2,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phone": phone,
                    "start_date": start_date
            }

            # validate form input
            err_message = validate_agent(data)

            if err_message:
                # validation error occurred -- display message
                st.error(err_message)
            else:
                # format phone number
                data['phone'] = standardize_phone_number(phone)

                # call function to insert the record into the database
                if action == "Add":
                    success = insert_agent(data)
                else:
                    success = update_agent(data)

                if success:
                    st.success(f"Agent {action.lower()}ed.")
                else:
                    st.error("An error occurred while adding the agent.")
