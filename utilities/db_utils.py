import pandas as pd
import mysql.connector
import json
from datetime import date



# database connection function
def db_connect():
    cnx = mysql.connector.connect(
                user='root', 
                password='password', 
                host='localhost', 
                database='real_estate_proj'
    )

    return cnx, cnx.cursor(dictionary=True)

# function to get contents of requested table
def db_get_table(tbl):
    conn, cursor = db_connect()

    try:
        query = f"SELECT * FROM {tbl}"
        df = pd.read_sql_query(query, conn)
        print(df)
        return df
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    finally:
        cursor.close()
        conn.close()

# Function to insert a new client record into the database
def insert_client(data):
    conn, cursor = db_connect()
    
    query = (
        "INSERT INTO clients (first_name, last_name, budget, preferred_move_date, "
        "address_line_1, address_line_2, city, state, zip, "
        "phone, status, agent_id, sold, created_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
    )
    
    try:
        cursor.execute(query, data)
        conn.commit()
        return cursor.lastrowid  # return the auto_increment client_id of the new record
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()


# function to insert a new property record into the database
def insert_property(data):
    conn, cursor = db_connect()
    
    query = (
        "INSERT INTO properties (address_line_1, address_line_2, city, state, zip, "
        "original_listing_price, sold_price, type, sqft, bedrooms, bathrooms, year_built, "
        "on_market, off_market, agent_id, sold, created_at) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
    )
    
    try:
        cursor.execute(query, data)
        conn.commit()
        return cursor.lastrowid  # return the auto_increment property_id of the new record
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()
