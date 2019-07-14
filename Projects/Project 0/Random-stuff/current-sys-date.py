#!/usr/bin/env python3

#: Program Purpose: Displays the current system date and time to the console.
#:
#: Program Author : Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date   : 11/04/2019 (mm/dd/yyyy)

import datetime

def main():
    now = datetime.datetime.now()
    print("Current date and time: ", end="")
    print(now.strftime("%H:%M:%S %Y-%m-%d"))

if __name__ == '__main__':
    main()