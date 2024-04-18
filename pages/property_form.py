import streamlit as st
from datetime import datetime
from pages.get_players import get_players
from pages.validate_property import validate_property
from utilities.db_utils import *

from config.re_config import state_list, type_list


###################
## PROPERTY FORM ##
###################

def property_form(action, data):
    # get agent names for association
    agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')

    default_agent_index = agent_names.index(data['agent_name']) if data['agent_name'] in agent_names else 0
    default_state_index = state_list.index(data['state']) if data['state'] in state_list else 0
    default_type_index = type_list.index(data['type']) if data['type'] in type_list else 0

    on_market_date_str = data.get('on_market_date', '')  # Fallback to '' if not present
    if on_market_date_str:
        on_market_date_str = datetime.strptime(on_market_date_str, '%Y-%m-%d').date()
    else:
        on_market_date_str = None

    off_market_date_str = data.get('off_market_date', '')  # Fallback to '' if not present
    if off_market_date_str:
        off_market_date_str = datetime.strptime(off_market_date_str, '%Y-%m-%d').date()
    else:
        off_market_date_str = None


    # display form and collect data
    with st.form("property_form"):
        st.write(f"## {action} Property")

        # address with state dropdown
        address_line_1 = st.text_input("Address Line 1", value=data["address_line_1"], max_chars=90).strip()
        address_line_2 = st.text_input("Address Line 2", value=data["address_line_2"], max_chars=50).strip()
        city = st.text_input("City", value=data["city"], max_chars=30).strip()
        state = st.selectbox("State", state_list, index=default_state_index)
        zip = st.text_input("ZIP", value=data["zip"], max_chars=5).strip()

        # original listing price
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
        with col2:
            original_listing_price = st.text_input("Original Listing Price", value=data["original_listing_price"])

        # sold price
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
        with col2:
            sold_price = st.text_input("Sold Price", value=data["sold_price"])

        # type of property
        type = st.selectbox("Type", type_list, index=default_type_index)

        # property characteristics
        sqft = st.text_input("Square Feet", value=data['sqft']).strip()
        bedrooms = st.text_input("Bedrooms", value=data["bedrooms"]).strip()
        bathrooms = st.text_input("Bathrooms", value=data['bathrooms']).strip()
        year_built = st.text_input("Year Built", value=data['year_built']).strip()

        # on/off market dates
        on_market = st.date_input("On Market Date", value=on_market_date_str)
        off_market = st.date_input("Off Market Date", value=off_market_date_str)

        # choose agent
        agent_name = st.selectbox("Agent Name", options=[''] + agent_names, index=default_agent_index)

        # spld checkbox
        sold = st.checkbox("Sold", value=data['sold'])

        # form submission button
        submitted = st.form_submit_button("Submit Property")

        # when form is submitted, we edit
        if submitted:
            # collect the data into a dictionary
            data = {
                    "address_line_1": address_line_1,
                    "address_line_2": address_line_2,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "original_listing_price": original_listing_price,
                    "sold_price": sold_price,
                    "type": type,
                    "sqft": sqft,
                    "bedrooms": bedrooms,
                    "bathrooms": bathrooms,
                    "year_built": year_built,
                    "on_market": on_market,
                    "off_market": off_market,
                    "agent_name": agent_name,
                    "sold": sold
            }

            # validate form input
            err_message = validate_property(data)

            if err_message:
                # validation error occurred -- display message
                st.error(err_message)
            else:
                # get the agent_id from mapping
                data['agent_id'] = agent_mapping.get(agent_name)

                if action == "Add":
                    # call function to insert the record into the database
                    success = insert_property(data)
                else:
                    st.write('action')
                    success = True
                
                if success:
                    st.success(f"Property {action.lower()}ed.")
                else:
                    st.error("An error occurred while adding the property.")