#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Takes a positive integer as its parameter and returns a      #
#                        string containing the Roman Numeral representation of that   #
#                        integer.                                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def roman_numerals_as_string(some_num: int) -> str:

    def __in_range(low: int, val: int, high: int) -> bool:
        return low <= val <= high

    def __roman_str_gen(num: int, some_str: str) -> str:
        if __in_range(low=1, val=num, high=3):
            return __roman_str_gen(num=num-1, some_str=f"{some_str}I")

        elif num == 4:
            return f"{some_str}IV"

        elif __in_range(low=5, val=num, high=8):
            return __roman_str_gen(num=num-5, some_str=f"{some_str}V")

        elif num == 9:
            return f"{some_str}IX"

        elif __in_range(low=10, val=num, high=49):
            return __roman_str_gen(num=num-10, some_str=f"{some_str}X")

        elif __in_range(low=50, val=num, high=99):
            return __roman_str_gen(num=num-50, some_str=f"{some_str}L")

        elif __in_range(low=100, val=num, high=499):
            return __roman_str_gen(num=num-100, some_str=f"{some_str}C")

        elif __in_range(low=500, val=num, high=999):
            return __roman_str_gen(num=num-500, some_str=f"{some_str}D")

        elif num == 1000:
            return f"{some_str}M"

        elif num > 1000:
            return __roman_str_gen(num=num-1000, some_str=f"{some_str}M")
        else:
            return some_str


    return __roman_str_gen(num=some_num, some_str="")


if __name__ == "__main__":
    print(roman_numerals_as_string(some_num=1990))