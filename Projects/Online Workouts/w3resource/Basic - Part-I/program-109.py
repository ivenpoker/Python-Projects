# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Check if a number is positive, negative or zero.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":

    userNum = float(input("Enter enter a number: "))
    if userNum > 0:
        print(f"{userNum} is positive number")
    elif userNum == 0:
        print(f"{userNum} is zero")
    else:
        print(f"{userNum} is a negative number")
