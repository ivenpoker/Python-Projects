#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Check if an variable is of integer type or string type.      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == '__main__':

    firstInt = int(input("Enter first integer: "))
    secondInt = int(input("Enter second integer: "))

    if firstInt % secondInt == 0:
        print(f"Integer {firstInt} IS divisible by {secondInt}")
    else:
        print(f"Integer {firstInt} IS NOT divisible by {secondInt}")