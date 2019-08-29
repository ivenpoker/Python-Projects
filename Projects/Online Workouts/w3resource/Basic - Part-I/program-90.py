# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Create a copy of it's own source code.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 29, 2019                                              #
#                                                                                     #
#######################################################################################

import os

if __name__ == "__main__":

    new_file_name = f"{os.path.basename(__file__).split('.')[0]}-copy.py"
    new_copy = open(f"{new_file_name}", "w")
    this_file = open(f"{os.path.basename(__file__)}", "r")

    if this_file.mode == "r":
        new_copy.write(this_file.read())

