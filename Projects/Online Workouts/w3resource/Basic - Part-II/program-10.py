#!/usr/bin/env  python3

#######################################################################
#                                                                     #
#       Program purpose: Display some information about OS where the  #
#                        script is running.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>        #
#       Creation Date  : September 5, 2019                            #
#                                                                     #
#######################################################################

import platform as pl

if __name__ == "__main__":

    os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]
    for key in os_profile:
        if hasattr(pl, key):
            print(f"{key}: {str(getattr(pl, key)())}")
