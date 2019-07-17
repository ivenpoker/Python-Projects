
# !/usr/bin/env  python3

################################################################################
#                                                                              #
#       Program purpose: Finds the list common multiple (LCM) of two numbers.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                 #
#       Creation Date  : July 17, 2019                                         #
#                                                                              #
################################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def find_lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break
        z += 1
    return lcm


if __name__ == "__main__":
    intA = int(input("Enter number A: "))
    intB = int(input("Enter number B: "))

    print(f"LCM of {intA} and {intB}: {find_lcm(intA, intB)}")
