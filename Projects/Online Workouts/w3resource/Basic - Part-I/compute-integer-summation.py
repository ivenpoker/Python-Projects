#!/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Prints the sum 'n + nn + nnn' for some 'n' from user.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : 19/04/2019                                               #
#                                                                                 #
###################################################################################


def print_summation(_val):
    return int("{}".format(_val)) + int("{}{}".format(_val, _val)) + int("{}{}{}".format(_val, _val, _val))

def main():
    results = print_summation(int(input("Enter the value of n: ")))
    print("Result: {}".format(results))

if __name__ == '__main__':
    main()