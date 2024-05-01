<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">REAL_ESTATE_PROJ</h1>
</p>
<p align="center">
    <em>Unlock properties, simplify real estate interactions!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/kmspitzer/real_estate_proj?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/kmspitzer/real_estate_proj?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/kmspitzer/real_estate_proj?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
</details>
<hr>

##  Overview

The real_estate_proj project is a comprehensive real estate management application that streamlines operations for agents, clients, properties, and appointments. Through intuitive menus and forms, users can efficiently add, view, edit, and delete data, ensuring a seamless user experience. By offering dropdown options for data entry and interactive functionality, the project enhances user interaction and database integrity. This project's core functionalities focus on simplifying real estate tasks and promoting efficient management within the Real Estate Management System.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | *The project follows a modular architecture that facilitates easy navigation and interaction with various real estate management functionalities. It uses Streamlit for the user interface and SQLAlchemy for database interactions.* |
| 🔩 | **Code Quality**  | *The codebase maintains a good level of quality and style, with clear structure and commenting. It follows best practices in Python development.* |
| 📄 | **Documentation** | *The project contains extensive documentation to help users understand the codebase, including explanations of modules, functions, and usage examples.* |
| 🔌 | **Integrations**  | *Key integrations include Streamlit for the UI, MySQL as the database backend, and SQLAlchemy for ORM operations.* |
| 🧩 | **Modularity**    | *The codebase is structured in a modular way, making it easy to add new features and functionalities. Each module handles specific tasks, enhancing code reusability.* |
| ⚡️  | **Performance**   | *Efficiency and speed are ensured through optimized database interactions and Streamlit UI implementation.* |
| 📦 | **Dependencies**  | *Key external libraries and dependencies include Streamlit, MySQLClient, SQLAlchemy, and pandas for handling data and user interface components.* |

---

##  Repository Structure

```sh
└── real_estate_proj/
    ├── README.md
    ├── app.py
    ├── config
    │   └── re_config.py
    ├── menu.py
    ├── pages
    │   ├── add_agent.py
    │   ├── add_appointment.py
    │   ├── add_client.py
    │   ├── add_property.py
    │   ├── agent_form.py
    │   ├── agent_options.py
    │   ├── appointment_form.py
    │   ├── appointment_options.py
    │   ├── choose_agent.py
    │   ├── choose_appointment.py
    │   ├── choose_client.py
    │   ├── choose_property.py
    │   ├── client_form.py
    │   ├── client_options.py
    │   ├── delete_agents.py
    │   ├── delete_appointments.py
    │   ├── delete_clients.py
    │   ├── delete_properties.py
    │   ├── get_players.py
    │   ├── get_properties.py
    │   ├── property_form.py
    │   ├── property_options.py
    │   ├── show_properties.py
    │   ├── standardize_phone.py
    │   ├── validate_agent.py
    │   ├── validate_appointment.py
    │   ├── validate_client.py
    │   ├── validate_property.py
    │   ├── view_edit_agents.py
    │   ├── view_edit_appointments.py
    │   ├── view_edit_clients.py
    │   └── view_edit_properties.py
    ├── requirements.txt
    ├── sql
    │   └── real_estate_proj.sql
    └── utilities
        ├── db_utils.py
        └── real_estate_utils.py
```

---

##  Modules


| File                                                                                           | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                   |
| [requirements.txt](https://github.com/kmspitzer/real_estate_proj/blob/master/requirements.txt) | Facilitates real estate management app content navigation via a user-friendly menu. Key features include adding/editing agents, clients, appointments, and properties. Enhances user experience by simplifying interaction with the apps various functionalities.                                     |
| [menu.py](https://github.com/kmspitzer/real_estate_proj/blob/master/menu.py)                   | Defines navigation menus based on user roles for managing agents, clients, properties, and appointments. Ensures appropriate menu options are displayed for each role type, enhancing user experience and access to relevant functionalities within the real estate application.                      |
| [app.py](https://github.com/kmspitzer/real_estate_proj/blob/master/app.py)                     | Defines system entry point and role selection UI handling for Real Estate Management System. Initializes roles, prompts user role selection, saves selected role to state, and displays corresponding menu upon confirmation. Enhances user experience with informative messages and role validation. |


| File                                                                                          | Summary                                                                                                                                                                                                |
| ---                                                                                           | ---                                                                                                                                                                                                    |
| [re_config.py](https://github.com/kmspitzer/real_estate_proj/blob/master/config/re_config.py) | Defines lists for dropdown options in the real estate web app, such as states, property types, and client statuses. Enhances user interface by providing pre-defined selection choices for data entry. |



| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [real_estate_utils.py](https://github.com/kmspitzer/real_estate_proj/blob/master/utilities/real_estate_utils.py) | Improve streamlit layout with custom CSS rules for better alignment and presentation of content in the real_estate_projs app interface.                                                                                                                                                                                                                                                                                                                                                                 |
| [db_utils.py](https://github.com/kmspitzer/real_estate_proj/blob/master/utilities/db_utils.py)                   | The `app.py` file in the `real_estate_proj` repository serves as the main entry point for a real estate project management application. It orchestrates interactions between different modules to facilitate tasks such as adding agents, clients, properties, and appointments. By leveraging the repositorys architecture, the `app.py` file provides a cohesive user experience by coordinating various functionalities and streamlining processes within the real estate project management system. |


| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                   |
| [get_players.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/get_players.py)                       | Retrieves player data by creating concatenated names for display and mapping player IDs to names, aiding in user interactions with agent/client data in the Real Estate Project.                                                                                                                                      |
| [add_property.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_property.py)                     | Displays property menu and system title. Initializes data object for a new property. Renders property form for adding data.                                                                                                                                                                                           |
| [client_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/client_form.py)                       | Facilitates client data input and editing. Validates input, handles form submission, and updates the database. Displays a form to collect client details like name, location, budget, and agent association.                                                                                                          |
| [show_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/show_properties.py)               | Displays properties in the real estate system for clients. Authenticates user access and applies custom styling. Retrieves property data from the database and presents it on the screen.                                                                                                                             |
| [appointment_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/appointment_options.py)       | Displays appointment options in the Real Estate Management System, leveraging Streamlit for UI. Integrates appointment menu and database utilities for a streamlined user experience within the parent repositorys architecture.                                                                                      |
| [appointment_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/appointment_form.py)             | Enables dynamic appointment creation/update with user inputs for agent, client, property, date, time, and outcome. Validates data and performs DB operations accordingly, providing success/error messages. Supports real estate project workflow seamlessly.                                                         |
| [standardize_phone.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/standardize_phone.py)           | Standardizes phone numbers to a specific format for database consistency. Extracts digits from input, formats as (XXX) XXX-XXXX if length is correct, else raises error.                                                                                                                                              |
| [get_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/get_properties.py)                 | Retrieves and transforms property data into a list of concatenated addresses. Builds a mapping dictionary for property IDs and addresses, aiding in the visualization and identification of properties within the real estate project.                                                                                |
| [view_edit_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_properties.py)     | Manages property views and edits in the real estate system via a streamlined interface. Enables selecting, updating, and refreshing property data with ease.                                                                                                                                                          |
| [agent_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/agent_options.py)                   | Displays agent hub in real estate management app, featuring agent menu with Streamlit integration. Impressive UI showcases agents in the system.                                                                                                                                                                      |
| [delete_agents.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_agents.py)                   | Implements agent deletion interface, showcasing agents and enabling deletion by ID validation. Displays agents, validates input for numeric ID, and deletes record from the database if it exists. Allows user to refresh agents view and select another agent.                                                       |
| [view_edit_clients.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_clients.py)           | Enables viewing and editing clients in the Real Estate Management System. Presents a client sidebar, allows refreshing clients, selecting a client for editing, and displaying the client form for updates. Integrates with session state variables for seamless interaction.                                         |
| [choose_appointment.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/choose_appointment.py)         | Enhances interface by displaying and enabling editing of appointment data. Validates input, fetches specific appointment details, and prepares data for the next form. Resides in the pages module, contributing to the real estate project's interactive functionality.                                              |
| [view_edit_agents.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_agents.py)             | Manages agent data selection and updates. Displays agent sidebar, system title, and form for updating selected agent details. Allows refreshing agent list and selection. Central to Real Estate Management Systems user interaction for agent management.                                                            |
| [agent_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/agent_form.py)                         | Handles agent data input with validation, standardization, and database interaction. Displays a form for adding or editing agent details. Validates input, formats phone numbers, and performs database operations based on the action specified (Add or Update). Displays success or error messages accordingly.     |
| [property_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/property_form.py)                   | Enables property form submission, validation, and updates with agents association. Renders form inputs for property details, pricing, dates, and agent selection. Handles error messages and database transactions for both adding and updating property records.                                                     |
| [choose_property.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/choose_property.py)               | Displays and validates property records for viewing/editing. Retrieves data from the database, populates form fields, and handles error messages elegantly. Supports user interaction with a submit button, ensuring data integrity and providing a seamless user experience.                                         |
| [validate_appointment.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_appointment.py)     | Validates appointment data fields for required information, checking tour date, time, agent and client names, and property address. Sets outcome to None if blank. Ensures data integrity for database handling.                                                                                                      |
| [validate_property.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_property.py)           | Validates property data for real estate listings, ensuring essential fields are populated correctly and in the right format. Handles special cases like pricing and numeric property characteristics for database integrity. A crucial step in maintaining data accuracy and consistency in the real estate platform. |
| [validate_agent.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_agent.py)                 | Validates agent data ensuring completeness and accuracy for required fields such as first name, last name, address, city, state, zip code, and phone number in the real estate project.                                                                                                                               |
| [client_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/client_options.py)                 | Implements client menu interface in real estate app. Renders client hub with Streamlit, access to Real Estate Management System.                                                                                                                                                                                      |
| [add_appointment.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_appointment.py)               | Enables adding appointments to the real estate system via a user-friendly form. Displays the system title and relevant sidebar navigation before facilitating data entry for agent, client, property, and appointment details like tour date and time.                                                                |
| [add_client.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_client.py)                         | Enables adding new clients in the Real Estate Management System via a streamlined form interface. Presents client menu, system title, and pre-populated client data fields for input. Integrated with database utilities for seamless data handling.                                                                  |
| [delete_clients.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_clients.py)                 | Enables users to delete clients in the Real Estate Management System. Displays client data, allows refreshing client view, and provides a form to input and delete client records. Validates input for client ID and informs users of successful deletion or non-existent record.                                     |
| [validate_client.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_client.py)               | Validating client data for completeness and accuracy by checking required fields, handling special cases like budget, and ensuring proper formatting for fields like ZIP code and phone number. Critical for maintaining data integrity and usability in the real estate project.                                     |
| [view_edit_appointments.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_appointments.py) | Enables viewing and editing appointments in a real estate management system. Handles appointment selection, display, and updating via session state handling. Integrates appointment form functionality for seamless user interaction.                                                                                |
| [choose_agent.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/choose_agent.py)                     | Displays and validates agent details; retrieves info based on ID provided. Presented data object for future form. Highlights errors if ID not numeric or record not found.                                                                                                                                            |
| [delete_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_properties.py)           | Displays and deletes properties from the Real Estate Management System. Allows refreshing property view, entering a property ID to delete, and validating input before removing the property record from the database.                                                                                                |
| [add_agent.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_agent.py)                           | Implements a form to add new agents in the Real Estate Management System. Renders the sidebar navigation and system title, initializes data for a new agent, and displays the agent form for adding details like name, address, and contact information.                                                              |
| [property_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/property_options.py)             | Implements the properties hub interface in the real_estate_proj repository. Displays a menu, project title, and information about properties, enhancing the Real Estate Management Systems user experience.                                                                                                           |
| [choose_client.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/choose_client.py)                   | Renders a form to view and edit client details from database. Validates client ID, retrieves client data, and populates form for editing. Ensures data integrity and user-friendly management of real estate client information.                                                                                      |
| [delete_appointments.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_appointments.py)       | Displays and allows deletion of appointments in the Real Estate Management System. Validates and deletes appointments from the database based on user input. Maintains appointment details, such as agent, client, property, tour date, time, and outcome.                                                            |


| File                                                                                                       | Summary                                                                                                                                                                                                       |
| ---                                                                                                        | ---                                                                                                                                                                                                           |
| [real_estate_proj.sql](https://github.com/kmspitzer/real_estate_proj/blob/master/sql/real_estate_proj.sql) | Defines tables for agents, properties, clients, and appointments with specific attributes. Maintains referential integrity between these entities, supporting the real estate projects backend functionality. |


---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.7.x and above`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the real_estate_proj repository:
>
> ```console
> $ git clone https://github.com/kmspitzer/real_estate_proj
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd real_estate_proj
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run real_estate_proj in streamlit application using the command below:
> ```console
> $ streamlit run app.py
> ```