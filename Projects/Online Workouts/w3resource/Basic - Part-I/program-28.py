# !/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Prints even numbers in list before an exception.   #
#                        The exception being inclusive.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : July 17, 2019                                      #
#                                                                           #
#############################################################################

# URL: https://www.w3resource.com/python-exercises/python-basic-exercises.php

def print_even(num, exc):
    for x in num:
        if int(x) % 2 == 0 and x != exc:
            print(f"{x} ")
        elif x == exc:
            print(f"{x} ")
            break

if __name__ == "__main__":
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527]
    print_even(numbers, 237)
