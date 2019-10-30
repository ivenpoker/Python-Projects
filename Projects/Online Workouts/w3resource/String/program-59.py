#!/usr/bin/env  python3

#########################################################################################
#                                                                                       #
#       Program purpose: Find the maximum occurring letter in a string.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 30, 2019                                               #
#                                                                                       #
#########################################################################################

def obtain_user_input(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some data to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def obtain_max_letter_count(main_str: str) -> dict:
    data = {}
    for char in main_str:
        if char in data.keys():
            data[char] += 1
        else:
            data[char] = 1
    char_max = {main_str[0]: data[main_str[0]]}
    for (k, v) in zip(data.keys(), data.values()):
        if v > list(char_max.values())[0]:
            char_max = {k: v}
    return char_max

if __name__ == "__main__":
    main_data = obtain_user_input(input_mess='Enter some string to work with: ')
    max_lett_info = obtain_max_letter_count(main_str=main_data)
    print(f'Most occurring letter: {list(max_lett_info.keys())[0]}, '
          f'occurring {list(max_lett_info.values())[0]} time(s)')

