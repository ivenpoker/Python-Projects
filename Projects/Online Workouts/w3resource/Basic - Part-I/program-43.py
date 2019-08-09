# !/usr/bin/env  python3

#####################################################################################
#                                                                                   #
#       Program purpose: Get OS name, platform and release information.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                      #
#       Creation Date  : August 9, 2019                                             #
#                                                                                   #
#####################################################################################


if __name__ == "__main__":
    import os
    import platform

    print(f"Operating System name: {os.name}")
    print(f"Platform name: {platform.system()}")
    print(f"Release date: {platform.release()}")