import mysql.connector
import json
from datetime import date

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder subclass that knows how to encode date types."""
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def db_connect():
    cnx = mysql.connector.connect(
                user='root', 
                password='hello1234', 
                host='localhost', 
                database='real_estate_proj'
    )

    return cnx, cnx.cursor(dictionary=True)

def db_get_table(tbl):

    conn, cursor = db_connect()

    data_list = []

    try:
        query = f"select * from {tbl}"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        
        for row in rows:
            data_list.append(row)
        
        # Convert the list of dictionaries to a JSON string
        json_data = json.dumps(data_list, cls=CustomJSONEncoder)
        return json_data
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    finally:
        cursor.close()
        conn.close()