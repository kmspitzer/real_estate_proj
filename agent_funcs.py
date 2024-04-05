import streamlit as st
import json

from db_utils import db_get_table


def show_agents_page():
    st.title("Agents")

    agents = json.loads(db_get_table('agents'))

    # Display each agent with options
    for agent in agents:
        modify_key = f"modify_{agent['agent_id']}"  # Unique key for the Modify button
        delete_key = f"delete_{agent['agent_id']}"  # Unique key for the Delete button
        
        cols = st.columns([2, 2, 2, 1, 1])
        cols[0].write(agent['first_name'])
        cols[1].write(agent['last_name'])
        if cols[3].button("Modify", key=modify_key):
            # Handle modification logic
            pass
        if cols[4].button("Delete", key=delete_key):
            # Handle deletion logic
            pass

    # Button to add a new agent, correctly using a unique key
    if st.button("Add New Agent", key="add_new_agent"):
        pass  # Here, you would display a form for adding a new agent or navigate to an add agent page