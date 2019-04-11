#!/usr/bin/env   python3

#: Program Purpose:
#:      Reads an integer N, prints 123....N
#:
#: Program Author: Happi Yvan <ivensteinpoker@gmail.com>
#: Program Date  : 11/04/2019 (mm/dd/yyyy)



def process(intVal):
    for x in range(intVal):
        print(x+1, end="")

def main():
    val = int(input())
    process(val)

if __name__ == '__main__':
    main()
