#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Converts a list of tuples into a dictionary.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 19, 2019                                                 #
#                                                                                          #
############################################################################################

from random import randint

def random_tuples_list(low: int, high: int, size: int, init_str: str) -> list:
    if size < 0:
        raise ValueError(f"Invalid size ({size}) of tuple. Must be > 0")
    main_data, cnt = [], 0
    for _ in range(size):
        temp = (f'{init_str}{cnt}', randint(low, high))
        main_data.append(temp)
        cnt += 1
    return main_data

def tuples_to_dict(main_tuples_list: list) -> dict:
    main_dict = dict()
    for (valA, valB) in main_tuples_list:
        if valA in main_dict.keys():
            main_dict[valA].append(valB)
        else:
            main_dict[valA] = [valB]
    return main_dict

if __name__ == "__main__":
    tuples_list = random_tuples_list(low=0, high=5, size=5, init_str='key')
    print(f'New tuple data: {tuples_list}')
    print(f'Dictionary equivalent: {tuples_to_dict(main_tuples_list=tuples_list)}')
