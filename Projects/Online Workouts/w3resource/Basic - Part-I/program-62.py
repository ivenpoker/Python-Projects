# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Converts all units of time into seconds.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 15, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    days = int(input("Input days: ")) * 3600 * 24
    hours = int(input("Input hours: ")) * 3600
    minutes = int(input("Input minutes: ")) * 60
    seconds = int(input("Input seconds: "))

    time = days + hours + minutes + seconds

    print(f"The amount of seconds: {time}")

