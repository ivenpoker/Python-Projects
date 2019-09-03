#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Converts a decimal to hexadecimal.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == '__main__':
    userInt = int(input("Enter a decimal number: "))
    print(f"Hexadecimal equivalent: {format(userInt, '02x')}")
