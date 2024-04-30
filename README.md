<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">REAL_ESTATE_PROJ</h1>
</p>
<p align="center">
    <em>Unlock seamless real estate management effortlessly.</em>
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

The real_estate_proj software project enables streamlined real estate management through a user-friendly Streamlit app. It empowers users to efficiently add, view, and delete agents, clients, appointments, and properties with form validation and MySQL database connectivity. The project's core functionalities include dynamic menus based on user roles, standardized data input, and seamless navigation for an enhanced user experience. With a focus on data consistency and efficient transactions, real_estate_proj offers a valuable solution for managing real estate operations effectively.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a structured architecture design enabling real estate management UI through a Streamlit app. It utilizes SQLAlchemy for database connectivity with MySQL. The codebase is organized into distinct modules for easy navigation and maintenance. |
| 🔩 | **Code Quality**  | The codebase exhibits good quality and style with consistent coding practices. It demonstrates adherence to PEP 8 standards and follows a modular approach for better readability and maintainability. Comments and docstrings are used effectively to enhance code clarity. |
| 📄 | **Documentation** | The project includes well-documented code providing insights into functionality and usage. Detailed explanations are present for functions, files, and database interactions. |
| 🔌 | **Integrations**  | Key integrations include Streamlit for UI development and interaction, SQLAlchemy for database connectivity to MySQL, and python-dotenv for environment variable management. These integrations enhance the project's functionality and usability within the real estate domain. |
| 🧩 | **Modularity**    | The codebase demonstrates good modularity with clear separation of concerns. Modules such as menu, pages, and utilities handle specific functionalities, promoting code reusability and maintainability. |
| ⚡️  | **Performance**   | The project emphasizes user interaction efficiency through a streamlined UI and optimized database interactions. |
| 📦 | **Dependencies**  | Key dependencies include Streamlit for UI development, SQLAlchemy for database integration, and mysqlclient for MySQL database connectivity. These dependencies facilitate core functionalities of the real estate management application. |

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
        └── db_utils.py
```

---

##  Modules


| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                        |
| [requirements.txt](https://github.com/kmspitzer/real_estate_proj/blob/master/requirements.txt) | Enables real estate management UI through a Streamlit app. Facilitates adding, viewing, and deleting agents, clients, appointments, and properties. Implements form validation and database connectivity using SQLAlchemy and MySQL.                                                                                       |
| [menu.py](https://github.com/kmspitzer/real_estate_proj/blob/master/menu.py)                   | Defines navigation menus based on user roles in a real estate app. Ensures authenticated users access relevant features like managing agents, clients, properties, and appointments. Implements user redirection if not logged in. Encourages seamless user experience while navigating through different functionalities. |
| [app.py](https://github.com/kmspitzer/real_estate_proj/blob/master/app.py)                     | Defines entry point, sets user role, and renders dynamic menu for a real estate system. Allows users to select roles and navigate menu options. Facilitates smooth interaction within the system.                                                                                                                          |


| File                                                                                          | Summary                                                                                                                                        |
| ---                                                                                           | ---                                                                                                                                            |
| [re_config.py](https://github.com/kmspitzer/real_estate_proj/blob/master/config/re_config.py) | States, statuses, property types, and outcomes. Supports data consistency and selection options across the real estate projects UI components. |



| File                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                            | ---                                                                                                                                                                                                                                                                                                                                     |
| [db_utils.py](https://github.com/kmspitzer/real_estate_proj/blob/master/utilities/db_utils.py) | This `db_utils.py` file in the `real_estate_proj` repository serves as a key utility component for managing interactions with the projects database. It encapsulates functions and methods related to handling database operations efficiently across various parts of the application, ensuring smooth and reliable data transactions. |


| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                      |
| [get_players.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/get_players.py)                       | Retrieves player data from the database, concatenates first and last names, generates a list of names, and creates a mapping of player IDs to names. Enhances data retrieval functionality in the real estate project for improved user experience.                                                      |
| [add_property.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_property.py)                     | Enables adding property details through a streamlined form in the real_estate_proj web app. Facilitates input of address, pricing, type, agent, and other property specifics, enhancing user experience and efficiency.                                                                                  |
| [client_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/client_form.py)                       | Enables user interactions to add or edit client details with validation and database updates. Implements form inputs for client data like name, budget, address, phone, status, agent association, and validation checks. Displays success/error messages based on database operations.                  |
| [show_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/show_properties.py)               | Displays properties in client view within the real estate project. Retrieves and showcases property information from the database using Streamlit. Integrated within the menu for authenticated access.                                                                                                  |
| [appointment_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/appointment_options.py)       | Manages appointment operations through the appointment hub menu. Displays the Appointments title using Streamlit. Accesses functions from the appointment menu and database utilities for seamless navigation and data retrieval in the real estate project's Streamlit app.                             |
| [appointment_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/appointment_form.py)             | Enables creating or editing appointments by selecting agent, client, property, date, time, and outcome. Validates input, maps names to IDs, stores data in the database, and provides success or error messages.                                                                                         |
| [standardize_phone.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/standardize_phone.py)           | Standardizes phone numbers in the real estate project database by applying a uniform format. Parses input digits and formats them into a specified structure. Raises an error for invalid phone number lengths.                                                                                          |
| [get_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/get_properties.py)                 | Retrieves and formats property data from the database as foreign keys. Creates concatenated property addresses and a mapping of property IDs to addresses for reference within the real_estate_proj repository architecture.                                                                             |
| [view_edit_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_properties.py)     | Displays property details for editing, validates input fields, and updates property records in the database. Supports data retrieval and submission with error handling.                                                                                                                                 |
| [agent_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/agent_options.py)                   | Displays agent hub in the real estate project, allowing users to navigate agent-related actions. Integrates with the menu system and database utilities for seamless functionality.                                                                                                                      |
| [delete_agents.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_agents.py)                   | Deletes agents, showcasing and deleting records from the agents table in the database. Displays agent data, prompts for agent ID input, and enables deletion. Alerts on successful deletion and error occurrence.                                                                                        |
| [view_edit_clients.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_clients.py)           | Enables updating client information in a real estate app. Validates and processes user input to update client details in the database. Handles errors and provides feedback for successful updates.                                                                                                      |
| [view_edit_agents.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_agents.py)             | Enables viewing and editing agent details. Displays agents information, allows updates, and performs validation before database updates. Ensures accurate data input with standardized phone number format and verification for required fields.                                                         |
| [agent_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/agent_form.py)                         | Facilitates agent data management through a user-friendly form for adding or editing agent details. Validates form input, standardizes phone numbers, and inserts records into the database. Provides feedback on successful agent additions.                                                            |
| [property_form.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/property_form.py)                   | Enables property data entry and modification with user validation. Features interactive form elements for address, pricing, property details, agent association, and market dates. Executes database inserts based on user actions. Provides success and error feedback for property additions or edits. |
| [validate_appointment.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_appointment.py)     | Validates appointment data fields ensuring completeness before database insertion.                                                                                                                                                                                                                       |
| [validate_property.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_property.py)           | Validates property data fields including address, ZIP, price, type, characteristics, year built, and agent. Ensures correct formatting and required fields, converting values for database compatibility. Any errors return specific messages to prompt corrections.                                     |
| [validate_agent.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_agent.py)                 | First name, last name, address, city, state, zip code, and phone number format. Ensures completeness and correctness for each field, returning error messages as needed. Helps maintain data quality within the real estate project application.                                                         |
| [client_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/client_options.py)                 | Manages client operations by displaying a client hub menu and client title.-Integrates client interactions seamlessly within the real estate project.                                                                                                                                                    |
| [add_appointment.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_appointment.py)               | Enables adding appointments through a streamlined UI flow. Displays the sidebar navigation and a form to input appointment details. Integrates with database utilities for seamless data handling within the real estate project repository structure.                                                   |
| [add_client.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_client.py)                         | Manages addition of new client data through sidebar navigation in the real estate app. Displays client form for input fields and leverages database utilities for seamless integration.                                                                                                                  |
| [delete_clients.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_clients.py)                 | Displays and handles client deletion in the real estate app. Retrieves client data and prompts user to enter client ID for deletion. Notifies success or failure to delete client from the database.                                                                                                     |
| [validate_client.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/validate_client.py)               | Validates client data input for completeness and correctness in the real estate project. Checks for required fields, handles special cases like budget input, and ensures data format consistency for smooth processing within the application architecture.                                             |
| [view_edit_appointments.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/view_edit_appointments.py) | Updates and validates existing appointment details in the real estate project, displaying agent, client, and property information dynamically. Enables database record editing upon successful form submission, providing feedback on the update status.                                                 |
| [delete_properties.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_properties.py)           | Enables deleting properties in real estate project. Displays property list, allows selecting property ID, and triggers deletion with a success message or error prompt. Interacts with the database for deletion functionality.                                                                          |
| [add_agent.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/add_agent.py)                           | Implements an agent creation form with a sidebar navigation in a real estate project app. Displays fields for user input, including name, address, contact details, and start date. Integrated with database utilities and predefined state list for efficient data management.                          |
| [property_options.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/property_options.py)             | Manages property operations through a menu interface in the real_estate_proj repository. Presents property information and functionalities via Streamlit.                                                                                                                                                |
| [delete_appointments.py](https://github.com/kmspitzer/real_estate_proj/blob/master/pages/delete_appointments.py)       | Manages deletion of appointments from a database. Presents appointment details for deletion and handles user input. Displays success or error messages. Integrated within the real_estate_proj repos modular architecture for streamlined real estate management.                                        |


| File                                                                                                       | Summary                                                                                                                                                                                                                                                           |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                               |
| [real_estate_proj.sql](https://github.com/kmspitzer/real_estate_proj/blob/master/sql/real_estate_proj.sql) | Defines MySQL tables for agents, properties, clients, and appointments with attributes and relationships in the real_estate_proj database. Supports structured data storage and efficient querying for real estate management functionalities in the application. |


---

##  Getting Started

**System Requirements:**

* **Python**: `version Python 3.7+`

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

