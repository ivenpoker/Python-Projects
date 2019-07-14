#!/usr/bin/env  python3

#############################################################################
#                                                                           #
#       Program purpose: Prints current system date and time                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>              #
#       Creation Date  : 19/04/2019                                         #
#                                                                           #
#############################################################################

def print_date_time():
    import datetime
    now = datetime.datetime.now()
    print("Current date and time: {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))


def main():
    print_date_time()

if __name__ == "__main__":
    main()