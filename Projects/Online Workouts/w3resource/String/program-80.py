#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Count number of substrings with same first and last characters of #
#                        a given string.                                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_input(input_mess: str) -> str:
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

def no_of_substring_with_equal_ends(main_str: str) -> int:
    result = 0
    n = len(main_str)
    for i in range(n):
        for j in range(i, n):
            if main_str[i] == main_str[j]:
                result += 1
    return result

if __name__ == "__main__":
    user_input_data = obtain_user_input(input_mess='Enter some string data: ')
    print(f'Results: {no_of_substring_with_equal_ends(main_str=user_input_data)}')
