#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Display user provided names in reverse             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : 19/04/2019                                         #
#                                                                           #
#############################################################################

def print_user_names(_names):
    print("Names in reverse: {} {}".format(str(_names[1]), str(_names[0])))

def main():
    print_user_names(list(input("Enter your first (F) and last (L) names (as F L): ").split(' ')))

if __name__ == "__main__":
    main()