# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Checks if all numbers in a list are greater than a certain   #
#                        number.                                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
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

def all_values_greater_than(key=0, data=None):
    if data is None:
        return False

    for x in range(len(data)):
        if data[x] < key:
            return False

    return True


if __name__ == "__main__":
    random_data = fill_list(low=0, high=100, list_size=100)
    print_list(tmp_msg="Generated data", data=random_data, break_pt=10)

    key_val = int(input("\nEnter test integer: "))

    if all_values_greater_than(key=key_val, data=random_data):
        print(f"\nAll values are greater than {key_val}")
    else:
        print(f"\nThere is/are value(s) greater than {key_val} in data.")
