#!/usr/bin/env  python 3

############################################################################################
#                                                                                          #
#       Program purpose: Counts the number of strings, where the string length is 2 or     #
#                        more and the first and last characters are same from a given list #
#                        of strings.                                                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : November 8, 2019                                                  #
#                                                                                          #
############################################################################################

def do_the_count(list_data: list) -> int:
    cnt = 0
    for item in list_data:
        if len(item) >= 2 and item[0] == item[-1]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    test_data = ['abc', 'xyz', 'aba', '1221']
    print(f'Number of matches: {do_the_count(list_data=test_data)}')
