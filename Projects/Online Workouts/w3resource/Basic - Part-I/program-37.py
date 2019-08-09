# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Prints details in formatted manner.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 17, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php


def print_details(age, name, address):
    print(f"Name: {age}\nAge: {name}\nAddress: {address}")

if __name__ == "__main__":
    print_details(age=12, name="James", address="Bunker")
