#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Takes two digits (row and col) and gnerates a 2D-array. The       #
#                        element value in i-th row and j-th column of the array is i*j     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_int_data(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError(f"Invalid specifed data. Must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def compute_2D_array(row: int, col: int) -> list:
    array_2D = [[0 for col in range(col)] for row in range(row)]
    for row in range(row):
        for col in range(col):
            array_2D[row][col] = row * col
    return array_2D

if __name__ == "__main__":
    num_row = obtain_user_int_data(input_mess='Enter row count: ')
    num_col = obtain_user_int_data(input_mess='Enter col count: ')