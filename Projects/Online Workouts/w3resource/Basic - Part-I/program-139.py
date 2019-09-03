#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Validates an IP Address.                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 3, 2019                                            #
#                                                                                     #
#######################################################################################

import socket

if __name__ == '__main__':
    addr = '127.0.0.2561'
    try:
        socket.inet_aton(addr)
        print(f"Valid IP -> {addr}")
    except socket.error as error:
        print(f"Invalid IP [{error}]")