# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get numbers divisible by 15 from a list using an anonymous   #
#                        function.                                                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":

    num_list = [45, 55, 60, 37, 100, 105, 220]
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print(f"Numbers divisible by 15 are: {result}")
