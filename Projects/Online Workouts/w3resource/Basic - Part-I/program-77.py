# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Test whether system is big-endian platform or little-endian  #
#                        platform.                                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 17, 2019                                              #
#                                                                                     #
#######################################################################################

import sys

if __name__ == "__main__":
    if sys.byteorder == "little":
        # intel, alpha
        print("Little-endian platform.")
    else:
        # motorola, sparc
        print("Big-endian platform.")

    print()
