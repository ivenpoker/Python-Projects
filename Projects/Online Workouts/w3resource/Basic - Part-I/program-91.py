# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Swaps two variables.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################


if __name__ == "__main__":
    x = 1
    y = 2

    print(f"Before swap: x={x} and y={y}")
    
    x, y = y, x

    print(f"After swap: x={x} and y={y}")