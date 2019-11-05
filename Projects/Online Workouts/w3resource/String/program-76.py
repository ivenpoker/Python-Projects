#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Count the number of substrings from a given string of lowercase   #
#                        alphabets.                                                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 5, 2019                                                  #
#                                                                                          #
############################################################################################

def has_uppercase(data: str) -> bool:
    for char in data:
        if str.isupper(char):
            return True
    return False

def obtain_user_data(input_mess: str) -> str:
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops! Data is needed')
            if has_uppercase(user_data):
                raise ValueError('String must be lowercase')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def count_k_dist(str1: str, k_val: int) -> int:
    str_len = len(str1)
    result = 0
    ctr = [0] * 27

    for i in range(0, str_len):
        dist_ctr = 0
        ctr = [0] * 27
        for j in range(i, str_len):
            if ctr[ord(str1[j]) - 97] == 0:
                dist_ctr += 1
            ctr[ord(str1[j]) - 97] += 1
            if dist_ctr == k_val:
                result += 1
            if dist_ctr > k_val:
                break
    return result

if __name__ == "__main__":
    user_input_data = obtain_user_data(input_mess='Enter some string data (lowercase): ')
    k = int(-1)
    while k < 0:
        try:
            k = int(input('Input value of k: '))
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    print(f'Number of substrings with exactly {k} distinct characters: {count_k_dist(str1=user_input_data, k_val=k)}')