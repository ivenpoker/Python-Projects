# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Convert the distance (in feet) to inches, yards, and miles.  #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 10, 2019                                              #
#                                                                                     #
#######################################################################################

def get_inches_yards_and_miles(feet):
    return [feet * 12, feet / 3.0, feet / 5280.0]

if __name__ == "__main__":
    dist_feet = int(input("Input distance in feet: "))
    data = get_inches_yards_and_miles(dist_feet)

    print(f"The distance in inches is {data[0]} inches.")
    print(f"The distance in yards is {data[1]} yards.")
    print(f"The distance in miles is {data[2]} miles.")