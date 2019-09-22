#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Reads the two adjoined sides and the diagonal of a      #
#                        parallelogram and check whether the parallelogram is a  #
#                        rectangle or a rhombus                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 22, 2019                                      #
#                                                                                #
##################################################################################

if __name__ == "__main__":
    print("Input two adjoined sides and the diagonal of a parallelogram (comma separated): ", end="")
    valid = False
    while not valid:
        try:
            (a, b, c) = map(int, input().split(","))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    if c ** 2 == a ** 2 + b ** 2:
        print('This is a rectangle.')
    if a == b:
        print('This is a rhombus.')
