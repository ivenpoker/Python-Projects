# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Sum of the first n positive integers.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 14, 2019                                          #
#                                                                                 #
###################################################################################


def sum_of_first_n(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    return total_sum

if __name__ == "__main__":
    user_n_value = int(input("Enter value for n: "))
    print(f"Sum of first {user_n_value} integers: {sum_of_first_n(user_n_value)}")
