#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a list of characters to a string.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

def char_list(some_data: str) -> list:
    temp_list = []
    for word in some_data:
        for char in word:
            if not str.isspace(char):
                temp_list.append(char)
    return temp_list

def char_list_to_string(list_data: list) -> str:
    return ''.join(list_data)

if __name__ == "__main__":

    temp_str = 'This is some sample string'
    new_data = char_list(some_data=temp_str)
    print(f'  Sample characters: {char_list(new_data)}')
    print(f'After joining chars: {char_list_to_string(list_data=new_data)}')
