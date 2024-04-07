import streamlit as st
from menu import client_menu
from pages.get_players import get_players
from pages.standardize_phone import standardize_phone_number
from utilities.db_utils import *

from config.re_config import state_list



#########################
## ADD NEW CLIENT FORM ##
#########################

# get agent names for association
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
        # initialize a flag to track validation status
        validation_successful = True

        # check each field separately
        if not first_name:
            st.error('First Name is required.')
            validation_successful = False

        if not last_name:
            st.error('Last Name is required.')
            validation_successful = False

        # handle budget as a special case because it can be None
        if budget == "":
            budget_value = None
        else:
            try:
                # remove commas for database
                budget_value = int(budget.replace(",", "").strip())
            except ValueError:
                st.error("Please enter a valid number for Budget.")
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

        if not status:
            st.error('Status is required.')
            validation_successful = False

        if not agent_name:
            st.error('Agent Name is required.')
            validation_successful = False

        # if all fields are valid, proceed to process the form
        if validation_successful:
            # get the agent_id from our mapping
            agent_id = agent_mapping.get(agent_name)

            # collect the data into a dictionary
            data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "budget": budget_value,
                    "preferred_move_date": preferred_move_date,
                    "address_line_1": address_line_1,
                    "address_line_2": address_line_2,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phone": phone,
                    "status": status,
                    "agent_id": agent_id,
                    "sold": sold
            }

            # call the function to insert the record into the database
            success = insert_client(data)
            if success:
                st.success(f"Client added.")
            else:
                st.error("An error occurred while adding the client.")