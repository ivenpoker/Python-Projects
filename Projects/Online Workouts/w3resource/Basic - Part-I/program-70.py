# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Program to sort files by date.                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

import glob
import os

if __name__ == "__main__":
    files = glob.glob("*.py")         # get all files in current directory ending with .py
    files.sort(key=os.path.getmtime)  # sort them based on date.

    data = "\n".join(files)           # join each item in sequence with a new line character
    print(f'{data}')                  # print the data to stdin.

