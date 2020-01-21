#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accepts a string and calculate the number of digits and letters.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError(f"Oops, data needed!")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def parse_string(main_str: str) -> dict:
    info = dict()
    for char in main_str:
        if char.isdigit():
            if 'digits' in info.keys():
                info['digits'] += 1
            else:
                info['digits'] = 1
        elif char.isalpha():
            if 'letters' in info.keys():
                info['letters'] += 1
            else:
                info['letters'] = 1
    return info

if __name__ == "__main__":

    core_data = obtain_user_data(input_mess='Enter a sentence: ')
    data_info = parse_string(main_str=core_data)
    if 'letters' in data_info.keys():
        print(f"Letters: {data_info['letters']}")
    if 'digits' in data_info.keys():
        print(f"Digits: {data_info['digits']}")
