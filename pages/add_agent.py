import streamlit as st
from menu import agent_menu
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


    # form submission button
    submitted = st.form_submit_button("Submit Agent")

    # when form is submitted, we edit
    if submitted:
        # initialize a flag to track validation status
        validation_successful = True

        # check each field separately
        if not first_name:
            st.error('First Name is required.')
            validation_successful = False

        if not last_name:
            st.error('Last Name is required.')
            validation_successful = False

        if not address_line_1:
            st.error('Address Line 1 is required.')
            validation_successful = False

        if not city:
            st.error('City is required.')
            validation_successful = False

        if not state:
            st.error('State is required.')
            validation_successful = False

        # ensure zip is 5-digit
        if len(zip) != 5 or not zip.isdigit():
            st.error('A valid ZIP code is required.')
            validation_successful = False

        # standardize phone number (nnn) nnn-nnnn
        # as long as we get 10 digits
        try:
            phone = standardize_phone_number(phone)
        except:
            st.error('Enter valid Phone.')
            validation_successful = False

        # if all fields are valid, proceed to process the form
        if validation_successful:

            # collect the data into a tuple
            data = (first_name, last_name, address_line_1, address_line_2, city, state, zip,
                     phone, start_date
            )

            # call the function to insert the record into the database
            agent_id = insert_agent(data)
            if agent_id:
                st.success(f"Agent added with ID: {agent_id}")
            else:
                st.error("An error occurred while adding the agent.")