import streamlit as st
from datetime import datetime
from menu import appointment_menu
from pages.get_players import get_players
from pages.get_properties import get_properties
from pages.validate_appointment import validate_appointment
from utilities.db_utils import *

from config.re_config import state_list



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
        # collect the data into a dictionary
        data = {
                "agent_name": agent_name,
                "client_name": client_name,
                "property_address": property_address,
                "tour_date": tour_date,
                "tour_time": tour_time,
                "outcome": outcome
        }

        # validate form input
        err_message = validate_appointment(data)

        if err_message:
            # validation error occurred -- display message
            st.error(err_message)
        else:
            # get the agent_id, client_id and property_id from mappings
            data['agent_id'] = agent_mapping.get(agent_name)
            data['client_id'] = client_mapping.get(client_name)
            data['property_id'] = property_mapping.get(property_address)

            # need to store tour date and time as a timestamp in our database
            data['tour_datetime'] = datetime.combine(tour_date, tour_time)

            # call function to insert the record into the database
            success = insert_appointment(data)

            if success:
                st.success(f"Appointment added.")
            else:
                st.error("An error occurred while adding the appointment.")