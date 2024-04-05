from agent_funcs import show_agents_page
from show_properties_page import show_properties_page
from show_clients_page import show_clients_page
from show_appointments_page import show_appointments_page

def page_router(data_type):
    if data_type == 'Agents':
        show_agents_page()
    elif data_type == 'Properties':
        show_properties_page()
    elif data_type == 'Clients':
        show_clients_page()
    elif data_type == 'Appointments':
        show_appointments_page()