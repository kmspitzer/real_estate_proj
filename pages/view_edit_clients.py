import streamlit as st
from menu import client_menu
from utilities.db_utils import *
from pages.get_players import get_players
from config.re_config import state_list
from pages.standardize_phone import standardize_phone_number

try:
    agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')

    # place holder
    client_menu()
    st.title("Clients")

    st.write(db_get_table("clients"))

    with st.form("client_form"):
        st.write("## Update Existing Client")

        client_id = st.text_input("Client ID", max_chars=10).strip()
        client = db_get_client_by_id(client_id)
        client.loc[client['Sold'] == "Yes", "Sold"] = 1
        client.loc[client['Sold'] == "No", "Sold"] = 0

        # name
        first_name = st.text_input("First Name", value=str(client['First Name'].values[0]), max_chars=50).strip()
        last_name = st.text_input("Last Name", value=str(client['Last Name'].values[0]), max_chars=50).strip()

        # budget
        budget = st.text_input("Budget", value=str(client['Budget'].values[0])).strip()

        # move date
        preferred_move_date = st.text_input("Preferred Move Date", value=str(client['Preferred Move Date'].values[0])).strip()

        # address with state dropdown
        address_line_1 = st.text_input("Address Line 1", value=str(client['Address Line 1'].values[0]), max_chars=90).strip()
        address_line_2 = st.text_input("Address Line 2", value=str(client['Address Line 2'].values[0]), max_chars=50).strip()
        city = st.text_input("City", value=str(client['City'].values[0]), max_chars=30).strip()
        state = st.text_input("State", value=str(client['State'].values[0])).strip()
        zip = st.text_input("ZIP", value=str(client['ZIP'].values[0]), max_chars=5).strip()

        # phone number
        phone = st.text_input("Phone", value=str(client['Phone'].values[0]), max_chars=15).strip()

        # client status
        status = st.text_input("Status", value=str(client['Status'].values[0])).strip()

        agent_id = st.text_input("Agent ID", value=str(client['Agent ID'].values[0])).strip()

        # sold checkbox
        sold = st.text_input("Sold", value=str(client['Sold'].values[0])).strip()

        # form submission button
        submitted = st.form_submit_button("Submit Client")

        # when form is submitted, we edit
        if submitted:
            # initialize a flag to track validation status
            validation_successful = True

            # check each field separately
            if not client_id.isdigit():
                st.error('A numeric client ID is required.')
                validation_successful = False

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


            # if all fields are valid, proceed to process the form
            if validation_successful:

                # collect the data into a dictionary
                data = {
                        "client_id": client_id,
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
                        "sold": sold,
                        "agent_id": agent_id
                }

                # call the function to insert the record into the database
                success = update_client(data)
                if success:
                    st.success(f"Client updated.")
                else:
                    st.error("An error occurred while updating the client.")
except AttributeError: 
    pass #Hide error that occurs when user hasn't inputted data yet