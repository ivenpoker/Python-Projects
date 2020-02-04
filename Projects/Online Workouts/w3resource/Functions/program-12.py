#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Check if string is a palindrome or not.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

def obtain_user_data(input_mess: str) -> str:
    user_data, valid = str(''), False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def is_palindrome(some_str: str) -> bool:
    if not some_str or len(some_str) == 0:
        return False
    if len(some_str) == 1:
        return True
    if len(some_str) % 2 == 0:
        tmp_len = int(len(some_str) / 2)
        return some_str[:tmp_len] == some_str[tmp_len:][::-1]
    else:
        tmp_len = int(len(some_str) / 2)
        return some_str[:tmp_len] == some_str[tmp_len+1:][::-1]

if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter string to check if palindrome: ')
    print(f"Is string a palindrome: {'YES' if is_palindrome(some_str=main_data) else 'NO'}")
