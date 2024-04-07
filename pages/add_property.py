import streamlit as st
from menu import property_menu
from pages.get_agents import get_agents
from utilities.db_utils import *

from config.re_config import state_list


######################
## ADD NEW PROPERTY ##
######################

# get agent names for association
agent_names, agent_mapping = get_agents()

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
        # initialize a flag to track validation status
        validation_successful = True

        # check each field separately
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

        # handle original_listing_price as a special case because it can be None
        if original_listing_price == "":
            original_listing_price_value = None
        else:
            try:
                # remove commas for database
                original_listing_price_value = int(original_listing_price.replace(",", "").strip())
            except ValueError:
                st.error("Please enter a valid number for the Original Listing Price.")
                validation_successful = False

        # handle sold price as a special case because it can be None
        if sold_price == "":
            sold_price_value = None
        else:
            try:
                # remove commas for database
                sold_price_value = int(sold_price.replace(",", "").strip())
            except ValueError:
                st.error("Please enter a valid number for Sold Price.")
                validation_successful = False

        if not type:
            st.error('Property Type is required.')
            validation_successful = False

        # if populated, characteristics must be numeric
        sqft_value = sqft
        if  sqft_value == '':
            sqft_value = None
        elif not sqft_value.isdigit():
            st.error('Square Feet must be numeric.')
            validation_successful = False

        bedrooms_value = bedrooms
        if bedrooms_value == '':
            bedrooms_value = None
        elif not bedrooms_value.isdigit():
            st.error('Number of Bedrooms must be numeric.')
            validation_successful = False

        bathrooms_value = bathrooms
        if bathrooms_value == '':
            bathrooms_value = None
        elif not bathrooms_value.isdigit():
            st.error('Number of Bathrooms must be numeric.')
            validation_successful = False

        year_built = year_built
        if len(year_built) != 4 or not year_built.isdigit():
            st.error('Year Built must be 4 digits.')
            validation_successful = False

        if not agent_name:
            st.error('Agent Name is required.')
            validation_successful = False

        # if all fields are valid, proceed to process the form
        if validation_successful:
            # get the agent_id from our mapping
            agent_id = agent_mapping.get(agent_name)

            # collect the data into a tuple
            data = (address_line_1, address_line_2, city, state, zip,
                    original_listing_price_value, sold_price_value, type, sqft_value, bedrooms_value,
                    bathrooms_value, year_built, on_market, off_market, agent_id, sold
            )

            # call the function to insert the record into the database
            property_id = insert_property(data)
            if property_id:
                st.success(f"Property added with ID: {property_id}")
            else:
                st.error("An error occurred while adding the property.")