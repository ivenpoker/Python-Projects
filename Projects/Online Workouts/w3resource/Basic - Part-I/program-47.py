# !/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Program to find the number of CPU currently in use       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : August 9, 2019                                           #
#                                                                                 #
###################################################################################

if __name__ == "__main__":

    import multiprocessing
    print(f"Number of CPUs: {multiprocessing.cpu_count()}")

