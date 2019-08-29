
# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Compute sum over a container.                                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

import random

def fill_list(low=0, high=100, list_size=100):
    data = []
    for x in range(list_size):
        data.append(random.randint(low, high-1))
    return data

def print_list(tmp_msg="", data=None, break_pt=5):
    if data is None:
        data = []
    print(f"\n{tmp_msg}: \n")

    for x in range(len(data)):
        if x % break_pt == 0 and x != 0:
            print("%02d" % (data[x]))
        else:
            print("%02d " % (data[x]), end="")
    print("")

def find_sum(data=[]):
    if data is None:
        raise TypeError

    total = 0
    for x in range(len(data)):
        total += data[x]

    return total

if __name__ == "__main__":
    data = fill_list(low=0, high=100, list_size=100)
    print_list(tmp_msg="Generated data", data=data, break_pt=10)

    print(f"\nSum over container {find_sum(data=data)}")
