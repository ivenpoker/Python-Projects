# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Find sum based on some range.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 17, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def find_sum(valA, valB):
    ans = valA + valB
    if 15 <= ans <= 20:
        return 20
    return ans

if __name__ == "__main__":
    intA = int(input("Enter first integer: "))
    intB = int(input("Enter second integer: "))

    print(f"Sum of {intA} and {intB}: {find_sum(intA, intB)}")


