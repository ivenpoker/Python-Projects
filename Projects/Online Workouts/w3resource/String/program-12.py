#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Counts the occurrences of each word in a sentence.           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 11, 2019                                             #
#                                                                                     #
#######################################################################################

def obtain_user_data(mess: str):
    is_valid = False
    data = ''
    while is_valid is False:
        try:
            data = input(mess)
            if len(data) == 0:
                raise ValueError('Please enter a sentence')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return data

def count_words(sentence: str):
    list_data = sentence.split()
    data = {}
    for word in list_data:
        if word in data.keys():
            data[word] += 1
        else:
            data[word] = 1
    return data

if __name__ == "__main__":
    user_data = obtain_user_data(mess='Enter a sentence: ')
    word_data = count_words(sentence=user_data)
    print(f'Obtained data: {word_data}')
