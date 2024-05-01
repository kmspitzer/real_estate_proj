from datetime import datetime
import streamlit as st
from utilities.db_utils import *
from utilities.real_estate_utils import *

def choose_appointment():

    # apply CSS for table display
    apply_custom_css()

    # retrieve all appointments and add a temporary record id
    appt = db_get_appointment_display()
    appt["Appt ID"] =  range(1, len(appt) + 1)

    # convert the time column from timedelta to time
    if pd.api.types.is_timedelta64_dtype(appt['Tour Time']):
        # Convert Timedelta to time (HH:MM:SS) by adding it to a minimal datetime
        appt['Tour Time'] = appt["Tour Time"].dt.components.apply(lambda x: f"{x.hours:02}:{x.minutes:02}", axis=1)

    # make a copy of the appointments, and keep only the columns for the screen table
    disp_appts = appt.copy()
    disp_appts = disp_appts[['Appt ID', "Agent Name", "Client Name", "Property Address", "Tour Date", "Tour Time", "Outcome"]]
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

            # perform any edits on appointment id
            if not record_id.isdigit():
                st.error("Appt ID must be numeric.")
                validated = False
            elif int(record_id) > len(appt):
                st.error("Appt ID does not exist.")
                validated = False

            if validated:
                # ID is valid --
                # get the record associated with our temporary id
                target_appt = appt[appt["Appt ID"] == int(record_id)]

                # populate data object for next form
                data = {
                    "agent_name": target_appt['Agent Name'].iloc[0],
                    "client_name": target_appt['Client Name'].iloc[0],
                    "property_address": target_appt['Property Address'].iloc[0],
                    "tour_date": target_appt['Tour Date'].iloc[0],
                    "tour_time": target_appt['Tour Time'].iloc[0],
                    "outcome": target_appt["Outcome"].iloc[0]
                }

                return data
