#!/usr/bin/env  python3

#########################################################################################
#                                                                                       #
#       Program purpose: Find the operating system name, platform and platform release  #
#                        date.                                                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : September 3, 2019                                              #
#                                                                                       #
#########################################################################################

import os
import platform

if __name__ == '__main__':
    print(f"Operating system name: {os.name}")
    print(f"Platform name: {platform.system()}")
    print(f"Platform release: {platform.release()}")