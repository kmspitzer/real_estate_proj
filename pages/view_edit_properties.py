import streamlit as st
from menu import property_menu
from utilities.db_utils import *
from config.re_config import state_list
from pages.get_players import get_players

try:
    agent_names, agent_mapping = get_players('agents', 'agent_id', 'agent_name')

    # place holder
    property_menu()
    st.title("View/Edit Properties")

    st.write(db_get_table("properties"))

    # display form and collect data
    with st.form("property_form"):
        st.write("## Update Existing Property")

        property_id = st.text_input("Property ID", max_chars=10).strip()
        agent_id = st.text_input("Agent ID", max_chars=10).strip()

        property = db_get_properties_by_id(property_id, agent_id)
        property.loc[property['Sold'] == "Yes", "Sold"] = 1
        property.loc[property['Sold'] == "No", "Sold"] = 0

        address_line_1 = st.text_input("Address Line 1", value=str(property['Address Line 1'].values[0]), max_chars=90).strip()
        address_line_2 = st.text_input("Address Line 2", value=str(property['Address Line 2'].values[0]), max_chars=50).strip()
        city = st.text_input("City", value=str(property['City'].values[0]), max_chars=30).strip()
        state = st.text_input("State", value=str(property['State'].values[0]))
        zip = st.text_input("ZIP", value=str(property['ZIP'].values[0]), max_chars=5).strip()

        original_listing_price = st.text_input("Original Listing Price", value=str(property['Original Listing Price'].values[0]))
        sold_price = st.text_input("Sold Price", value=str(property['Sold Price'].values[0]))

        # type of property
        type = st.text_input("Type", value=str(property['Type'].values[0]))

        # property characteristics
        sqft = st.text_input("Square Feet", value=str(property['Square Feet'].values[0])).strip()
        bedrooms = st.text_input("Bedrooms", value=str(property['Bedrooms'].values[0])).strip()
        bathrooms = st.text_input("Bathrooms", value=str(property['Bathrooms'].values[0])).strip()
        year_built = st.text_input("Year Built", value=str(property['Year Built'].values[0])).strip()

        # on/off market dates
        on_market = st.text_input("On Market Date", value=str(property['On Market'].values[0]))
        off_market = st.text_input("Off Market Date", value=str(property['Off Market'].values[0]))

        # sold checkbox
        sold = st.text_input("Sold", value=str(property['Sold'].values[0]))
            

        # form submission button
        submitted = st.form_submit_button("Submit Property")

        # when form is submitted, we edit
        if submitted:
            # initialize a flag to track validation status
            validation_successful = True

            # check each field separately

            # ensure property ID is an integer
            if not property_id.isdigit():
                st.error('A numeric property ID is required.')
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

            # if not agent_name:
            #     st.error('Agent Name is required.')
            #     validation_successful = False

            # if all fields are valid, proceed to process the form
            if validation_successful:
                # # get the agent_id from our mapping
                # agent_id = agent_mapping.get(agent_name)

                # collect the data into a dictionary
                data = {
                        "property_id": property_id,
                        "address_line_1": address_line_1,
                        "address_line_2": address_line_2,
                        "city": city,
                        "state": state,
                        "zip": zip,
                        "original_listing_price": original_listing_price_value,
                        "sold_price": sold_price_value,
                        "type": type,
                        "sqft": sqft_value,
                        "bedrooms": bedrooms_value,
                        "bathrooms": bathrooms_value,
                        "year_built": year_built,
                        "on_market": on_market,
                        "off_market": off_market,
                        "agent_id": agent_id,
                        "sold": sold
                }

                # call the function to insert the record into the database
                success = update_property(data)
                if success:
                    st.success(f"Property updated.")
                else:
                    st.error("An error occurred while updating the property.")
except AttributeError: 
    pass #Hide error that occurs when user hasn't inputted data yet