import streamlit as st
from datetime import datetime, time
from pages.get_players import get_players
from pages.get_properties import get_properties
from pages.validate_appointment import validate_appointment
from utilities.db_utils import *

from config.re_config import outcome_list


def appointment_form(action, data):
    ######################
    ## APPOINTMENT FORM ##
    ######################

    # get agent and client names for association
    agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')
    client_names, client_mapping = get_players('clients', 'client_id', 'client_name')
    property_addresses, property_mapping = get_properties()

    default_agent_index = agent_names.index(data['agent_name']) + 1 if data['agent_name'] in agent_names else 0
    default_client_index = client_names.index(data['client_name']) + 1 if data['client_name'] in client_names else 0
    default_property_index = property_addresses.index(data['property_address']) + 1 if data['property_address'] in property_addresses else 0
    default_outcome_index = outcome_list.index(data['outcome'] if data['outcome'] in outcome_list else "")

    tour_date_str = data.get('tour_date', 'today')  # Fallback to 'today' if not present
    if tour_date_str == 'today':
        tour_date_default = datetime.today().date()
    else:
        # Convert string to datetime.date object
        if isinstance(tour_date_str, date):
            tour_date_default = tour_date_str
        else:
            # Only parse if start_date_str is a string
            tour_date_default = datetime.strptime(tour_date_str, '%Y-%m-%d').date()

    tour_time_str = data.get('tour_time', 'now')  # Fallback to 'now' if not present
    if tour_time_str == 'now':
        tour_time_default = datetime.now().time()
    else:
        # Convert string to datetime.date object
        if isinstance(tour_time_str, time):
            tour_time_default = tour_time_str
        else:
            tour_time_default = datetime.strptime(tour_time_str, '%H:%M').time()

    # display form and collect data
    with st.form("appointment_form"):
        st.write(f"## {action} Appointment")

        # choose agent
        agent_name = st.selectbox("Agent Name", options=[''] + agent_names, index=default_agent_index)

        # choose client
        client_name = st.selectbox("Client Name", options=[''] + client_names, index=default_client_index)

        # choose property
        property_address = st.selectbox("Property", options=[''] + property_addresses, index=default_property_index)

        # tour date/time
        tour_date = st.date_input("Tour Date", value=tour_date_default)
        tour_time = st.time_input("Tour Time", value=tour_time_default)

        # outcome dropdown
        outcome = st.selectbox("Outcome", outcome_list, index=default_outcome_index)

        # form submission button
        submitted = st.form_submit_button(f"{action} Appointment")

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
                data['tour_datetime'] = datetime.combine(tour_date, tour_time).strftime('%Y-%m-%d %H:%M')

                if action == "Add":
                    # call function to insert the record into the database
                    success = insert_appointment(data)
                else:
                    # call function to update record in the database
                    success = update_appointment(data)

                if success:
                    st.success(f"Appointment {action.lower()}ed.")
                else:
                    st.error("An error occurred while adding the appointment.")