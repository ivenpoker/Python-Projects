#########################################################################################
#                                                                                       #
#       Program purpose: Find the first repeated character of a given string where the  #
#                        index of first occurrence is smallest.                         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 25, 2019                                               #
#                                                                                       #
#########################################################################################

def find_repeated_char_smallest_distance(main_data: str):
    temp = {}
    for ch in main_data:
        if ch in temp:
            return ch
        else:
            temp[ch] = 0
    return 'None'

if __name__ == "__main__":
    test_data, i = ['abcabc', 'abbcabc', 'abcbabc', 'abcxxy', 'abc'], 0
    for test in test_data:
        print(f"Test #{i} with data '{test}': {find_repeated_char_smallest_distance(main_data=test)}")
