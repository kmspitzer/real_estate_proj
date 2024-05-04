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

    # get indexes for dropdowns
    default_agent_index = agent_names.index(data['agent_name']) + 1 if data['agent_name'] in agent_names else 0
    default_state_index = state_list.index(data['state']) if data['state'] in state_list else 0
    default_type_index = type_list.index(data['type']) if data['type'] in type_list else 0

    # initialize date fields
    on_market_date_str = data.get('on_market_date', '')  # Fallback to today if not present
    if on_market_date_str:
        on_market_date_str = datetime.strptime(on_market_date_str, '%Y-%m-%d').date()
    else:
        on_market_date_str = None

    off_market_date_str = data.get('off_market_date', '')  # Fallback to now if not present
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
            orig_price_value = data['original_listing_price'] if data['original_listing_price'] is not None else ""
            original_listing_price = st.text_input("Original Listing Price", value=orig_price_value)

        # sold price
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
        with col2:
            sold_price_value = data['sold_price'] if data['sold_price'] is not None else ""
            sold_price = st.text_input("Sold Price", value=sold_price_value)

        # type of property
        type = st.selectbox("Type", type_list, index=default_type_index)

        # property characteristics
        sqft_value = data['sqft'] if data['sqft'] is not None else ""
        sqft = st.text_input("Square Feet", value=sqft_value).strip()
        bedroom_value = data['bedrooms'] if data['bedrooms'] is not None else ""
        bedrooms = st.text_input("Bedrooms", value=bedroom_value).strip()
        bathroom_value = data['bathrooms'] if data['bathrooms'] is not None else ""
        bathrooms = st.text_input("Bathrooms", value=bathroom_value).strip()
        year_value = data['year_built'] if data['year_built'] is not None else ""
        year_built = st.text_input("Year Built", value=year_value).strip()

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
            if action == "Update":
                # format keys from original data
                data = {
                    "property_id": data["property_id"]
                }

            # items from data input
            data["address_line_1"] = address_line_1
            data["address_line_2"] = address_line_2
            data["city"] = city
            data["state"] = state
            data["zip"] = zip
            data["original_listing_price"] = original_listing_price
            data["sold_price"] = sold_price
            data["type"] = type
            data["sqft"] = sqft
            data["bedrooms"] = bedrooms
            data["bathrooms"] = bathrooms
            data["year_built"] = year_built
            data["on_market"] = on_market
            data["off_market"] = off_market
            data["agent_name"] = agent_name
            data["sold"] = sold

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
                    report_action = "added"
                else:
                    # call function to update record in database
                    success = update_property(data)
                    report_action = "updated"
                
                if success:
                    st.success(f"Property {report_action}.")
                else:
                    st.error("An error occurred while adding the property.")