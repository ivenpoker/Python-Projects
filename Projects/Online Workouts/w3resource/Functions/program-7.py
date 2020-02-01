#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Obtains a string from user and calculates the number of uppercase #
#                        letters and lowercase letters in the string.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError("Oops, data needed")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def compute_lowers_and_uppers(some_str: str) -> dict:
    str_info = dict(lowers=0, uppers=0)
    for x in some_str:
        if x.isupper():
            str_info['uppers'] += 1
        elif x.islower():
            str_info['lowers'] += 1
    return str_info

if __name__ == "__main__":

    main_data = obtain_user_data(input_mess='Enter some string: ')
    some_info = compute_lowers_and_uppers(some_str=main_data)

    print(f'-' * 35)

    print(f"Number of lowercase letters: {some_info['lowers']}")
    print(f"Number of uppercase letters: {some_info['uppers']}")
