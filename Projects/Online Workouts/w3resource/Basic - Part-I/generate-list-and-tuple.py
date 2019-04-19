#!/usr/bin/env  python3

#################################################################################
#                                                                               #
#       Program purpose: Given a comma separated integers from STDIN (terminal) #
#                        prints a list and tuple of the integers.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                  #
#       Creation Date  : 19/04/2019                                             #
#                                                                               #
#################################################################################


def main():
    _data = list(input("Enter ',' separated integers: ").strip().split(', '))
    print("List: {}\nTuple: {}".format(_data, tuple(_data)))

if __name__ == '__main__':
    main()