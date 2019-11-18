#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Removes key values pairs from a list of dictionaries.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":

    original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
    print(f'Original list: {original_list}')

    new_list = [{k: v for (k, v) in d.items() if k != 'key1'} for d in original_list]
    print(f'New list: {new_list}')