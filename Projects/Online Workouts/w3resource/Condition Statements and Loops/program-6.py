#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Count number of evens an odds from a series of numbers.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

from random import randint

def random_int_list(low: int, high: int, size: int) -> list:
    if size < 0:
        raise ValueError(f"Invalid specified siz '{size}'")
    return [randint(low, high) for _ in range(size)]

def count_evens_and_odds(main_data: list) -> dict:
    main_dict = dict()
    for x in main_data:
        if int(x) % 2 == 0:
            if 'evens' in main_dict.keys():
                main_dict['evens'] += 1
            else:
                main_dict['evens'] = 1
        else:
            if 'odds' in main_dict.keys():
                main_dict['odds'] += 1
            else:
                main_dict['odds'] = 1
    return main_dict

if __name__ == "__main__":
    list_data = random_int_list(low=0, high=20, size=10)
    print(f'Random list: {list_data}')

    info_dict = count_evens_and_odds(main_data=list_data)
    print(f"Number of evens: {info_dict['evens']}, Number of odds: {info_dict['odds']}")