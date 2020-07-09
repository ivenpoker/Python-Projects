#!/usr/bin/env python3

import mysql
import mysql.connector
from mysql.connector import Error

class MYSQL_DB_connection:
    def __init__(self, host: str, username: str, password: str):
        try:
            self._db_connection = mysql.connector.connect(host=host,
                                                          username=username,
                                                          password=password)
            if self._db_connection.is_connected():
                self._db_info = self._db_connection.get_server_info()
                self._db_cursor = self._db_connection.cursor()
            else:
                raise Error(msg="NOT_CONNECTED_TO_DB")
        except Error as error:
            raise error

    def close_db_connection(self):
        if self._db_connection and self._db_connection.is_connected():
            if self._db_cursor:
                self._db_cursor.close()
            self._db_connection.close()

