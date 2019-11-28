#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Generates and print a dictionary that contains a number (between  #
#                        1 and n) in the form (x, x*x)                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_user_N(input_mess: str) -> int:
    user_data, is_valid = '', False
    while is_valid is False:
        try:
            user_data = int(input(input_mess))
            if user_data < 0:
                raise ValueError(f'Invalid max N. Must be > 0')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def N_generate_dict(max_n: int) -> dict:
    return {x: pow(x, 2) for x in range(1, max_n+1)}

if __name__ == "__main__":
    user_int = obtain_user_N(input_mess='Enter maximum value for N: ')
    new_dict = N_generate_dict(max_n=user_int)

    print(f'Generated dictionary: {new_dict}')
