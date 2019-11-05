#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Counts characters at same position in a given string (lower and   #
#                        uppercase characters) as in English alphabet.                     #
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

def count_char_position(str1: str) -> int:
    count_chars = 0
    for i in range(len(str1)):
        if (i == ord(str1[i]) - ord('A')) or (i == ord(str1[i]) - ord('a')):
            count_chars += 1
    return count_chars

if __name__ == "__main__":
    user_input = obtain_user_input(input_mess='Enter a string data: ')
    print(f'Number of characters of the said string at same position as in English alphabet: '
          f'{count_char_position(str1=user_input)}')