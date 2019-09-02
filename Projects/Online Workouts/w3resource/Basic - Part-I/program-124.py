# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Check if multiple variables have the same value.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    firstVal = input("Enter first input: ")
    secondVal = input("Enter second input: ")
    thirdVal = input("Enter third input: ")

    if firstVal == secondVal == thirdVal:
        print("All variables have same value!")
    else:
        print("Some or All variables don't have same value")