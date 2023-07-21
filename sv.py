import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name, 
            user = user_name,
            passwd = user_password,
            auth_plugin='mysql_native_password'
        )
        print("MySQL Database connection successfull")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Put our MySQL Terminal Password

pw = "admin"

# Database name
db = "StayVista"
connection = create_server_connection("localhost", "root", pw)

# create StayVista

def create_database(connection, query):
    cursor = connection.cursor()  #So this MySQL's cursor of MySQL connector pyton is used to execute statements to communicate with the MySQL database
    # MySQL cursor class initiates objects that can execute operations such as the MySQL's statements.
    try: 
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}' ")


create_database_query = "Create database StayVista"
create_database(connection, create_database_query)

# Connect to database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: '{err}' ")
    return connection


# Execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successfull")
    except Error as err:
        print(f"Error: '{err}' ")