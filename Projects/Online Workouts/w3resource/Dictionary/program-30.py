#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets the top three items in a shop.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

import operator

def sort_dict(main_dict: dict, ascending=True) -> dict:
    return dict(sorted(main_dict.items(), key=operator.itemgetter(1))) if ascending else\
        dict(sorted(main_dict.items(), key=operator.itemgetter(1), reverse=True))

def find_top_n_items_in_shop(shop_data: dict, top_n: int) -> dict:
    if top_n < 0 or top_n > len(shop_data):
        raise ValueError(f'Invalid value from top. Must be in range [0, {len(shop_data)}]')
    new_data = sort_dict(main_dict=shop_data, ascending=False)
    results, temp = {}, 0
    for (k, v) in zip(new_data.keys(), new_data.values()):
        if temp <= top_n:
            results[k] = v
            temp += 1
    return results

if __name__ == "__main__":
    shop_items = {'item1': 42.50, 'item2': 41.30, 'item4': 55, 'item50': 24}
    top_three = find_top_n_items_in_shop(shop_data=shop_items, top_n=3)
    print(f'Top 3 items in shop: {top_three}')
