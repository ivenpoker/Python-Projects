# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get the size of a file.                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

import os

if __name__ == "__main__":

    try:
        file_path = input("Enter path to file: ")
        print(f"\nThe size of {file_path} is: {os.path.getsize(file_path)} bytes")

    except FileNotFoundError as fileNotFound:
        print(f"Path is not valid file.\n{fileNotFound}")
