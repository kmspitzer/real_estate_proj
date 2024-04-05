import mysql.connector

from database_setup import db_connect
from standardize_phone import standardize_phone_number


def add_agent(agent_details):
    try:
        
        # Connect to the MySQL database
        conn, cursor = db_connect()

        # SQL INSERT statement
        insert_stmt = (
            "INSERT INTO agents (first_name, last_name, address_line_1, address_line_2, city, state, zip, phone, start_date, created_at) "
            "VALUES (%(first_name)s, %(last_name)s, %(address_line_1)s, %(address_line_2)s, %(city)s, %(state)s, %(zip)s, %(phone)s, %(start_date)s, NOW())"
        )

        # Execute the SQL statement
        cursor.execute(insert_stmt, agent_details)
        
        # Commit the changes
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except ValueError as ve:
        print(f"Error: {ve}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    print("Agent added successfully.")
