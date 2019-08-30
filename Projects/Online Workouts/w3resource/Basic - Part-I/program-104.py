# !/usr/bin/env  python3

#########################################################################################
#                                                                                       #
#       Program purpose: Get the effective group id, effective user id, real group id,  #
#                        a list of supplemental group ids associated with the current   #
#                        process.                                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : August 30, 2019                                                #
#                                                                                       #
#########################################################################################

import os

if __name__ == "__main__":
    
    print(f"Effective group id: {os.getegid()}")
    print(f"Effective user id: {os.geteuid()}")
    print(f"Real group id: {os.getgid()}")
    print(f"List of supplemental group ids: {os.getgroups()}")
