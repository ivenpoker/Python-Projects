#!/usr/bin/env  python3

#####################################################################################
#                                                                                   #
#       Program purpose: Display the difference of a number with 17, if the number  #
#                        is greater than 17 return double the absolute difference   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                      #
#       Creation Date  : 19/04/2019                                                 #
#                                                                                   #
#####################################################################################

def compute_difference(_val):
    if _val > 17:
        return 2 * (_val - 17)
    else:
        return 17 - _val

def main():
    val = int(input("Enter the number: "))
    print("Difference: {}".format(compute_difference(val)))

if __name__ == '__main__':
    main()