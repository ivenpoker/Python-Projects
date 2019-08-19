# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Finds the sum of individual digits in an integer number.     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################


def find_sum_of_digits(some_num):
    total = 0
    while some_num is not 0:
        total += some_num % 10
        some_num //= 10
    return total


if __name__ == "__main__":

    try:
        data = int(input("Enter an integer: "))

    except ValueError as ve:
        print(f"Can't convert input to int")

    print(f"Sum of digits is: {find_sum_of_digits(some_num=data)}")

