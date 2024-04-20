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


# function to get agent display columns
def db_get_agent_display():
    engine = db_connect()

    try:
        query = f"""
                select  ag.first_name "First Name",
                        ag.last_name "Last Name",
                        ag.address_line_1 "Address Line 1",
                        ag.address_line_2 "Address Line 2",
                        ag.city "City",
                        ag.state "State",
                        ag.zip "ZIP",
                        ag.phone "Phone",
                        ag.start_date "Start Date"
                from agents ag
                order by ag.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None



# function to join other tables to appointments
def db_get_appointment_display():
    engine = db_connect()

    try:
        query = f"""
                select  concat(ag.first_name, ' ', ag.last_name) "Agent Name",
                        concat(cl.first_name, ' ', cl.last_name) "Client Name",
                        concat(pr.address_line_1, ', ', pr.address_line_2, ', ', pr.city, ', ', pr.state, ', ', pr.zip) "Property Address",
                        date(ap.tour_datetime) "Tour Date",
                        time(ap.tour_datetime) "Tour Time",
                        ap.outcome "Outcome"
                from appointments ap
                join agents ag on ap.agent_id = ag.agent_id
                join clients cl on ap.client_id = cl.client_id
                join properties pr on ap.property_id = pr.property_id
                order by ag.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None


# function to join agents table to clients
def db_get_client_display():
    engine = db_connect()

    try:
        query = f"""
                select  cl.first_name "First Name",
                        cl.last_name "Last Name",
                        concat('$ ', cl.budget) "Budget",
                        cl.preferred_move_date "Preferred Move Date",
                        cl.address_line_1 "Address Line 1",
                        cl.address_line_2 "Address Line 2",
                        cl.city "City",
                        cl.state "State",
                        cl.zip "ZIP",
                        cl.phone "Phone",
                        cl.status "Status",
                        concat(ag.first_name, ' ', ag.last_name) "Agent Name",
                        case cl.sold
                            when true then "Yes"
                            else "No"
                        end "Sold"
                from clients cl
                join agents ag on cl.agent_id = ag.agent_id
                order by cl.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None


# function to join agents table to properties
def db_get_properties_display():
    engine = db_connect()

    try:
        query = f"""
                select  pr.address_line_1 "Address Line 1",
                        pr.address_line_2 "Address Line 2",
                        pr.city "City",
                        pr.state "State",
                        pr.zip "ZIP",
                        concat('$ ', pr.original_listing_price) "Original Listing Price",
                        concat('$ ', pr.sold_price) "Sold Price",
                        pr.type "Type",
                        pr.sqft "Square Feet",
                        pr.bedrooms "Bedrooms",
                        pr.bathrooms "Bathrooms",
                        pr.year_built "Year Built",
                        pr.on_market "On Market",
                        pr.off_market "Off Market",
                        concat(ag.first_name, ' ', ag.last_name) "Agent Name",
                        case pr.sold
                            when true then "Yes"
                            else "No"
                        end "Sold"
                from properties pr
                join agents ag on pr.agent_id = ag.agent_id
                order by ag.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None
    
# function to join agents table to properties
def db_get_properties_by_id(property_id, agent_id):
    engine = db_connect()

    try:
        query = f"""
                select  pr.address_line_1 "Address Line 1",
                        pr.address_line_2 "Address Line 2",
                        pr.city "City",
                        pr.state "State",
                        pr.zip "ZIP",
                        pr.original_listing_price "Original Listing Price",
                        pr.sold_price "Sold Price",
                        pr.type "Type",
                        pr.sqft "Square Feet",
                        pr.bedrooms "Bedrooms",
                        pr.bathrooms "Bathrooms",
                        pr.year_built "Year Built",
                        pr.on_market "On Market",
                        pr.off_market "Off Market",
                        concat(ag.first_name, ' ', ag.last_name) "Agent Name",
                        case pr.sold
                            when true then "Yes"
                            else "No"
                        end "Sold"
                from properties pr
                join agents ag on pr.agent_id = ag.agent_id
                where pr.property_id = {property_id} AND ag.agent_id = {agent_id}
                order by ag.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None

# function to get agent display columns
def db_get_agent_by_id(agent_id):
    engine = db_connect()

    try:
        query = f"""
                select  ag.first_name "First Name",
                        ag.last_name "Last Name",
                        ag.address_line_1 "Address Line 1",
                        ag.address_line_2 "Address Line 2",
                        ag.city "City",
                        ag.state "State",
                        ag.zip "ZIP",
                        ag.phone "Phone",
                        ag.start_date "Start Date"
                from agents ag
                where ag.agent_id = {agent_id}
                order by ag.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None
    
# function to join agents table to clients
def db_get_client_by_id(client_id):
    engine = db_connect()

    try:
        query = f"""
                select  cl.first_name "First Name",
                        cl.last_name "Last Name",
                        cl.budget "Budget",
                        cl.preferred_move_date "Preferred Move Date",
                        cl.address_line_1 "Address Line 1",
                        cl.address_line_2 "Address Line 2",
                        cl.city "City",
                        cl.state "State",
                        cl.zip "ZIP",
                        cl.phone "Phone",
                        cl.status "Status",
                        case cl.sold
                            when true then "Yes"
                            else "No"
                        end "Sold",
                        cl.agent_id "Agent ID"
                from clients cl
                where cl.client_id = {client_id}
                order by cl.last_name
        """
        # use the engine directly with pandas
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as err:
        print(f"Error: {err}")
        return None

# function to join other tables to appointments
def db_get_appointment_by_id(agent_id, client_id, property_id, tour_datetime):
    engine = db_connect()

    try:
        query = f"""
                select  ap.agent_id "Agent ID",
                        ap.client_id "Client ID",
                        ap.property_id "Property ID",
                        ap.tour_datetime "Tour Datetime",
                        ap.outcome "Outcome"
                from appointments ap
                where ap.agent_id = {agent_id} and ap.client_id = {client_id} and ap.property_id = {property_id} and ap.tour_datetime = '{tour_datetime}'

        """
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
    

# function to update an existing property record in the database
def update_property(data):
    engine = db_connect()
    
    # format insert statement
    sql_statement = text("""
        update properties
        set address_line_1 = :address_line_1,
                         address_line_2 = :address_line_2,
                         city = :city,
                         state = :state,
                         zip = :zip,
                         original_listing_price = :original_listing_price,
                         sold_price = :sold_price,
                         type = :type,
                         sqft = :sqft,
                         bedrooms = :bedrooms,
                         bathrooms = :bathrooms,
                         year_built = :year_built,
                         on_market = :on_market,
                         off_market = :off_market,
                         sold = :sold
        where property_id = :property_id
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Update failed: {e}")
        return False
    

# function to update an existing client record into the database
def update_client(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        update clients 
        set first_name = :first_name,
                         last_name = :last_name,
                         budget = :budget,
                         preferred_move_date = :preferred_move_date,
                         address_line_1 = :address_line_1,
                         address_line_2 = :address_line_2,
                         city = :city,
                         state = :state,
                         zip = :zip,
                         phone = :phone,
                         status = :status,
                         agent_id = :agent_id,
                         sold = :sold
        where client_id = :client_id
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Update failed: {e}")
        return False
    
# function to update an existing agent record into the database
def update_appointment(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        update appointments 
        set agent_id = :agent_id,
                        client_id = :client_id,
                        property_id = :property_id,
                        tour_datetime = :tour_datetime,
                        outcome = :outcome
        where agent_id = :agent_id AND client_id = :client_id AND property_id = :property_id AND tour_datetime = :tour_datetime
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Update failed: {e}")
        return False

# function to update an existing agent record into the database
def update_agent(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        update agents 
        set first_name = :first_name,
                         last_name = :last_name,
                         address_line_1 = :address_line_1,
                         address_line_2 = :address_line_2,
                         city = :city,
                         state = :state,
                         zip = :zip,
                         phone = :phone,
                         start_date = :start_date
        where agent_id = :agent_id
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            # execute the query with named parameters provided in 'data'
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Update failed: {e}")
        return False
    
# function to delete an existing agent record from the database
def delete_agent(data):
    engine = db_connect()

    try:
        sql_statement = text("""
                delete from agents
                where agent_id = :agent_id
                             """)
        
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except Exception as err:
        print(f"Error: {err}")
        return None
    
    
# function to delete an existing appointment record from the database
def delete_appointment(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        delete from appointments 
        where agent_id = :agent_id AND client_id = :client_id AND property_id = :property_id AND tour_datetime = :tour_datetime
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Delete failed: {e}")
        return False
    
# function to delete an existing client record from the database
def delete_client(data):
    engine = db_connect()

    # format insert statement
    sql_statement = text("""
        delete from clients
        where client_id = :client_id
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Delete failed: {e}")
        return False
    
# function to delete an existing property record from the database
def delete_property(data):
    engine = db_connect()
    
    # format insert statement
    sql_statement = text("""
        delete from properties
        where property_id = :property_id
    """)

    # execute database insert
    try:
        with engine.connect() as connection:
            connection.execute(sql_statement, data)
            connection.commit()
            return True
    except ProgrammingError as e:
        print(f"Delete failed: {e}")
        return False