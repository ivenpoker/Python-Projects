#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Converts a set of strings with specific format to camel case #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################


def to_camel_case(main_str: str) -> str:
    new_str = None

    if main_str.find('-') >= 0:
        tokens = main_str.split("-")
        new_str = tokens[0]
        for (idx, val) in enumerate(tokens):
            if idx > 0:
                val = f'{val[0].upper()}{val[1:]}'
                new_str = f'{new_str}{val}'

    tokens = new_str.split("_") if new_str else main_str.split("_")
    new_str = tokens[0]
    for (idx, val) in enumerate(tokens):
        if idx > 0:
            val = f'{val[0].upper()}{val[1:]}'
            new_str = f'{new_str}{val}'

    return new_str if new_str else main_str

if __name__ == "__main__":
    print(to_camel_case(main_str="the-stealth-warrior"))
    print(to_camel_case(main_str="The_Stealth_Warrior"))
    print(to_camel_case(main_str="A-pippi_is-Omoshiroi"))



