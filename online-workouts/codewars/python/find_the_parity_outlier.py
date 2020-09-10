#!/usr/bin/env python3

#######################################################################################
#                                                                                     #
#       Program purpose: Finds the parity outlier of a list of numbers.               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 10, 2020                                           #
#                                                                                     #
#######################################################################################


def find_parity(num_list: list) -> int:
    def is_even(val: int) -> bool:
        return val % 2 == 0

    def is_odd(val: int) -> bool:
        return val % 2 == 1

    if is_even(num_list[0]) and is_even(num_list[1]):
        return list(filter(is_odd, num_list))[0]

    elif is_odd(num_list[0] and is_odd(num_list[1])):
        return list(filter(is_even, num_list))[0]

    else:
        if is_even(num_list[0]) and is_even(num_list[2]):
            return num_list[1]

        elif is_even(num_list[1]) and is_even(num_list[2]):
            return num_list[0]

        elif is_odd(num_list[0]) and is_odd(num_list[2]):
            return num_list[1]

        elif is_odd(num_list[1]) and is_odd(num_list[2]):
            return num_list[0]


if __name__ == "__main__":
    print(find_parity(num_list=[3667261, -2437231, -4347355, -8742391, 2594691, 594986,
                                -8394681, -2387287, -2793501, 4640481, 5191757, -6023855,
                                9136251, -9004123, -5850287, -9660449, 1135181, -3011513,
                                -7344243, 9112395, -9657865, -8302959, -4996551, 6732885,
                                -9231851, -3472249, 9923247, -7943829, 191247, -1058677,
                                -584431, 1050943]))
