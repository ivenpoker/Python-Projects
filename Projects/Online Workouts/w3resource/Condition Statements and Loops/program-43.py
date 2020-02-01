#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a multiplication table (from 1 to 10) of a number.        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError("Invalid input. Must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def display_multiplication_table(some_num: int) -> None:
    for x in range(1, 11):
        print(f'{some_num:2} x {x:2}: {some_num * x:2}')

if __name__ == "__main__":
    main_num = obtain_user_data(input_mess='Enter a number: ')
    display_multiplication_table(some_num=main_num)
