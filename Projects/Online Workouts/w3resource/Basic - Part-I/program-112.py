# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Removes the first item for specified list.                   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : September 1, 2019                                            #
#                                                                                     #
#######################################################################################

def random_list(size=10):
    return list(range(size))

def remove_first(someList=[]):
    if len(someList) is 0:
        return []

    return someList[1:]

if __name__ == "__main__":
    rand_list = random_list(20)
    print(f"Original list: {rand_list}")
    print(f"Updated list : {remove_first(someList=rand_list)}")