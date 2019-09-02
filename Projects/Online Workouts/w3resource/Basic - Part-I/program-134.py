# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Input two integers in a single line.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    print("Input the value of x and y: ")
    x, y = map(int, input().split())

    print(f"The value of x and y are: {x} {y}")