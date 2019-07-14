#!/usr/bin/env python3

"""
    Program Purpose: Gets two names from console and prints greetings
    Program Author : Happi Yvan
    Author  email  : ivensteinpoker@gmail.com
"""
def main():
    first_name = input("\n\tEnter first name: ")
    last_name = input("\tEnter last name : ")
    print("\tHello %s %s! You just delved into Python" % (first_name, last_name))


if __name__ == "__main__":
    print("\n\t==========[ PROGRAM: Get names and display message ]========")
    main()