import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError, ProgrammingError
from datetime import date
import os
from dotenv import load_dotenv

# database connection function
def db_connect():

    # read in env
    dotenv_path = os.path.join('.', 'credentials.env')
    load_dotenv(dotenv_path)

    # pull required vars
    user=os.getenv('DBUSER')
    password=os.getenv('DBPASSWORD') 
    host=os.getenv('HOST')
    database=os.getenv('DBNAME')

    # SQLAlchemy connection string
    connection_str = f'mysql://{user}:{password}@{host}/{database}'
  
    # create and return the engine
    engine = create_engine(connection_str)
    return engine


# function to get contents of requested table
def db_get_table(tbl):
    engine = db_connect()

    try:
        query = f"select * from {tbl}"
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    
    except Exception as err:
        print(f"Error: {err}")
        return None


# function to insert a new agent record into the database
def insert_agent(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        insert into agents (
            first_name, last_name, address_line_1, address_line_2, city, state, zip, 
            phone, start_date, created_at
        ) values (
            :first_name, :last_name, :address_line_1, :address_line_2, :city, :state, :zip, 
            :phone, :start_date, NOW()
        )
    """
                         )

    # execute database insert
    try:
        with engine.connect() as connection:
            # execute the query with named parameters provided in 'data'
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False


# function to insert a new agent record into the database
def insert_appointment(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        insert into appointments (
            agent_id, client_id, property_id, tour_datetime, outcome, created_at
        ) values (
            :agent_id, :client_id, :property_id,
            :tour_datetime, :outcome, NOW()
        )
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False


# function to insert a new client record into the database
def insert_client(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        insert into clients (
            first_name, last_name, budget, preferred_move_date,
            address_line_1, address_line_2, city, state, zip,
            phone, status, agent_id, sold, created_at
        ) values (
            :first_name, :last_name, :budget, :preferred_move_date,
            :address_line_1, :address_line_2, :city, :state, :zip,
            :phone, :status, :agent_id, :sold, NOW()
        )
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False


# function to insert a new property record into the database
def insert_property(data):
    engine = db_connect()
    
    # format insert statement
    sql_statement = text("""
        insert into properties (
            address_line_1, address_line_2, city, state, zip, original_listing_price,
            sold_price, type, sqft, bedrooms, bathrooms, year_built, on_market, 
            off_market, agent_id, sold, created_at
        ) values (
            :address_line_1, :address_line_2, :city, :state, :zip, 
            :original_listing_price, :sold_price, :type, :sqft, :bedrooms, 
            :bathrooms, :year_built, :on_market, :off_market, :agent_id, :sold, NOW()
        )
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False
