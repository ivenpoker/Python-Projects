#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts a list of tuple using a lambda expression.                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 04, 2020                                                 #
#                                                                                          #
############################################################################################

from random import randint

alphabet = 'abddefghijklmnopqrstuvwxyz'

def random_tuple_data() -> list:
    return [(i, alphabet[i]) for i in [randint(0, 25) for i in range(0, 15)]]

def sort_list_using_lambda(some_list: list) -> list:
    sorted_list = sorted(some_list, key=lambda x: x[0], reverse=False)
    return sorted_list

if __name__ == "__main__":

    main_tuple_data = random_tuple_data()
    print(f'New data: {main_tuple_data}')

    sorted_list_data = sort_list_using_lambda(some_list=main_tuple_data)
    print(f'Sorted data: {sorted_list_data}')
