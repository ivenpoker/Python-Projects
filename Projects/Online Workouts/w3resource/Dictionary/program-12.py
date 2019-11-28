#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Deletes certain keys from dictionary.                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 28, 2019                                                 #
#                                                                                          #
############################################################################################

import random

def random_dict(low: int, high: int, size: int) -> dict:
    if size < 0:
        raise ValueError(f'Invalid size ({size}) for new dictionary')
    rand_keys = [random.randint(low, high) for _ in range(size)]
    rand_values = [random.randint(low, high) for _ in range(size)]

    return {k: v for (k, v) in zip(rand_keys, rand_values)}

def delete_keys_in_dict(main_dict: dict, del_keys: list) -> dict:
    print('-' * 45)
    for key in del_keys:
        if key in main_dict.keys():
            print(f"Deleting key -> '{key:02}' from dictionary...")
            del main_dict[key]
    print('-' * 45)
    return main_dict

if __name__ == "__main__":
    new_dict = random_dict(low=0, high=20, size=15)
    rand_list = [random.randint(0, 20) for _ in range(6)]

    print(f'Generated dictionary: {new_dict}')
    print(f'Keys to delete: {rand_list}')

    delete_keys_in_dict(main_dict=new_dict, del_keys=rand_list)

    print(f'After processing dictionary: {new_dict}')