#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Counts Uppercase, Lowercase, special character and numeric values #
#                        in a given string.                                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR] {ve}')
    return user_data

def process_data(main_data: str) -> dict:
    data = dict(upper_cnt=0, lower_cnt=0, spec_char=0, num_val=0)
    for char in main_data:
        if str.isupper(char):
            data['upper_cnt'] += 1
        elif str.islower(char):
            data['lower_cnt'] += 1
        elif str.isnumeric(char):
            data['num_val'] += 1
        else:
            data['spec_char'] += 1
    return data

if __name__ == "__main__":

    user_input = obtain_user_data(input_mess='Enter input data: ')
    data_info = process_data(main_data=user_input)

    for (key, val) in zip(data_info.keys(), data_info.values()):
        print(f'{key}: {val}')