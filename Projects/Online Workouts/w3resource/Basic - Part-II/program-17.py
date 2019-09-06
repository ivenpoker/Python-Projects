#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Gets all strobogrammatic numbers that are of  #
#                        length 'n'.                                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

def gen_strobogrammatic(num):
    """
    Compute various numbers of 'n'
    :param num: Number
    :return: List of string.
    """
    result = helper(num=num, length=num)
    return result

def helper(num, length):
    if num == 0:
        return [""]
    if num == 1:
        return ["1", "0", "8"]
    middles = helper(num-2, length=length)
    result = []

    for middle in middles:
        if num != length:
            result.append(f"0{middle}0")
        result.append(f"8{middle}8")
        result.append(f"1{middle}1")
        result.append(f"9{middle}6")
        result.append(f"6{middle}9")
    return result

if __name__ == "__main__":

    print(f"n = 2 -> {gen_strobogrammatic(2)}")
    print(f"n = 3 -> {gen_strobogrammatic(3)}")
    print(f"n = 4 -> {gen_strobogrammatic(4)}")
    print(f"n = 5 -> {gen_strobogrammatic(5)}")

