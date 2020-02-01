#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes and prints the Pascal's triangle.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_triangle_size(input_mess: str) -> int:
    user_size, valid = int(-1), False
    while not valid:
        try:
            user_size = int(input(input_mess))
            if user_size < 0:
                raise ValueError("Invalid triangle size. Must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_size

def print_triangle(main_size: int) -> None:
    core_data = []
    curr_row = []
    for x in range(1, main_size+1):
        if x == 1 or x == 2:
            curr_row.append(1)
            core_data.append(curr_row[:])
        else:
            temp, temp_sum = 1, []
            while temp < len(curr_row):
                temp_sum.append(curr_row[temp-1] + curr_row[temp])
                temp += 1
            curr_row = curr_row[:1] + temp_sum + curr_row[-1:]
            core_data.append(curr_row[:])

    for row in core_data:
        print(row)

if __name__ == "__main__":

    triangle_size = obtain_triangle_size(input_mess='Enter triangle size: ')
    print_triangle(main_size=triangle_size)
