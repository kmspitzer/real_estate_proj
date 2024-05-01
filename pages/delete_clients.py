import streamlit as st
from menu import client_menu
from utilities.db_utils import *

client_menu()
st.title("Real Estate Managment System")

# button to reset the view and select another agent
if st.button('Refresh Clients'):
    st.session_state['client_data'] = None
    st.session_state['delete_client'] = False

# get agents for display on screen
st.write(db_get_client_display().to_html(index=False), unsafe_allow_html=True)

# displacy form
with st.form("delet_client_form"):
    st.write("## Delete Client")

    # accept record id input
    record_id = st.text_input("Client ID", max_chars=50).strip()

    # form submission button
    submitted = st.form_submit_button("Delete Client")

    if submitted:
        # submit button clicked -- initialize validated flag
        validated = True

        # perform any edits on client id
        if not record_id.isdigit():
            st.error("Client ID must be numeric.")
            validated = False

        if validated:
            # call the function to delete the record from the database
            success = delete_client({'client_id': record_id})
            if success:
                st.success(f"Client deleted.")
            else:
                st.error("Record ID does not exist.")
