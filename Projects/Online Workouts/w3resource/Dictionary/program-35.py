#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts a counter by value.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter

if __name__ == "__main__":
    x = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})
    print(x.most_common())
