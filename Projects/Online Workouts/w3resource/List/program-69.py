#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the depth of a dictionary.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 23, 2019                                                 #
#                                                                                          #
############################################################################################

def dict_depth(core_dict: dict) -> int:
    if isinstance(core_dict, dict):
        return 1 + (max(map(dict_depth, core_dict.values())) if core_dict else 0)
    return 0

if __name__ == "__main__":
    main_dict = {'a': 1, 'b': {'c': {'d': {}}}}
    print(f'Depth of dictionary: {dict_depth(core_dict=main_dict)}')