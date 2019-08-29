# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Perform an action if a condition is true.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":

    some_str = input("Enter some string: ")
    if len(some_str) > 0:
        print(f"String entered is {some_str}.")
