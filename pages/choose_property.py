import streamlit as st
from utilities.db_utils import *
from utilities.real_estate_utils import *

def choose_property():
    apply_custom_css()

    prop_df = db_get_properties_display()
    prop_df = prop_df.fillna('')

    # get agents for display on screen
    st.write(prop_df.to_html(index=False), unsafe_allow_html=True)

    # display form
    with st.form("property_view_form"):
        st.write("## View/Edit Properties")

        # accept record id input
        record_id = st.text_input("Property ID", max_chars=50).strip()

        # display submit button and wait on click
        view_submitted = st.form_submit_button("View Property Details")

        if view_submitted:
            # submit button clicked -- initialize validated flag
            validated = True

            if not record_id.isdigit():
                st.error("Property ID must be numeric.")
                validated = False

            if validated:
                # record id was valid -- get the agent requested
                property = db_get_properties_by_id(int(record_id))

                # populate data object for next form
                if not property.empty:
                    data = {
                        "property_id": property["property_id"].iloc[0],
                        "address_line_1": property["Address Line 1"].iloc[0],
                        "address_line_2": property["Address Line 2"].iloc[0],
                        "city": property["City"].iloc[0],
                        "state": property["State"].iloc[0],
                        "zip": property["ZIP"].iloc[0],
                        "original_listing_price": property["Original Listing Price"].iloc[0],
                        "sold_price": property["Sold Price"].iloc[0],
                        "type": property["Type"].iloc[0],
                        "sqft": property["Square Feet"].iloc[0],
                        "bedrooms": property["Bedrooms"].iloc[0],
                        "bathrooms": property["Bathrooms"].iloc[0],
                        "year_built": property["Year Built"].iloc[0],
                        "on_market": property["On Market"].iloc[0],
                        "off_market": property["Off Market"].iloc[0],
                        "agent_name": property["Agent Name"].iloc[0],
                        "sold": property["Sold"].iloc[0]
                    }

                    return data
                else:
                    # record id entered was not found
                    st.error("Please enter a valid Record ID.")