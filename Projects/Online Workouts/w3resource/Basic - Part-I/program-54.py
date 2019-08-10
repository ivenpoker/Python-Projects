# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Get current username of user in system                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 10, 2019                                          #
#                                                                                 #
###################################################################################

import getpass

if __name__ == "__main__":
    print(f"Current username: {getpass.getuser()}")