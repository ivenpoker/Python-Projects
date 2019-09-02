# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Checks if there's a lowercase character in a string.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 2, 2019                                            #
#                                                                                     #
#######################################################################################

def is_lowercase_found(string=""):
    for x in string:
        if str.islower(x):
            return True
    return False

if __name__ == "__main__":
    mainString = input("Enter some string: ")
    if is_lowercase_found(mainString):
        print(f"Lowercase character FOUND in string.")
    else:
        print("Lowercase character NOT FOUND in string.")

    # we could still have used.
    # print(any(c.islower() for c in mainString))

