import streamlit as st
from utilities.db_utils import *
from utilities.real_estate_utils import *

def choose_agent():
    apply_custom_css()

    # get agents for display on screen
    st.write(db_get_agent_display().to_html(index=False), unsafe_allow_html=True)

    # display form
    with st.form("agent_view_form"):
        st.write("## View/Edit Agent")

        # accept record id input
        record_id = st.text_input("Record ID", max_chars=50).strip()

        # display submit button and wait on click
        view_submitted = st.form_submit_button("View Agent Details")

        if view_submitted:
            # submit button clicked -- initialize validated flag
            validated = True

            if not record_id.isdigit():
                st.error("Record ID must be numeric.")
                validated = False

            if validated:
                # record id was valid -- get the agent requested
                agent = db_get_agent_by_id(int(record_id))

                # populate data object for next form
                if not agent.empty:
                    data = {
                        "agent_id": agent["agent_id"].iloc[0],
                        "first_name": agent["First Name"].iloc[0],
                        "last_name": agent["Last Name"].iloc[0],
                        "address_line_1": agent["Address Line 1"].iloc[0],
                        "address_line_2": agent["Address Line 2"].iloc[0],
                        "city": agent["City"].iloc[0],
                        "state": agent["State"].iloc[0],
                        "zip": agent["ZIP"].iloc[0],
                        "phone": agent["Phone"].iloc[0],
                        "start_date": agent["Start Date"].iloc[0]
                    }

                    return data
                else:
                    # record id entered was not found
                    st.error("Please enter a valid Record ID.")