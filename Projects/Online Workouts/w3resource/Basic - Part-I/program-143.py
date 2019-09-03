#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Determines if the python shell is executing in 32-bit or 64-bit   #
#                        mode on operating system.                                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : September 3, 2019                                                 #
#                                                                                          #
############################################################################################

import struct
import sys

if __name__ == '__main__':
    print(f'Shell is executing in {(struct.calcsize("P") * 8)}-bit mode on this {sys.platform} system')
