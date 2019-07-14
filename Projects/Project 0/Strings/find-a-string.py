#!/usr/bin/env python3

"""
    Program Purpose: Finds the number of occurrences of a substring in a string
    Program Author : Happi Yvan
    Author  email  : ivensteinpoker@gmail.com
"""
def count_substring(main_str, substr):
    cnt = 0
    for ind in range(len(main_str)):
        if main_str[ind] == substr[0]:
            if main_str[ind: (ind + len(substr))] == substr:
                cnt += 1
    return cnt


def main():
    user_str = input("\n\tEnter a string: ").strip()
    substr   = input("\tEnter substring: ").strip()
    print("\tOccurrences of '%s' in '%s': %d\n"
          % (substr, user_str, count_substring(user_str, substr)))

if __name__ == "__main__":
    print("\n\t========[ PROGRAM: Count the occurrences of substring in string ]========")
    main()