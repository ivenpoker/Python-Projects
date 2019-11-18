#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Generates groups of five consecutive numbers in list.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

if __name__ == "__main__":
    temp_list = [[5 * i + j for j in range(1, 6)] for i in range(5)]
    print(f'Generated list: {temp_list}')