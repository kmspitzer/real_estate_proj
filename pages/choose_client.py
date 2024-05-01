import streamlit as st
from utilities.db_utils import *
from utilities.real_estate_utils import *

def choose_client():

    # apply CSS for table display
    apply_custom_css()

    # get agents for display on screen
    st.write(db_get_client_display().to_html(index=False), unsafe_allow_html=True)

    # display form
    with st.form("client_view_form"):
        st.write("## View/Edit Client")

        # accept client id input
        record_id = st.text_input("Client ID", max_chars=50).strip()

        # display submit button and wait on click
        view_submitted = st.form_submit_button("View Client Details")

        if view_submitted:
            # submit button clicked -- initialize validated flag
            validated = True

            # perform any edits on client id
            if not record_id.isdigit():
                st.error("Client ID must be numeric.")
                validated = False

            if validated:
                # record id was valid -- get the client requested
                client = db_get_client_by_id(int(record_id))

                # populate data object for next form
                if not client.empty:
                    data = {
                        "client_id": client["client_id"].iloc[0],
                        "first_name": client["First Name"].iloc[0],
                        "last_name": client["Last Name"].iloc[0],
                        "budget": client["Budget"].iloc[0],
                        "preferred_move_date":client["Preferred Move Date"].iloc[0],
                        "address_line_1": client["Address Line 1"].iloc[0],
                        "address_line_2": client["Address Line 2"].iloc[0],
                        "city": client["City"].iloc[0],
                        "state": client["State"].iloc[0],
                        "zip": client["ZIP"].iloc[0],
                        "phone": client["Phone"].iloc[0],
                        "status": client["Status"].iloc[0],
                        "sold": client["Sold"].iloc[0],
                        "agent_name": client['Agent Name'].iloc[0]
                    }

                    return data
                else:
                    # record id entered was not found
                    st.error("Please enter a valid Record ID.")