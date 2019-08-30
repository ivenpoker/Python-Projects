# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get the name of the host on which this script is running.    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import socket

if __name__ == "__main__":
    print(f"Host name: {socket.gethostname()}")

