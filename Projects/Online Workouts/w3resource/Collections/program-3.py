#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Creates a new deque with n-items and iterate over the deque's     #
#                        elements.                                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import deque

def obtain_user_data(input_mess: str) -> str:
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

def iterate_over_deque(main_deque: deque) -> None:
    for element in main_deque:
        print(f'{element}')

if __name__ == "__main__":
    main_data = obtain_user_data(input_mess='Enter some text data: ')
    new_dq = deque(main_data)

    # we now print the data in deque
    iterate_over_deque(main_deque=new_dq)
