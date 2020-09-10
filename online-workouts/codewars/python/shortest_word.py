#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Given an array of integer list items, finds the first index  #
#                        within the array where the sum of all elements to the left   #
#                        of the index of the array equals those to the right of the   #
#                        index.                                                       #
#                                                                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################

def find_shortest_word_length(sentence: str) -> int:
    words = sentence.split(" ")
    shortest_len = len(words[0].strip())
    for word in words:
        if len(word.strip()) < shortest_len:
            shortest_len = len(word)
    return shortest_len

if __name__ == "__main__":
    print(find_shortest_word_length(sentence="bitcoin take over the world maybe who knows perhaps"))