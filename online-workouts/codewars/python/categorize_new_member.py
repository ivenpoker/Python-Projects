#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: The Western Suburbs Croquet Club has two categories of       #
#                        membership, Senior and Open. Simulation of an application    #
#                        form that will tell prospective members which category they  #
#                        will be placed.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

from typing import List


def categorize_new_member(data: list) -> List:
    mem_category = []
    for mem in data:
        if int(mem[0]) >= 55 and int(mem[1]) > 7:
            mem_category.append("Senior")
        else:
            mem_category.append("Open")
    return mem_category


if __name__ == "__main__":
    mems_category = categorize_new_member([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
    print(mems_category)