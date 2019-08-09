# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Get path and name of the current program under execution #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################


if __name__ == "__main__":

    import os
    fullPath = os.path.realpath(__file__)   # Extract path to this file.
    fileName = os.path.basename(fullPath)   # Retrieve base name from the path extracted.

    print(f"File name: {fileName}")
    print(f"Current File Name: {os.path.realpath(__file__)}")
