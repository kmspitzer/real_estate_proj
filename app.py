import streamlit as st

from agent_funcs import show_agents_page

def show_properties_page():
    st.header("Properties")
    # Add content for the properties page here

def show_clients_page():
    st.header("Clients")
    # Add content for the clients page here

def show_appointments_page():
    st.header("Appointments")
    # Add content for the appointments page here

# Main function to display the landing page and handle navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ('Home', 'Agents', 'Properties', 'Clients', 'Appointments'))

    if page == 'Home':
        st.title("Real Estate Management System")
        st.write("Please select a page from the sidebar to begin.")
    elif page == 'Agents':
        show_agents_page()
    elif page == 'Properties':
        show_properties_page()
    elif page == 'Clients':
        show_clients_page()
    elif page == 'Appointments':
        show_appointments_page()

if __name__ == "__main__":
    main()