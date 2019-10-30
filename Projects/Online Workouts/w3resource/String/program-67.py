#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes all consecutive duplicates of a given string.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : October 30, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_string(input_mess: str) -> str:
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

def remove_consecutive_duplicates(main_str: str) -> str:
    data, i = [], int(0)
    while i < len(main_str):
        if i+1 < len(main_str):
            if main_str[i] != main_str[i+1]:
                data.append(main_str[i])
        i += 1

    return ''.join(data)

if __name__ == "__main__":
    main_data = obtain_user_string(input_mess='Enter some string data: ')
    new_val = remove_consecutive_duplicates(main_str=main_data)
    print(f'After removing duplicates: {new_val}')
