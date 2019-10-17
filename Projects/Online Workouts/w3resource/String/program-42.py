#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Counts the repeated characters in a string and display them. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_data(input_mess: str):
    is_valid = False
    user_data = ''
    while is_valid is not True:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please provide some text data')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def obtain_occurrences(main_str: str):
    info_data = {}
    for char in main_str:
        if char not in info_data.keys() and str.isalpha(char):
            info_data[char] = main_str.count(char)
    return info_data

if __name__ == "__main__":

    user_text = get_user_data(input_mess='Enter some text: ')
    new_data = obtain_occurrences(main_str=user_text)
    repeated_char = [key for key in new_data.keys() if new_data[key] >= 2]
    print(f'Characters that repeat: {repeated_char}')

