# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get the current recursion limit value.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import sys
    print()
    print(f"Current value of the recursion limit: {sys.getrecursionlimit()}")
    print()
