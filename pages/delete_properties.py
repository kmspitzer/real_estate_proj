import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

agent_menu()
st.title("Delete Properties")

st.write(db_get_table("properties"))

with st.form("agent_form"):
    st.write("## Delete Existing Property")

    property_id = st.text_input("Property ID", max_chars=10).strip()
    # form submission button
    submitted = st.form_submit_button("Delete Property")

    data = {
                "property_id": property_id}
    
    # call the function to delete the record from the database
    success = delete_property(data)
    if success:
        st.success(f"Property deleted.")
    else:
        st.error("An error occurred while deleting the property.")
