import os
from dotenv import load_dotenv
import mysql.connector
import pytest


# Load environment variables from .env file
load_dotenv()

# Get environment variables
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

def test_connect_to_database():
    assert connect_to_database is not None, "Failed to connect to database"


# Test case using pytest
# def test_fetch_data(table_name, expected_count):
#     connection = connect_to_database()
#     assert connection is not None, "Failed to connect to database"
#     connection.close()



