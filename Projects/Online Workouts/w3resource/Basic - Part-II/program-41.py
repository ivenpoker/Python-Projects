#!/usr/bin/env python3

##################################################################################
#                                                                                #
#       Program purpose: Computes and prints the sum of two given integers (more #
#                        than or equal to zero). If given integers or the sum    #
#                        have more than 80 digits, print "overflow"              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 19, 2019                                      #
#                                                                                #
##################################################################################

def read_integer(input_mess: str):

    valid = False
    int_val = 0
    while not valid:
        try:
            int_val = int(input(input_mess))
            valid = True
        except ValueError as ve:
            print(f"ERROR: {ve}")
    return int_val

def is_overflow(int_val: int):
    return int_val >= 10 ** 8


if __name__ == "__main__":

    int_a = read_integer("Enter first integer value : ")
    int_b = read_integer("Enter second integer value: ")

    if is_overflow(int_a) or is_overflow(int_b) or is_overflow(int_a + int_b):
        print(f"Overflow!")
    else:
        print(f"Sum of the two integers: {int_a + int_b}")
