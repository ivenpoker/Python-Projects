# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Count number of specific characters in a string.             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
#                                                                                     #
#######################################################################################

def find_count(char='', string=""):
    count = 0
    for x in range(len(string)):
        if string[x] == char:
            count += 1
    return count

if __name__ == "__main__":
    user_str = str(input("Enter a sentence: "))
    key_char = str(input("Enter a search character: "))

    while len(key_char) is not 1:
        key_char = str(input("Enter a SINGLE search character: "))

    cnt = find_count(char=key_char, string=user_str)
    print(f"Number of '{key_char}' in string is: {cnt}")


