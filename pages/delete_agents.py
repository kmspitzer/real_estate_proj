import streamlit as st
from menu import agent_menu
from utilities.db_utils import *

agent_menu()
st.title("Delete Agents")

st.write(db_get_table("agents"))

with st.form("agent_form"):
    st.write("## Delete Existing Agent")

    agent_id = st.text_input("Agent ID", max_chars=10).strip()

    # form submission button
    submitted = st.form_submit_button("Delete Agent")

    data = {
                "agent_id": agent_id}

    # call the function to delete the record from the database
    success = delete_agent(data)
    if success:
        st.success(f"Agent deleted.")
    else:
        st.error("An error occurred while deleting the agent.")