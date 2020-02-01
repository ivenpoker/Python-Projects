#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if a number is pefect or not.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_number(input_mess: str) -> int:
    user_data, valid = int(-1), False
    while not valid:
        try:
            user_data = int(input(input_mess))
            if user_data <= 0:
                raise ValueError(f"Invalid number '{user_data}' must be > 0")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def is_perfect(some_num: int) -> bool:
    factors = get_factors(main_num=some_num)
    return sum(factors) == some_num

def get_factors(main_num: int) -> list:
    main_num = abs(main_num)
    if main_num == 0:
        return []
    facts = []
    temp = 1
    while temp <= main_num / 2:
        if main_num % temp == 0:
            facts.append(temp)
        temp += 1
    return facts

if __name__ == "__main__":

    user_num = obtain_user_number(input_mess='Enter number to check if perfect: ')
    print(f'Is {user_num} perfect ?: {is_perfect(some_num=user_num)}')
