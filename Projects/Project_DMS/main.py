#!/usr/bin/env  python3

import os

from mysql.connector import Error
from modules import db_connect

# Initialize UI settings based on terminal size (width)

# UI_fill_width = os.get_terminal_size()[0]
UI_fill_width = 74
UI_menu_fill_char = ' '

# Initialize UI settings (for prompts) based on terminal size (width)

# UI_input_fill_width = int(int(os.get_terminal_size()[0]) / 2) + 16
UI_input_fill_width = 54
UI_input_fill_char = ' '

def obtain_login_field_data(mess: str) -> str:
    valid = False
    user_field_resp = ''

    while not valid:
        try:
            user_field_resp = input(str(mess).rjust(UI_input_fill_width, UI_input_fill_char))
            if len(user_field_resp) == 0:
                raise ValueError("Please enter VALID data")
            valid = True
        except ValueError as ve:
            print(f"[INPUT_ERROR]: {ve}")
    return user_field_resp


def print_main_menu() -> None:
    print()
    print(" [  DATA-MANAGEMENT-SYSTEM  ] ".center(UI_fill_width, UI_menu_fill_char))
    print()

def obtain_login_credentials() -> dict:
    username = obtain_login_field_data(mess="Enter system database username: ")
    password = obtain_login_field_data(mess="Enter system database password: ")

    return dict(username=username, password=password)

def print_user_login_screen(username: str, password: str) -> None:
    print("")


if __name__ == "__main__":

    is_logged_in = False
    db_connection = None
    login_error_msg = ""

    while not is_logged_in:

        os.system("clear")
        print_main_menu()

        if login_error_msg:
            print(f"{login_error_msg}".center(UI_fill_width, " "))
            print()

        db_credentials = obtain_login_credentials()

        try:
            db_connection = db_connect(host="localhost",
                                       username=db_credentials["username"],
                                       password=db_credentials["password"])
            is_logged_in = True
        except Error as e:
            login_error_msg = "---> [BAD CREDENTIALS] <---"



