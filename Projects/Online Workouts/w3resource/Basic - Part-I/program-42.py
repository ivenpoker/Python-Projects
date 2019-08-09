# !/usr/bin/env  python3

#####################################################################################
#                                                                                   #
#       Program purpose: Checks if the shell on which this program is run is        #
#                        x64 (64-bit) or x32 (32bit).                               #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                      #
#       Creation Date  : August 9, 2019                                             #
#                                                                                   #
#####################################################################################

def getInfo():
    import struct
    if struct.calcsize("P") * 8 == 32:
        return "32 bit"
    elif struct.calcsize("P") * 8 == 64:
        return "64 bit"
    else:
        return "Unknown"   # This is really weird....

if __name__ == "__main__":
    print(f"Shell is: {getInfo()}")
