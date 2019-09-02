# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: List home directory without absolute path.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

import os

if __name__ == "__main__":
    print(f"Home directory: {os.path.expanduser('~')}")