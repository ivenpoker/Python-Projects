#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Constructs a pyramidal pattern, using nested for loop.            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def construct_pattern(max_size: int) -> None:
    if max_size < 0:
        raise ValueError(f"Invalid patter size '{max_size}'")

    for i in range(max_size):
        if i <= int(max_size/2):
            temp = ('*' * i).split()
            print(' '.join(temp))
        else:
            temp = ('*' * (max_size - i)).split()
            print(' '.join(temp))


if __name__ == "__main__":
    construct_pattern(max_size=100)
