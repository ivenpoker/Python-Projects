#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts string to dictionary.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed!')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def convert_string_to_dict(main_str: str) -> dict:
    if len(main_str) == 0:
        return dict()

    temp = list(main_str)
    new_dict = dict()

    for char in temp:
        if char not in new_dict.keys():
            new_dict[char] = 1
        else:
            new_dict[char] += 1
    return new_dict


if __name__ == "__main__":
    user_str = obtain_user_data(input_mess='Enter some string: ')
    dict_str = convert_string_to_dict(main_str=user_str)

    print(f'Dictionary equivalent: {dict_str}')