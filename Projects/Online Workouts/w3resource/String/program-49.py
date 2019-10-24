#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Count the number of vowels in a string and displays them.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 24, 2019                                             #
#                                                                                     #
#######################################################################################

vowels = 'aeiou'

def get_user_string(mess: str):
    is_valid = False
    user_data = ''
    while is_valid is False:
        try:
            user_data = input(mess)
            if len(user_data) == 0:
                raise ValueError('Please provide a string to work with');
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def process_vowels(main_str: str):
    data_info = dict(vowel_count=0, vowels=[])
    for char in main_str:
        if char in vowels:
            data_info['vowel_count'] += 1
            data_info['vowels'].append(char)
    return data_info


if __name__ == "__main__":
    main_data = get_user_string(mess='Enter a string: ')
    new_data = process_vowels(main_str=main_data)
    print(f'String vowel info: {new_data}')