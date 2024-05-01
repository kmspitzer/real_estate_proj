import streamlit as st
from menu import appointment_menu
from utilities.db_utils import *

appointment_menu()
st.title("Real Estate Managment System")

# button to reset the view and select another agent
if st.button('Refresh Appointments'):
    st.session_state['appt_data'] = None
    st.session_state['delete_appt'] = False

appt = db_get_appointment_display()
appt["Appt ID"] =  range(1, len(appt) + 1)

if pd.api.types.is_timedelta64_dtype(appt['Tour Time']):
    # Convert Timedelta to time (HH:MM:SS) by adding it to a minimal datetime
    appt['Tour Time'] = appt["Tour Time"].dt.components.apply(lambda x: f"{x.hours:02}:{x.minutes:02}", axis=1)

    disp_appts = appt.copy()
    disp_appts = disp_appts[['Appt ID', "Agent Name", "Client Name", "Property Address", "Tour Date", "Tour Time", "Outcome"]]
    # get agents for display on screen
    st.write(disp_appts.to_html(index=False), unsafe_allow_html=True)

with st.form("delete_appt_form"):
    st.write("## Delete Appointments")

    # accept record id input
    record_id = st.text_input("Appt ID", max_chars=50).strip()
    # form submission button

    submitted = st.form_submit_button("Delete Appointment")

    if submitted:
        # submit button clicked -- initialize validated flag
        validated = True

        if not record_id.isdigit():
            st.error("Appt ID must be numeric.")
            validated = False
        elif int(record_id) > len(appt):
            st.error("Appt ID does not exist.")
            validated = False

        if validated:
            # get the record associated with our temporary id
            target_appt = appt[appt["Appt ID"] == int(record_id)]

            data = {
                    'agent_id': target_appt['agent_id'].iloc[0],
                    'client_id': target_appt['client_id'].iloc[0],
                    'property_id': target_appt['property_id'].iloc[0],
                    'tour_datetime': target_appt['tour_datetime'].iloc[0]
            }

            # call the function to delete the record from the database
            success = delete_appointment(data)
            if success:
                st.success(f"Appointment deleted.")
            else:
                st.error("Appt ID does not exist.")