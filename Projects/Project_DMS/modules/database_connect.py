#!/usr/bin/env python3

import mysql
import mysql.connector
from mysql.connector import Error

db_cursor = None
db_connection = None

def db_connect(host: str, username: str, password: str):
    global db_cursor
    global db_connection

    # If there was any previous connection to the DB,
    # we close that connection
    close_db_connection()

    try:
        db_connection = mysql.connector.connect(host=host,
                                                username=username,
                                                password=password)
        if db_connection.is_connected():
            db_info = db_connection.get_server_info()
            print(f"\rConnected to MySQL Server Version {db_info}")
            db_cursor = db_connection.cursor()
        else:
            raise Error(msg="NOT_CONNECTED_TO_DB")
    except Error as e:
        raise e


def close_db_connection():
    if db_connection and db_connection.is_connected():
        if db_cursor:
            db_cursor.close()
        db_connection.close()
