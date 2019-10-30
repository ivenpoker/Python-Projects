#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Find all the common characters in lexicographical order from      #
#                        two given lower case strings. If there are no common letters      #
#                        print “No common characters".                                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : October 30, 2019                                                  #
#                                                                                          #
############################################################################################

from collections import Counter

def find_common_chars(str1: str, str2: str) -> dict:
    data = {'found': False, 'info': ''}
    d1 = Counter(str1)
    d2 = Counter(str2)
    common_dict = d1 & d2

    if len(common_dict) == 0:
        data['info'] = 'No common characters'
        return data

    data['found'] = True
    # list of common elements
    common_chars = list(common_dict.elements())
    common_chars = sorted(common_chars)

    data['data'] = ''.join(common_chars)

    return data

if __name__ == "__main__":
    str1 = 'Python'
    str2 = 'PHP'
    data_info = find_common_chars(str1=str1, str2=str2)
    if data_info['found']:
        print(f"Two strings: '{str1}' and '{str2}': {data_info['data']}")
    else:
        print(f"Two strings: '{str1}' and '{str2}': {data_info['info']}")

    str1 = 'Java'
    str2 = 'PHP'
    data_info = find_common_chars(str1=str1, str2=str2)
    if data_info['found']:
        print(f"Two strings: '{str1}' and '{str2}': {data_info['data']}")
    else:
        print(f"Two strings: '{str1}' and '{str2}': {data_info['info']}")
