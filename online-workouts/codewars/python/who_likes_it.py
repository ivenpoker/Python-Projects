#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Recreation of facebook feature on post likes.                #
#                                                                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def likes(persons: list) -> str:
    if len(persons) == 1:
        return f"{persons[0]} likes this"
    elif len(persons) == 2:
        return f"{' and '.join(persons)} like this"
    elif len(persons) == 3:
        return f"{', '.join(persons[0:2])} and {persons[2]} like this"
    else:
        return f"{', '.join(persons[0:2])} and {len(persons[2:])} others like this"

if __name__ == "__main__":
    print(likes(["Peter"]))
    print(likes(["Jacob", "Alex"]))
    print(likes(["Max", "John", "Mark"]))
    print(likes(["Alex", "Jacob", "Mark", "Max"]))

