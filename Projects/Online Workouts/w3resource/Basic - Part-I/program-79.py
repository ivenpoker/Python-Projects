# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Get the size of an object in bytes.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import sys
    str1 = "one"
    str2 = "four"
    str3 = "three"

    print()

    print(f"Memory size of {str1}: {str(sys.getsizeof(str1))} bytes")
    print(f"Memory size of {str2}: {str(sys.getsizeof(str2))} bytes")
    print(f"Memory size of {str3}: {str(sys.getsizeof(str3))} bytes")

    print()
