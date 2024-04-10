import streamlit as st

##############################
## SIDEBAR MENU DEFINITIONS ##
##############################
def authenticated_menu():
    # show a navigation menu for authenticated users based on role
    st.sidebar.page_link("app.py", label="Switch User Type")
    st.sidebar.write("")
    if st.session_state.role == "Agent Manager":
        st.sidebar.page_link("pages/agent_options.py", label='Manage Agents')
    elif st.session_state.role == "Client":
        st.sidebar.page_link("pages/show_properties.py", label="Property Listings")
    else: # role is Agent
        st.sidebar.page_link("pages/property_options.py", label="Manage Properties")
        st.sidebar.page_link("pages/client_options.py", label="Manage Clients")
        st.sidebar.page_link("pages/appointment_options.py",label="Manage Appointments")

def property_menu():
    if 'role' not in st.session_state:
        st.session_state.role = 'Agent'
    # show a navigation menu for users with access to property functions
    st.sidebar.page_link("app.py", label="Switch User Type")
    st.sidebar.write("")
    if st.session_state.role == "Agent Manager":
        st.sidebar.page_link("pages/agent_options.py", label='Manage Agents')
    elif st.session_state.role == "Client":
        st.sidebar.page_link("pages/show_properties.py", label="Property Listings")
    else: # role is Agent
        st.sidebar.page_link("pages/property_options.py", label="Manage Properties")
        st.sidebar.page_link("pages/add_property.py", label="-->> Add Property")
        st.sidebar.page_link("pages/view_edit_properties.py", label="-->> View/Edit Propeties")
        st.sidebar.page_link("pages/client_options.py", label="Manage Clients")
        st.sidebar.page_link("pages/appointment_options.py",label="Manage Appointments")

def agent_menu():
    if 'role' not in st.session_state:
        st.session_state.role = 'Agent Manager'
    # show a navigation menu for users with access to agent functions
    st.sidebar.page_link("app.py", label="Switch User Type")
    st.sidebar.write("")
    if st.session_state.role == "Agent Manager":
        st.sidebar.page_link("pages/agent_options.py", label='Manage Agents')
        st.sidebar.page_link("pages/add_agent.py", label="-->> Add Agent")
        st.sidebar.page_link("pages/view_edit_agents.py", label="-->> View/Edit Agents")
    elif st.session_state.role == "Client":
        st.sidebar.page_link("pages/show_properties.py", label="Property Listings")
    else: # role is Agent
        st.sidebar.page_link("pages/property_options.py", label="Manage Properties")
        st.sidebar.page_link("pages/client_options.py", label="Manage Clients")
        st.sidebar.page_link("pages/appointment_options.py",label="Manage Appointments")

def client_menu():
    if 'role' not in st.session_state:
        st.session_state.role = 'Agent'
    # show a navigation menu for users with access to client functions
    st.sidebar.page_link("app.py", label="Switch User Type")
    st.sidebar.write("")
    if st.session_state.role == "Agent Manager":
        st.sidebar.page_link("pages/agent_options.py", label='Manage Agents')
    elif st.session_state.role == "Client":
        st.sidebar.page_link("pages/show_properties.py", label="Property Listings")
    else: # role is Agent
        st.sidebar.page_link("pages/property_options.py", label="Manage Properties")
        st.sidebar.page_link("pages/client_options.py", label="Manage Clients")
        st.sidebar.page_link("pages/add_client.py", label="-->> Add Client")
        st.sidebar.page_link("pages/view_edit_clients.py", label="-->> View/Edit Clients")
        st.sidebar.page_link("pages/appointment_options.py",label="Manage Appointments")
    

def appointment_menu():
    if 'role' not in st.session_state:
        st.session_state.role = 'Agent'
    # show a navigation menu for users with access to appointment functions
    st.sidebar.page_link("app.py", label="Switch user type")
    st.sidebar.write("")
    if st.session_state.role == "Agent Manager":
        st.sidebar.page_link("pages/manage_agents.py", label='Manage Agents')
    elif st.session_state.role == "Client":
        st.sidebar.page_link("pages/show_properties.py", label="Property Listings")
    else: # role is Agent
        st.sidebar.page_link("pages/property_options.py", label="Manage Properties")
        st.sidebar.page_link("pages/client_options.py", label="Manage Clients")
        st.sidebar.page_link("pages/appointment_options.py",label="Manage Appointments")
        st.sidebar.page_link("pages/add_appointment.py", label="-->> Add Appointment")
        st.sidebar.page_link("pages/view_edit_appointments.py", label="-->> View/Edit Appointments")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()