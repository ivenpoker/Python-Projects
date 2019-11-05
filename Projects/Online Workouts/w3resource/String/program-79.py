#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the smallest and largest word in a given string.            #
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

def find_smallest_and_largest_words(str_data: str) -> dict:

    str_data = str_data.split()
    info = dict(largest=str_data[0].strip(), smallest=str_data[0].strip())
    for word in str_data:
        word = word.strip()
        if len(word) > len(info['largest']):
            info['largest'] = word
        elif len(word) < len(info['smallest']):
            info['smallest'] = word
    return info

if __name__ == "__main__":
    user_input_data = obtain_user_input(input_mess='Enter some string data: ')
    data_info = find_smallest_and_largest_words(str_data=user_input_data)

    print(f"Smallest word: {data_info['smallest']}\nLargest word: {data_info['largest']}")
