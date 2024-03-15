import os
from dotenv import load_dotenv
import mysql.connector
import pytest


# Load environment variables from .env file
load_dotenv()

# Get environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")


# Connect to MySQL database
def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
        )
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:")
        print(error)
    return connection

def test_connect_to_database():
    connection = connect_to_database()
    assert connection is not None, "Failed to connect to database"
    connection.close()


# Test case using pytest
# def test_fetch_data(table_name, expected_count):
#     connection = connect_to_database()
#     assert connection is not None, "Failed to connect to database"
#     connection.close()

