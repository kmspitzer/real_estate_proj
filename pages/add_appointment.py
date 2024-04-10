import streamlit as st
from datetime import datetime
from menu import appointment_menu
from pages.get_players import get_players
from pages.get_properties import get_properties
from utilities.db_utils import *



##############################
## ADD NEW APPOINTMENT FORM ##
##############################

# get agent and client names for association
agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')
client_names, client_mapping = get_players('clients', 'client_id', 'client_name')
property_addresses, property_mapping = get_properties()

# display the appropriate sidebar nav
appointment_menu()

# display form and collect data
with st.form("appointment_form"):
    st.write("## Add New Appointment")

    # choose agent
    agent_name = st.selectbox("Agent Name", options=[''] + agent_names)

    # choose client
    client_name = st.selectbox("Client Name", options=[''] + client_names)

    # choose property
    property_address = st.selectbox("Property", options=[''] + property_addresses)

    # tour date/time
    tour_date = st.date_input("Tour Date", value='today')
    tour_time = st.time_input("Tour Time", value='now')

    # outcome dropdown
    outcome = st.selectbox("Outcome", ['', 'Uninterested', 'Interested', 'Make Offer', 'Buy'])

    # form submission button
    submitted = st.form_submit_button("Submit Appointment")

    # when form is submitted, we edit
    if submitted:
        # initialize a flag to track validation status
        validation_successful = True

        # check each field separately
        if not tour_date:
            st.error('Tour Date is required.')
            validation_successful = False

        if not tour_time:
            st.error('Tour Time is required.')
            validation_successful = False

        if not agent_name:
            st.error('Agent Name is required.')
            validation_successful = False

        if not client_name:
            st.error('Client Name is required.')
            validation_successful = False

        if not property_address:
            st.error('Property is required.')
            validation_successful = False

        outcome_value = outcome
        if outcome_value == "":
            outcome_value = None

        # if all fields are valid, proceed to process the form
        if validation_successful:
            # get the agent_id from our mapping
            agent_id = agent_mapping.get(agent_name)
            client_id = client_mapping.get(client_name)
            property_id = property_mapping.get(property_address)

            # need to store tour date and time as a timestamp in our database
            tour_datetime = datetime.combine(tour_date, tour_time)

            # collect the data into a dictionary
            data = {
                    "agent_id": agent_id,
                    "client_id": client_id,
                    "property_id": property_id,
                    "tour_datetime": tour_datetime,
                    "outcome": outcome_value
            }

            # call the function to insert the record into the database
            success = insert_appointment(data)
            print(f'db output: {success}')
            if success:
                st.success(f"Appointment added.")
            else:
                st.error("An error occurred while adding the appointment.")