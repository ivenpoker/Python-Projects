#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: When character are consecutive in a string , it is          #
#                        possible to shorten the character string by replacing the   #
#                        character with a certain rule. For example, in the case     #
#                        of the character string YYYYY, if it is expressed as # 5 Y, #
#                        it is compressed by one character. Python program to        #
#                        restore the original string by entering the compressed      #
#                        string with this rule. However, the # character does not    #
#                        appear in the restored character string.                    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : September 23, 2019                                          #
#                                                                                    #
######################################################################################

def read_data(mess: str):
    valid = False
    main_data = ""
    while not valid:
        try:
            main_data = str(input(mess).strip())
            valid = True
        except (ValueError, RuntimeError) as ve:
            print(f"[ERROR]: {ve}")
    return main_data

def uncompress_data(comp_data: str):
    list_data = []
    x = 0
    while x < len(comp_data):
        if comp_data[x] == '#':
            temp = comp_data[x+2] * int(comp_data[x+1])
            list_data.append(temp)
            x += 3
        else:
            list_data.append(comp_data[x])
            x += 1
    return ''.join(list_data)

if __name__ == "__main__":
    data = read_data(mess="Enter some compressed text: ")
    print(f"Uncompressed data: {uncompress_data(comp_data=data)}")
