import streamlit as st
from menu import property_menu
from pages.get_players import get_players
from pages.validate_property import validate_property
from utilities.db_utils import *

from config.re_config import state_list


######################
## ADD NEW PROPERTY ##
######################

# get agent names for association
agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')

# display the appropriate sidebar nav
property_menu()

# display form and collect data
with st.form("property_form"):
    st.write("## Add New Property")

    # address with state dropdown
    address_line_1 = st.text_input("Address Line 1", max_chars=90).strip()
    address_line_2 = st.text_input("Address Line 2", max_chars=50).strip()
    city = st.text_input("City", max_chars=30).strip()
    state = st.selectbox("State", state_list)
    zip = st.text_input("ZIP", max_chars=5).strip()

    # original listing price
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
    with col2:
        original_listing_price = st.text_input("Original Listing Price", value="")

    # sold price
    col1, col2 = st.columns([1, 20])
    with col1:
        st.markdown("&#36;", unsafe_allow_html=True)  # HTML code for dollar sign
    with col2:
        sold_price = st.text_input("Sold Price", value="")

    # type of property
    type = st.selectbox("Type", ['', 'Single Family Home', 'Commercial', 'Land', 'Multi Family Home', 'Apartment', 'Townhouse', 'Condo'])

    # property characteristics
    sqft = st.text_input("Square Feet").strip()
    bedrooms = st.text_input("Bedrooms").strip()
    bathrooms = st.text_input("Bathrooms").strip()
    year_built = st.text_input("Year Built").strip()

    # on/off market dates
    on_market = st.date_input("On Market Date", value=None)
    off_market = st.date_input("Off Market Date", value=None)

    # choose agent
    agent_name = st.selectbox("Agent Name", options=[''] + agent_names)

    # spld checkbox
    sold = st.checkbox("Sold")

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

            # call function to insert the record into the database
            success = insert_property(data)
            
            if success:
                st.success(f"Property added.")
            else:
                st.error("An error occurred while adding the property.")