import streamlit as st
from menu import property_menu
from pages.property_form import property_form



# display the appropriate sidebar nav
property_menu()
st.title("Real Estate Management System")

data = {
        "address_line_1": "",
        "address_line_2": "",
        "city": "",
        "state": "",
        "zip": "",
        "original_listing_price": "",
        "sold_price": "",
        "type": "",
        "sqft": "",
        "bedrooms": "",
        "bathrooms": "",
        "year_built": "",
        "on_market": "",
        "off_market": "",
        "agent_name": "",
        "sold": False
}

property_form("Add", data)