#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes item(s) from set.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 20, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_set_data(low: int, high: int, size: int) -> set:
    if size < 0:
        raise ValueError(f"Invalid size ({size}). Must be > 0")
    return set([randint(low, high) for _ in range(size)])

def remove_data_from_set(main_set: set) -> None:
    while len(main_set) > 0:
        print(f'Set data: {main_set}')
        print(f'-' * 40)
        try:
            user_val = int(input('Enter data to remove: '))
            if user_val in main_set:
                main_set.remove(user_val)
                print(f'Removal ... [DONE]')
            else:
                print(f'Removal ... [FAILED]')
        except ValueError as ve:
            print(f'{ve}')
        print(f'-' * 40)

if __name__ == "__main__":
    new_set = random_set_data(low=0, high=10, size=15)
    print(f'New set data: {new_set}')
    print('-' * 40)

    remove_data_from_set(main_set=new_set)
