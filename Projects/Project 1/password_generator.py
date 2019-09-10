#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Generate password.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : September 10, 2019                                     #
#                                                                               #
#################################################################################

import random

def generate_password(size: int):
    main_str = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(random.sample(main_str, size))

if __name__ == '__main__':
    password_len = 0
    max_passwords = 0
    cont = True

    while cont:
        try:
            password_len = int(input("Enter length for password [minimum is 6]: "))
            if password_len < 6:
                raise ValueError("Invalid password length. Try again.")
            cont = False
        except ValueError as ve:
            print(f"[ERROR]: {ve}")

    cont = True
    while cont:
        try:
            max_passwords = int(input("Number of passwords to generate: "))
            cont = False
        except ValueError as ve:
            print(f"[ERROR]: {ve}")

    temp = 1
    while temp != max_passwords:
        print(f"Password #{temp}: {generate_password(size=password_len)}")
        temp += 1
