# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Checks if an integer fits in 64 bits.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    intVal = 30
    if intVal.bit_length() <= 63:
        print((-2 ** 63).bit_length())
        print((2 ** 63).bit_length())