import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

try:
    agent_menu()
    st.title("Delete Appointments")

    st.write(db_get_table("appointments"))

    with st.form("agent_form"):
        st.write("## Delete Existing Appointment")

        agent_id = st.text_input("Agent ID", max_chars=10).strip()
        client_id = st.text_input("Client ID", max_chars=10).strip()
        property_id = st.text_input("Property ID", max_chars=10).strip()
        tour_datetime = st.text_input("Tour Datetime", max_chars=19).strip()
        # form submission button
        submitted = st.form_submit_button("Delete Appointment")

        data = {
                    "agent_id": agent_id,
                    "client_id": client_id,
                    "property_id": property_id,
                    "tour_datetime": tour_datetime}
        
        # call the function to delete the record from the database
        success = delete_appointment(data)
        if success:
            st.success(f"Appointment deleted.")
        else:
            st.error("An error occurred while deleting the appointment.")

except Exception:
    print("Please enter values in the text boxes.")
