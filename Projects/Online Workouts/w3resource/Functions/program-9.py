#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Tests whether a number is prime or not.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_int(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError("Number must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def num_factors(some_num: int) -> int:
    some_num = abs(some_num)
    if some_num == 1:
        return 1
    num_facts = 2       # 1 and the number itself
    temp = 2
    while temp < some_num/2:
        if some_num % temp == 0:
            num_facts += 1
        temp += 1
    return num_facts


def is_prime(some_num: int) -> bool:
    return num_factors(some_num=some_num) == 2

if __name__ == "__main__":

    main_num = obtain_user_int(input_mess='Enter some number [> 0]: ')
    print(f'Is {main_num} prime: {is_prime(some_num=main_num)}')