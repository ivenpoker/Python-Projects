#!/usr/bin/env  python3

##############################################################################################
#                                                                                            #
#       Program purpose: Counts the occurrences of character of a given text in a text       #
#                        file, that is, it finds occurrences of each character in file.      #                                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                               #
#       Creation Date  : September 5, 2019                                                   #
#                                                                                            #
##############################################################################################

def process_data(list_string=None):
    if list_string is None:
        return {}

    data = {}

    for text in list_string:
        for x in range(len(text)):
            if text[x] in data.keys():
                data[text[x]] = data.get(text[x]) + 1
            else:
                data[text[x]] = 1
    return data


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    file = open(file_name, "r")

    if file.mode == "r":
        contents = file.readlines()
        new_data = process_data(list_string=contents)
        print(f"Processed data:\n{new_data}")
