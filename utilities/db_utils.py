import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError, ProgrammingError
from datetime import date



# database connection function
def db_connect():
    # SQLAlchemy connection string
    connection_str = 'mysql+mysqlconnector://root:password@localhost/real_estate_proj'
    # Create and return the engine
    engine = create_engine(connection_str)
    return engine

# function to get contents of requested table
def db_get_table(tbl):
    engine = db_connect()

    try:
        query = f"SELECT * FROM {tbl}"
        # Use the engine directly with pandas
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
        INSERT INTO agents (
            first_name, last_name, address_line_1, address_line_2, city, state, zip, 
            phone, start_date, created_at
        ) VALUES (
            :first_name, :last_name, :address_line_1, :address_line_2, :city, :state, :zip, 
            :phone, :start_date, NOW()
        )
    """)

    try:
        with engine.connect() as connection:
            # Execute the query with named parameters provided in 'data'
            connection.execute(sql_statement, data)
            connection.commit()
            return True  # Or you might want to return something specific
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False


# function to insert a new agent record into the database
def insert_appointment(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        INSERT INTO appointments (
            agent_id, client_id, property_id, tour_datetime, outcome, created_at
        ) VALUES (
            :agent_id, :client_id, :property_id,
            :tour_datetime, :outcome, NOW()
        )
    """)

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
        INSERT INTO clients (
            first_name, last_name, budget, preferred_move_date,
            address_line_1, address_line_2, city, state, zip,
            phone, status, agent_id, sold, created_at
        ) VALUES (
            :first_name, :last_name, :budget, :preferred_move_date,
            :address_line_1, :address_line_2, :city, :state, :zip,
            :phone, :status, :agent_id, :sold, NOW()
        )
    """)

    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True  # If you need to return specific data, adjust this accordingly
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False


# function to insert a new property record into the database
def insert_property(data):
    engine = db_connect()
    
    # format insert statement
    sql_statement = text("""
        INSERT INTO properties (
            address_line_1, address_line_2, city, state, zip, original_listing_price,
            sold_price, type, sqft, bedrooms, bathrooms, year_built, on_market, 
            off_market, agent_id, sold, created_at
        ) VALUES (
            :address_line_1, :address_line_2, :city, :state, :zip, 
            :original_listing_price, :sold_price, :type, :sqft, :bedrooms, 
            :bathrooms, :year_built, :on_market, :off_market, :agent_id, :sold, NOW()
        )
    """)

    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            # SQLAlchemy doesn't provide a direct way to fetch the last inserted ID with a composite primary key
            # Thus, if you need to fetch any specific value after insertion, consider executing another query here if needed
            return True
    except ProgrammingError as e:
        print(f"Insert failed: {e}")
        return False
