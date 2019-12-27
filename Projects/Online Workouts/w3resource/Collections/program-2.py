#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the most common elements and their counts of a specified    #
#                        text.                                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter

def obtain_user_input(input_mess: str) -> str:
    user_data, valid = '', False
    while not valid:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Oops, data needed!')
            valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

if __name__ == "__main__":
    new_data = obtain_user_input(input_mess='Enter some text: ')
    top_common = Counter(new_data).most_common(3)
    print(f'Most common three characters of said text: {top_common}')
