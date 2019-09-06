#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Creates a sequence where the first four members  #
#                        of the sequence are equal to one, and each       #
#                        successive term of the sequence is equal to the  #
#                        sum of the four previous ones.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 6, 2019                                #
#                                                                         #
###########################################################################

def new_seq(num):
    if num == 1 or num == 2 or num == 3 or num == 4:
        return 1
    return new_seq(num=num-1) + new_seq(num=num-2) + new_seq(num=num-3) \
           + new_seq(num=num-4)

if __name__ == "__main__":

    print(new_seq(5))
    print(new_seq(6))
    print(new_seq(7))
