#!/usr/bin/evn  python3

##################################################################################
#                                                                                #
#       Program purpose: Reads an integer n and find the number of combinations  #
#                        of a, b, c and d (0 <= a, b, c d <= 9) where (a + b +   #
#                        c + d) will be equal to n.                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 19, 2019                                      #
#                                                                                #
##################################################################################

import itertools

if __name__ == "__main__":
    isValid = False
    n = -1

    while isValid is False:
        try:
            n = int(input("Enter the number (n): "))
            isValid = True
        except ValueError as ve:
            print(f"ERROR: {ve}")

    result = 0
    for (i, j, k) in itertools.product(range(10), range(10), range(10)):
        result += (0 <= n - (i + j + k) <= 9)
    print(f"Number of combinations: {result}")
