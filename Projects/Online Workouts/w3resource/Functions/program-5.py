#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the factorial of a number.                               #
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
                raise ValueError("Negative number not allowed!")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def factorial_A(some_num: int) -> int:
    if some_num <= 1:
        return 1
    return some_num * factorial_A(some_num=some_num-1)

def factorial_B(some_num: int) -> int:
    results = 1
    while some_num:
        results *= some_num
        some_num -= 1
    return results

if __name__ == "__main__":
    main_num = obtain_user_data(input_mess='Input number to compute factorial: ')

    print('-' * 35)

    print(f'Factorial (func A): {factorial_A(some_num=main_num)}')
    print(f'Factorial (func B): {factorial_B(some_num=main_num)}')