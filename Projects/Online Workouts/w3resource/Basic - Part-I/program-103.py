# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Extract the filename from a given path.                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import os

if __name__ == "__main__":
    mainPath = input("Enter path: ")
    print(f"Filename is: {os.path.basename(mainPath)}")
