#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Demonstrate use of frozensets.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 24, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":

    set_A = frozenset([1, 2, 3, 4, 5])
    set_B = frozenset([3, 4, 5, 6, 7])

    print(f' Are both sets disjoint: {set_A.isdisjoint(set_B)}')
    print(f'New set from difference: {set_A.difference(set_B)}')
    print(f' New set from both sets: {set_A | set_B}')