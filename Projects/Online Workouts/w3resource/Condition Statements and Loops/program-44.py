#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Displays a particular pattern based on some number.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_num(input_mess: str) -> int:
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

def print_pattern(some_num: int) -> None:
    for x in range(1, some_num + 1):
        print(f'{x}' * x)

if __name__ == "__main__":
    core_num = obtain_user_num(input_mess='Enter pattern size: ')
    print_pattern(some_num=core_num)

