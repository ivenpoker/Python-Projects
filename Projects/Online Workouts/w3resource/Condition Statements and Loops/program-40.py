#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Find the mean an median of three values.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

from math import floor

def obtain_user_data(input_mess: str) -> int:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def find_mean(main_data: list) -> float:
    temp_sum = sum(main_data)
    return float(temp_sum / len(main_data))

def find_median(main_data: list) -> float:
    mid = floor(len(main_data) / 2)
    return main_data[mid]

if __name__ == "__main__":

    int_A = obtain_user_data(input_mess='Enter int A: ')
    int_B = obtain_user_data(input_mess='Enter int B: ')
    int_C = obtain_user_data(input_mess='Enter int C: ')

    print('\n', '=' * 10, "[ RESULTS ]", '=' * 10, '\n')

    print(f'Mean is: {find_mean(main_data=[int_A, int_B, int_C] )}')
    print(f' Median: {find_median(main_data=[int_A, int_B, int_C])}')

