#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Find the smallest window that contains all characters of a given  #
#                        string.                                                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

from collections import defaultdict

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops! Data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


def find_sub_string(some_str: str) -> str:
    str_len = len(some_str)

    # Count all distinct characters
    dist_count_char = len(set([x for x in some_str]))

    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0)
    for i in range(str_len):
        curr_count[some_str[i]] += 1

        if curr_count[some_str[i]] == 1:
            ctr += 1
        if ctr == dist_count_char:
            while curr_count[some_str[start_pos]] > 1:
                if curr_count[some_str[start_pos]] > 1:
                    curr_count[some_str[start_pos]] -= 1
                start_pos += 1

            len_window = i - start_pos + 1
            if min_len > len_window:
                min_len = len_window
                start_pos_index = start_pos
    return some_str[start_pos_index: start_pos_index + min_len]

if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter some string data: ')
    print(f'Smallest window that contains all characters of the said string: {find_sub_string(some_str=main_data)}')