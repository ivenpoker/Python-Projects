#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Performs a sum on two integers. However if the sum is between 15  #
#                        to 20, will return 20.                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def perform_sum(valA: int, valB: int) -> int:
    temp_sum = valA + valB
    if 15 <= temp_sum <= 20:
        temp_sum = 20
    return temp_sum

if __name__ == "__main__":
    int_A = obtain_user_input(input_mess=' Enter first int: ')
    int_B = obtain_user_input(input_mess='Enter second int: ')
    print(f"Sum is: {perform_sum(valA=int_A, valB=int_B)}")

    print('-' * 20)

    print(f'Test case #1: {perform_sum(10, 6)}')
    print(f'Test case #2: {perform_sum(10, 2)}')
    print(f'Test case #3: {perform_sum(10, 12)}')
