#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks whether a number is in a given range.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> int:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def in_range(low: int, key: int, high: int, bounded: bool = False) -> bool:
    if bounded:
        return low <= key <= high
    else:
        return low < key < high

if __name__ == "__main__":

    lower_bound = obtain_user_data(input_mess='Enter lower bound: ')
    upper_bound = obtain_user_data(input_mess='Enter upper bound: ')
    key_val = obtain_user_data(input_mess='Enter key to check: ')

    temp = obtain_user_data(input_mess='Bounded (0=true, 1=false): ')
    bounded = True if temp == 0 else False

    print(f'Is {key_val} in range ?: '
          f'{in_range(low=lower_bound, key=key_val, high=upper_bound, bounded=bounded)}')
