# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Concatenates N-strings.                                      #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
#                                                                                     #
#######################################################################################

def read_strs(max_cnt=0):
    strings = []
    tmp = 1
    while tmp is not max_cnt+1:
        tmp_str = str(input(f"Enter string #{tmp}: "))
        strings.append(tmp_str)
        tmp += 1
    return strings

if __name__ == "__main__":
    num_str = int(input("Enter number of strings: "))
    strs = read_strs(num_str)
    print(f"\nStrings are: {strs}")

    # joining strings on '-'
    print(f"Concatenated strings: {'-'.join(strs)}")
