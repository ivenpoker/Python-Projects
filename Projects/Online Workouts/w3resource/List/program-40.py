#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Sorts a list based on the first character of word.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 18, 2019                                                 #
#                                                                                          #
############################################################################################

from itertools import groupby
from operator import itemgetter

if __name__ == "__main__":
    word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                 'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

    for (letter, words) in groupby(sorted(word_list), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)