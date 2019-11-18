#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Converts list to list of dictionaries.                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

def convert_list_to_dict(listA: list, listB: list, proposed_keys: list) -> list:
    return [{proposed_keys[0]: v1, proposed_keys[1]: v2} for v1, v2 in zip(listA, listB)]

if __name__ == "__main__":
    color_name = ["Black", "Red", "Maroon", "Yellow"]
    color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    print(f'List of dict:'
          f"\n{convert_list_to_dict(listA=color_name, listB=color_code, proposed_keys=['color_name', 'color_code'])}")
