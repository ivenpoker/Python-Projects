#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks the validity of a password.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

import re

def obtain_user_password(input_mess: str) -> str:
    user_password, valid = '', False
    while not valid:
        try:
            user_password = input(input_mess)
            if len(user_password) == 0:
                raise ValueError(f"Oops, data needed!")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_password

def passwod_valid(main_pass: str) -> bool:
    if len(main_pass) < 6 or len(main_pass) > 12:
        return True
    elif not re.search('[a-z]', main_pass):
        return True
    elif not re.search('[0-9]]', main_pass):
        return True
    elif not re.search('[A-Z]', main_pass):
        return True
    elif not re.search('[$#@]', main_pass):
        return True
    else:
        return False

if __name__ == "__main__":
    password = obtain_user_password(input_mess='Enter your password: ')
    if passwod_valid(main_pass=password):
        print(f'Password valid')
    else:
        print(f'Invalid password')