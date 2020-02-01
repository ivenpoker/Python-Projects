#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Reverses a string obtained from user in console.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_string(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError("Oops! data needed")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def reverse_string(some_str: str) -> str:
    return some_str[::-1]

if __name__ == "__main__":
    main_data = obtain_user_string(input_mess='Enter a string to reverse: ')
    print(f'String in reverse: {reverse_string(some_str=main_data)}')
