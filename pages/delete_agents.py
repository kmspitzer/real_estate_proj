import streamlit as st
from menu import agent_menu
from utilities.db_utils import *
from utilities.real_estate_utils import *


# display agent sidebar
agent_menu()
st.title("Real Estate Managment System")

# apply CSS for table display
apply_custom_css()

# button to reset the view and select another agent
if st.button('Refresh Agents'):
    st.session_state['agent_data'] = None
    st.session_state['delete_agent'] = False

# get agents for display on screen
st.write(db_get_agent_display().to_html(index=False), unsafe_allow_html=True)

# display form
with st.form("delete_agent_form"):
    st.write("## Delete Agent")

    # accept record id input
    record_id = st.text_input("Agent ID", max_chars=50).strip()

    # form submission button
    submitted = st.form_submit_button("Delete Agent")

    if submitted:
        # submit button clicked -- initialize validated flag
        validated = True

        # perform any edits on 
        if not record_id.isdigit():
            st.error("Agent ID must be numeric.")
            validated = False

        if validated:
            # call the function to delete the record from the database
            success = delete_agent({'agent_id': record_id})
            if success:
                st.success(f"Agent deleted.")
            else:
                st.error("Agent ID does not exist.")