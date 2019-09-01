# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Program to prove that two string variables of same value     #
#                        point to the same memory location.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    str1 = "Python"
    str2 = "Python"

    print(f"Memory location of str1: {hex(id(str1))}")
    print(f"Memory location of str2: {hex(id(str2))}")
