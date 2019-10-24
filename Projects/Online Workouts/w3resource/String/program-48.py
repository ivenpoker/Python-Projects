#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Swaps comma and dot in a string.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 24, 2019                                             #
#                                                                                     #
#######################################################################################

def get_user_amount(mess: str):
    is_valid = False
    user_val = ''

    while is_valid is False:
        try:
            user_val = input(mess)
        except ValueError as ve:
            print(f'[ERROR]: {ve}')

    return user_val

if __name__ == "__main__":
    amount = get_user_amount(mess='Enter some amount (with dot and comma): ')
    maketrans = amount.maketrans
    amount = amount.translate(maketrans(',.', '.,'))
    print(amount)
