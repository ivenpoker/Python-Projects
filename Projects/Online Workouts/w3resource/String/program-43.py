#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Prints the square and cube symbol in the area of a rectangle #
#                        and volume of a cylinder.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    temp_area = 1256.66
    volume = 1254.725
    decimals = 2
    print(f'The area of the rectangle is {temp_area:.{decimals}f}cm\u00b2')
    decimals = 3
    print(f'The volume of the cylinder is {volume:.{decimals}f}cm\u00b3')
