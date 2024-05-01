from datetime import datetime
import streamlit as st
from utilities.db_utils import *
from utilities.real_estate_utils import *

def choose_appointment():
    apply_custom_css()

    appt = db_get_appointment_display()
    appt["Appt ID"] =  range(1, len(appt) + 1)

    if pd.api.types.is_timedelta64_dtype(appt['Tour Time']):
        # Convert Timedelta to time (HH:MM:SS) by adding it to a minimal datetime
        appt['Tour Time'] = appt["Tour Time"].dt.components.apply(lambda x: f"{x.hours:02}:{x.minutes:02}", axis=1)

    disp_appts = appt.copy()
    disp_appts = disp_appts[['Appt ID', "Agent Name", "Client Name", "Property Address", "Tour Date", "Tour Time", "Outcome"]]
    # get agents for display on screen
    st.write(disp_appts.to_html(index=False), unsafe_allow_html=True)

    # display form
    with st.form("appt_view_form"):
        st.write("## View/Edit Appointments")

        # accept record id input
        record_id = st.text_input("Appt ID", max_chars=50).strip()

        # display submit button and wait on click
        submitted = st.form_submit_button("View Appointment Details")

        if submitted:
            # submit button clicked -- initialize validated flag
            validated = True

            if not record_id.isdigit():
                st.error("Appt ID must be numeric.")
                validated = False

            if int(record_id) > len(appt):
                st.error("Appt ID does not exist.")
                validated = False

            if validated:
                # get the record associated with our temporary id
                target_appt = appt[appt["Appt ID"] == int(record_id)]

                # record id was valid -- get the agent requested
                appointment = db_get_appointment_by_id(target_appt['agent_id'].iloc[0], target_appt['client_id'].iloc[0],
                                                       target_appt['property_id'].iloc[0], target_appt['tour_datetime'].iloc[0])
                appointment["Tour Time"] = appointment["Tour Time"].dt.components.apply(lambda x: f"{x.hours:02}:{x.minutes:02}", axis=1)

                # populate data object for next form
                if not appointment.empty:
                    data = {
                        "agent_name": appointment['Agent Name'].iloc[0],
                        "client_name": appointment['Client Name'].iloc[0],
                        "property_address": appointment['Property Address'].iloc[0],
                        "tour_date": appointment['Tour Date'].iloc[0],
                        "tour_time": appointment['Tour Time'].iloc[0],
                        "outcome": appointment["Outcome"].iloc[0]
                    }

                    return data
                else:
                    # record id entered was not found
                    st.error("Please enter a valid Record ID.")