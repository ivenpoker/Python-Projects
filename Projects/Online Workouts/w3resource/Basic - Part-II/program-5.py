#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Create a combination of 3 digit combo.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : September 4, 2019                                                #
#                                                                                         #
###########################################################################################

def generate_combination(max_range=1000):
    numbers = []
    for num in range(max_range):
        num = str(num).zfill(3)
        numbers.append(num)
    return numbers

if __name__ == "__main__":
    data = generate_combination()
    print(f"Data: {data}")
