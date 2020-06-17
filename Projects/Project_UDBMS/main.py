#!/usr/bin/env  python3

from Projects.Project_UDBMS.modules import db_connect
from Projects.Project_UDBMS.modules import close_db_connection

def print_main_menu() -> None:
    print(" [USER MANAGEMENT SYSTEM] ".center(75, "#"))

if __name__ == "__main__":
    print_main_menu()
