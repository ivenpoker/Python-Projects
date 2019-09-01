# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Input a number, if not number, generate error message.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    try:
        userInput = int(input("Enter some integer: "))
        print(f"Your integer: {userInput}")
    except ValueError as valErr:
        print(f"That was not a number. Try again...")
