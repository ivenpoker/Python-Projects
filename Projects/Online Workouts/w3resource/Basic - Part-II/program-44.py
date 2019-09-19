#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Finds the maximum sum of a contiguous subsequence from  #
#                        a given sequence of numbers. Subsequence of one element #
#                        is also a subsequence.                                  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 10, 2019                                      #
#                                                                                #
##################################################################################

import random

def read_data_from_keyboard():
    stop = False
    input_cnt = 1
    input_data = []
    while not stop:
        try:
            val = input(f"Enter some number [enter '.' to stop] #{input_cnt:02}: ")
            if val == '.':
                stop = True
            else:
                input_data.append(int(val))
                input_cnt += 1
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return sorted(input_data)


def compute_contiguous_sum(seq):
    if len(seq) == 1:
        return seq[0]

    sum_list = []

    for i in range(len(seq)):
        diff = 1
        temp_sum = seq[i]
        for j in range(i+1, len(seq)):
            if seq[j] - seq[i] == diff:
                temp_sum += seq[j]
                diff += 1
            else:
                sum_list.append(temp_sum)
                break
    return sorted(sum_list, reverse=True)


def random_sorted_integer_list(list_size=10):
    list_data = []
    for x in range(list_size):
        list_data.append(random.choice(seq=range(list_size)))
    return sorted(list_data)


if __name__ == "__main__":
    # data = read_data_from_keyboard()

    int_data = random_sorted_integer_list(list_size=25)

    print(f"Generated data: {int_data}")
    print(f"Sum of max contiguous: {max(compute_contiguous_sum(seq=int_data))}")
