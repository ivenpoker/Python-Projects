#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the minimum window in a given string which will contain all #
#                        the characters of another given string.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

import collections

def obtain_user_data(input_mess: str) -> str:
    user_data, is_valid = '', False
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_data(strA: str, strB: str) -> str:
    result_char, missing_char = collections.Counter(strB), len(strB)
    i = p = q = 0
    for (j, c) in enumerate(strA, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[strA[i]] < 0:
                result_char[strA[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return strA[p:q]

if __name__ == "__main__":
    data_A = obtain_user_data(input_mess=' Enter first string: ')
    data_B = obtain_user_data(input_mess='Enter second string: ')

    print(f'Original strings: StrA -> {data_A} | StrB -> {data_B}')
    print(f'Minimum window: {process_data(strA=data_A, strB=data_B)}')
