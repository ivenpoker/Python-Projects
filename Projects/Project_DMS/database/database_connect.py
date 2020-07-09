#!/usr/bin/env python3

import mysql
import mysql.connector
from mysql.connector import Error

class MYSQL_DB_connection:
    def __init__(self, host: str, username: str, password: str):
        self.__APP_DATABASE_NAME = "LDMS"
        self.__USER_TABLE_NAME = "USERS"
        try:
            # Try connecting to the database
            self._db_connection = mysql.connector.connect(host=host,
                                                          username=username,
                                                          password=password)
            if self._db_connection.is_connected():

                # get server information and store it.
                self._db_info = self._db_connection.get_server_info()
                self._db_cursor = self._db_connection.cursor()

                # Obtain all database names in the server
                self._db_cursor.execute("SHOW DATABASES")
                all_dbs = self._db_cursor.fetchall()

                print(f"All database: {all_dbs}")

                # check to see if we can find our application database in the MYSQL database
                found = False
                for db_tup in all_dbs:
                    # print(f"Searching app. Testing {db_tup[0]}")
                    if db_tup[0] == self.__APP_DATABASE_NAME:
                        # print(f"Found our app: {db_tup[0]}")
                        found = True
                        break

                # If we didn't find it, we create it.
                if not found:
                    self._db_cursor.reset()

                    # create a new database, since OURs wasn't existing
                    self._db_cursor.execute(f"CREATE DATABASE {self.__APP_DATABASE_NAME}")

                # setup application to use this our newly created database, as the applications
                # working database.
                self._db_cursor.reset()
                self._db_cursor.execute(f"USE {self.__APP_DATABASE_NAME}")

                self._db_cursor.reset()
                self._db_cursor.execute(f"SHOW TABLES")
                tables = self._db_cursor.fetchall()

                # If there are not tables in the database, we start creating them, else we just continue
                if len(tables) == 0:
                    # Create a new USERS table in the our new database to reflect the USERS of our application.
                    self._db_cursor.reset()
                    self._db_cursor.execute(f"CREATE TABLE {self.__USER_TABLE_NAME} (UserID int, Useranme varchar(255), Password varchar(255))")

            else:
                raise Error(msg="NOT_CONNECTED_TO_DB")
        except Error as error:
            raise error

    def close_db_connection(self):
        if self._db_connection and self._db_connection.is_connected():
            if self._db_cursor:
                self._db_cursor.close()
            self._db_connection.close()

