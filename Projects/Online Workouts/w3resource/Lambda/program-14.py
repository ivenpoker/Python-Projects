#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Filters a given list whether the values in the list are having    #
#                        length of 6 using Lambda.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 05, 2020                                                 #
#                                                                                          #
############################################################################################

from typing import Callable

def FUNC_filter_by_len(some_data: list) -> Callable:
    return lambda: [x for x in some_data if len(x) == 6]

if __name__ == "__main__":

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    main_func = FUNC_filter_by_len(some_data=weekdays[:])

    print(f'Days with length 6: {main_func()}')