#!/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Prints an examination date from a tuple to the console   #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : 19/04/2019                                               #
#                                                                                 #
###################################################################################

def main():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from: %d/%d/%d" % exam_st_date)

if __name__ == "__main__":
    main()