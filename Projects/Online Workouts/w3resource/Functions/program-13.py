#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Checks if a word or sentence is a pangram.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def obtain_user_data(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError("Oops, data neede")
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def is_pangram(some_str: str) -> bool:
    temp_cnt = 0
    for x in alphabet:
        # Check if letter occurs at least once in alpahbet
        if some_str.count(x.lower()) >= 1:
            temp_cnt += 1
    return temp_cnt == len(alphabet)

if __name__ == "__main__":
    main_str = obtain_user_data(input_mess='Enter string data: ')
    print(f'Is string pangram ?: {is_pangram(some_str=main_str)}')
