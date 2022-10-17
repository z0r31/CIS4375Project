#import mysql connector module from pytjon library
import mysql.connector
from mysql.connector import Error, connect
#define a function which will take parameters of host name from aws, assigned user name, password, and database name
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("Connection established successfully.")
    except Error as e:
        print("The error '{e}' has occured.")
    return connection

#function for executing the execute SQL query
def execute_query(connection, query):
    cursor = connection.cursor()
    

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#fuction to fetch the table results in dictionary data type
def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error '{e}' has occured")
