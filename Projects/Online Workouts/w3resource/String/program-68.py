#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Create two strings from a given string. Create the first string   #
#                        using those character which occurs only once and create the       #
#                        second string which consists of multi-time occurring characters   #
#                        in the said string.                                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_data_from_user(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data


def process_str(main_str: str) -> dict:
    data = dict(repeat='', unique='')
    found_repeat = []
    for char in main_str:
        if main_str.count(char) > 1:
            if char not in found_repeat:
                data['repeat'] += char
                found_repeat.append(char)
        else:
            data['unique'] += char
    return data


if __name__ == "__main__":
    main_data = obtain_data_from_user(input_mess='Enter main string: ')
    proc_data = process_str(main_str=main_data)
    print(f"Repeated: {proc_data['repeat']}\nNo repeated: {proc_data['unique']}")