import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

agent_menu()
st.title("Delete Clients")

st.write(db_get_table("clients"))

with st.form("agent_form"):
    st.write("## Delete Existing Client")

    client_id = st.text_input("Client ID", max_chars=10).strip()
    # form submission button
    submitted = st.form_submit_button("Delete Client")

    data = {
                "client_id": client_id}
    
    # call the function to delete the record from the database
    success = delete_client(data)
    if success:
        st.success(f"Client deleted.")
    else:
        st.error("An error occurred while deleting the client.")
