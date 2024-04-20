import streamlit as st
from menu import appointment_menu
from datetime import datetime
from utilities.db_utils import *
from pages.get_players import get_players
from pages.get_properties import get_properties

agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')
client_names, client_mapping = get_players('clients', 'client_id', 'client_name')
property_addresses, property_mapping = get_properties()

# place holder
appointment_menu()
st.title("View/Edit Appointments")

st.write(db_get_table("appointments"))

with st.form("appointment_form"):
    st.write("## Update Existing Appointment")

    # tour date/time
    tour_datetime = st.text_input("Tour Datetime", max_chars=19).strip()
    agent_id = st.text_input("Agent ID", max_chars=10).strip()
    property_id = st.text_input("Property ID", max_chars=10).strip()
    client_id = st.text_input("Client ID", max_chars=10).strip()
    appointments = db_get_appointment_by_id(agent_id, client_id, property_id, tour_datetime)

    # outcome
    outcome = st.text_input("Outcome (Possible values: Uninterested, Interested, Make Offer, Buy)", value=str(appointments['Outcome'].values[0]))

    # form submission button
    submitted = st.form_submit_button("Submit Appointment")

    # when form is submitted, we edit
    if submitted:
        # initialize a flag to track validation status
        validation_successful = True

        # check each field separately
        if not tour_datetime:
            st.error('Tour Datetime is required.')
            validation_successful = False

        outcome_value = outcome
        if outcome_value == "":
            outcome_value = None
        if outcome_value not in ['Uninterested', 'Interested', 'Make Offer', 'Buy']:
            st.error('Not a valid outcome')
            validation_successful = False

        # if all fields are valid, proceed to process the form
        if validation_successful:

            # collect the data into a dictionary
            data = {
                    "agent_id": agent_id,
                    "client_id": client_id,
                    "property_id": property_id,
                    "tour_datetime": tour_datetime,
                    "outcome": outcome_value
            }

            # call the function to insert the record into the database
            success = update_appointment(data)
            print(f'db output: {success}')
            if success:
                st.success(f"Appointment updated.")
            else:
                st.error("An error occurred while updating the appointment.")