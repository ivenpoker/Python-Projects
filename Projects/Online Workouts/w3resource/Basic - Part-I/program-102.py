# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get system command output.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import subprocess

if __name__ == "__main__":

    # file and directory listing

    returnedText = subprocess.check_output("dir", shell=True, universal_newlines=True)
    print(f"'dir' command to list file and directory:\n\n{returnedText}")