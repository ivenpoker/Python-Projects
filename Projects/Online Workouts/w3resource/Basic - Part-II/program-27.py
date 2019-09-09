#!/usr/bin/env  python3

###########################################################################
#                                                                         #
#       Program purpose: Determines if a list of integer is an Arithmetic #
#                        or Geometric progression.
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>            #
#       Creation Date  : September 9, 2019                                #
#                                                                         #
###########################################################################

def ap_gp_sequence(data=None):
    if data is None:
        data = []
    if data[0] == data[1] == data[2] == 0:
        return {"error": "Wrong numbers"}
    else:
        if data[1] - data[0] == data[2] - data[1]:
            temp = 2 * data[2] - data[1]
            return {"seq": "AP", "next": str(temp)}
        else:
            temp = data[2] ** 2 / data[1]
            return {"seq": "GP", "next": str(temp)}

def print_info(info=None):
    if "error" in info.keys():
        print(f"{seq_a} is not AP or GP")
    else:
        print(f"{seq_a} is {info['seq']} and next value is {info['next']}")

if __name__ == "__main__":

    seq_a = [1, 2, 3]
    seq_b = [2, 6, 18]
    seq_c = [0, 0, 0]

    print_info(ap_gp_sequence(data=seq_a))
    print_info(ap_gp_sequence(data=seq_b))
    print_info(ap_gp_sequence(data=seq_c))
