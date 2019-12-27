#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accepts some words and count the number of distinct words. Print  #
#                        the number of distinct words and number of occurrences for each   #
#                        distinct word according to their appearances.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == "__main__":
    word_array = []
    temp = int(input('Input number of words: '))
    print('Input the words')

    for i in range(temp):
        word_array.append(input().strip())
    word_ctr = OrderedCounter(word_array)

    print(len(word_ctr))
    for word in word_ctr:
        print(word_ctr[word], end=' ')
