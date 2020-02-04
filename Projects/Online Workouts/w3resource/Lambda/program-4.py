#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts dictionary data in list based on some property using lambda #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def random_dict_data(max_size: int) -> list:
    if max_size < 0:
        raise ValueError('Invalid specified size. Must be > 0')
    core_data = []
    for x in range(max_size):
        rand_key = randint(0, len(alphabet))
        new_dict = {'key': rand_key, 'value': alphabet[rand_key]}
        core_data.append(new_dict)
    return core_data

def sort_dict_data(dict_data: list) -> list:
    sorted_data = sorted(dict_data, key=lambda x: x['key'], reverse=False)  # sort based on 'key'
    return sorted_data

if __name__ == "__main__":

    main_data = random_dict_data(max_size=10)
    print(f'New data: {main_data}')

    sorted_dict_data = sort_dict_data(dict_data=main_data)
    print(f'Sortd data: {sorted_dict_data}')
