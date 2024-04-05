import streamlit as st

from show_agents_page import show_agents_page
from show_properties_page import show_properties_page
from show_clients_page import show_clients_page
from show_appointments_page import show_appointments_page

def main():
    st.title('Real Estate Management System')

    # Dropdown menu for selecting data type
    data_type = st.selectbox(
        'Choose the data you want to interact with:',
        ('', 'Agents', 'Properties', 'Clients', 'Appointments')
    )

    # Submit button for the selection
    submit = st.button('Go')

     # Check if the user has made a selection and clicked 'Go'
    if submit and data_type:
        # Use the selection to determine the navigation
        if data_type == 'Agents':
            show_agents_page()
        elif data_type == 'Properties':
            show_properties_page()
        elif data_type == 'Clients':
            show_clients_page()
        elif data_type == 'Appointments':
            show_appointments_page()
        # Add additional conditions for other data types as needed
    elif submit and not data_type:
        # User clicked 'Go' without making a selection
        st.error("Please select a data type to proceed.")

if __name__ == "__main__":
    main()