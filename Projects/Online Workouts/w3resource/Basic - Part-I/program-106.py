# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Divide a path on the extension separator.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

import os

if __name__ == "__main__":
    for path in ['text.txt', 'filename', '/user/system/test.txt', '/', '']:
        print(f"{path}: {os.path.splitext(path)}")
