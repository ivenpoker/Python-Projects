#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a string is an integer or not.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError(f'Oops! data needed')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def determine_type(main_test: str) -> None:
    try:
        result_int = int(main_test)
        if result_int:
            print(f'String is an integer')
    except ValueError:
        print(f'String is not an ingeer')

if __name__ == "__main__":
    test_int = obtain_user_input(input_mess='Enter a string: ')
    determine_type(main_test=test_int)
