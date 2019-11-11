#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Generate and print a list of first and last 5 elements where the  #
#                        values are square of the numbers between 1 and 30                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 11, 2019                                                 #
#                                                                                          #
############################################################################################

def obtain_list(size: int) -> dict:
    if size < 10:
        raise ValueError('Invalid size of list. Must be > 10')
    temp_list = []
    for (i, x) in enumerate(range(size)):
        if i <= 5 or (i in range(size-5, size)):
            if i == 0:
                continue
            temp_list.append(i ** 2)
        else:
            temp_list.append(i)
    return {0: temp_list[:5], 1: temp_list[len(temp_list)-5:]}

if __name__ == "__main__":
    print(f'Processed data: {obtain_list(size=21)}')