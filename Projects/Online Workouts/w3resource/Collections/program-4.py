#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Finds the occurrences of 10 most common words in a given text.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 27, 2019                                                 #
#                                                                                          #
############################################################################################

from collections import Counter
import re

def obtain_file_data(input_mess: str) -> list:
    file_data, valid = [], False
    while not valid:
        try:
            file_name = input(input_mess)
            if len(file_name) == 0:
                raise ValueError('Oops, file name needed!')
            for line in open(file_name, 'r'):
                file_data.append(line)
            valid = True
        except ValueError as ve:
            print(f'[INPUT-ERROR]: {ve}')
        except IOError as ioE:
            print(f'[FILE-ERROR]: {ioE}')
    return file_data

if __name__ == "__main__":
    new_file_data = obtain_file_data(input_mess='Enter file name (or path): ')
    words = re.findall('\w+', ' '.join(new_file_data))
    print(f'-' * 100)
    print(f'THE 10 MOST COMMON WORDS:\n\n {Counter(words).most_common(10)}')
