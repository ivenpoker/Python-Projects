#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the depth of a dictionary.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 27, 2019                                                 #
#                                                                                          #
############################################################################################

def dict_depth(some_dict: dict) -> int:
    if isinstance(some_dict, dict):
        return 1 + (max(map(dict_depth, some_dict.values())) if some_dict else 0)
    return 0

if __name__ == "__main__":
    dic = {'a': 1, 'b': {'c': {'d': {}}}}
    print(dict_depth(some_dict=dic))
