# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Retrieve file properties.                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import os
import time

if __name__ == "__main__":

    print(f"File          : {__file__}")
    print(f"Access time   : {time.ctime(os.path.getatime(__file__))}")
    print(f"Modified time : {time.ctime(os.path.getmtime(__file__))}")
    print(f"Change time   : {time.ctime(os.path.getctime(__file__))}")
    print(f"Size          : {os.path.getsize(__file__)}")
