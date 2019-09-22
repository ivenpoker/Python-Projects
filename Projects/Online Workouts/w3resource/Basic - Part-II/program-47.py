#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Reads a text (only alphabetical characters and spaces.) #
#                        and prints two words. The first one is the word which   #
#                        is arise most frequently in the text. The second one is #
#                        the word which has the maximum number of letters.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 19, 2019                                      #
#                                                                                #
##################################################################################

import collections

def read_data(input_mess: str):
    valid = False
    main_text = ""
    while not valid:
        try:
            main_text = list(map(str, input(input_mess).strip().split()))
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: Invalid input. Try again")
    return main_text

def process_data(text_list: str):
    sc = collections.Counter(text_list)
    common_word = sc.most_common()[0][0]
    max_char = ""
    for s in text_list:
        if len(max_char) < len(s):
            max_char = s
    return common_word, max_char


if __name__ == "__main__":
    input_data = read_data("Enter some text: ")
    common_word_from_data, word_with_max_char = process_data(input_data)
    print(f"Most common word: {common_word_from_data}\nWord with max chars: {word_with_max_char}")