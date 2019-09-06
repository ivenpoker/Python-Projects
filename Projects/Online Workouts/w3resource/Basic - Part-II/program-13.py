#!/usr/bin/env  python3

########################################################################
#                                                                      #
#       Program purpose: Get all possible two digit letter combination #
#                        from a digit.
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>         #
#       Creation Date  : September 6, 2019                             #
#                                                                      #
########################################################################

def letter_combinations(digits):
    if digits == "":
        return []

    string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

if __name__ == "__main__":
    digit_string = "47"
    print(letter_combinations(digit_string))
    digit_string = "29"
    print(letter_combinations(digit_string))
