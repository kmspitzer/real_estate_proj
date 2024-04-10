import streamlit as st
from datetime import datetime
from menu import agent_menu
from pages.validate_agent import validate_agent
from pages.standardize_phone import standardize_phone_number
from utilities.db_utils import *

from config.re_config import state_list



########################
## ADD NEW AGENT FORM ##
########################


# display the appropriate sidebar nav
agent_menu()

# display form and collect data
with st.form("agent_form"):
    st.write("## Add New Agent")

    # name
    first_name = st.text_input("First Name", max_chars=50).strip()
    last_name = st.text_input("Last Name", max_chars=50).strip()

    # address with state dropdown
    address_line_1 = st.text_input("Address Line 1", max_chars=90).strip()
    address_line_2 = st.text_input("Address Line 2", max_chars=50).strip()
    city = st.text_input("City", max_chars=30).strip()
    state = st.selectbox("State", state_list)
    zip = st.text_input("ZIP", max_chars=5).strip()

    # phone number
    phone = st.text_input("Phone", max_chars=15).strip()

    start_date = st.date_input("Start Date", 'today')

    # display submit button
    submitted = st.form_submit_button("Submit Agent")

    # when form is submitted, we edit
    if submitted:
        # gather input into dictionary
        data = {
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
            success = insert_agent(data)

            if success:
                st.success(f"Agent added.")
            else:
                st.error("An error occurred while adding the agent.")
