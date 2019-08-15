# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Convert seconds to day, hour, minutes and seconds            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 15, 2019                                              #
#                                                                                     #
#######################################################################################

def get_hours(minutes):
    hours = 0
    while minutes >= 60:
        hours += 1
        minutes -= 60
    return hours

def get_minutes(seconds):
    min = 0
    while seconds >= 60:
        min += 1
        seconds -= 60
    return min

if __name__ == "__main__":
    total_secs = int(input("Enter max number of seconds: "))
    mins = get_minutes(seconds=total_secs)
    if mins * 60 == total_secs:
        total_secs = 0
    else:
        total_secs -= (mins * 60)

    hours = get_hours(mins)

    if hours * 60 == mins:
        mins = 0
    else:
        mins -= (hours * 60)

    day = 0
    while hours >= 24:
        day += 1
        hours -= 24

    print(f"Total days: {day}\nTotal hours: {hours}\nTotal minutes:"
          f" {mins}\nTotal seconds: {total_secs}")