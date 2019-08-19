# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get the command-line arguments (name of the script, the      #
#                        number of arguments, arguments) passed to a script.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

import sys

if __name__ == "__main__":
    print(f"Name of script: {sys.argv[0]}")
    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Argument list: {sys.argv}")
