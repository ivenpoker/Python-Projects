# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose:  Python program to get a directory listing, sorted by        #
#                         creation date.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

import os
import sys
import time
from stat import S_ISREG, ST_CTIME, ST_MODE

if __name__ == "__main__":
    # Relative or absolute path to the directory
    dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

    # all entries in the directory w/ stats
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)

    # regular files, insert creation date
    data = ((stat[ST_CTIME], path)
            for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data):
        print(time.ctime(cdate), os.path.basename(path))
