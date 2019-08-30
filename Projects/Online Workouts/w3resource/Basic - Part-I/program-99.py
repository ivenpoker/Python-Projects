# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Program to clear the terminal screen.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import os
import sys
import time

if __name__ == "__main__":

    if sys.platform == 'windows':       # If windows system
        os.system('dir')                # list it contents
        time.sleep(2)                   # wait (sleep) for 2 seconds
        os.system('cls')                # clear screen

    elif sys.platform == 'linux':       # If Linux system
        os.system('ls')                 # list it contents
        time.sleep(2)                   # wait (sleep) for 2 seconds
        os.system('clear')              # clear screen

