#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Iterates over elements repeating each as many times as its count. #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter

if __name__ == "__main__":
    temp = Counter(p=4, q=2, r=0, s=-2)
    print(f'Elements are: {list(temp.elements())}')
