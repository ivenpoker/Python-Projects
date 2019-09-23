#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Sums all numerical values (positive integers) embedded    #
#                        in a sentence.                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 23, 2019                                        #
#                                                                                  #
####################################################################################

def read_data(mess: str):
    valid = False
    data = ""
    while not valid:
        try:
            data = str(input(mess).strip())
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return data

def process_sum(data: str):
    data_tokens = data.split(" ")
    data_num = []

    for x in range(len(data_tokens)):
        try:
            temp_int = float(data_tokens[x])
            data_num.append(temp_int)
        except ValueError as ve:
            #print(f"[ERROR]: Not a number -> {data_tokens[x]}")
            1

    return {"sum": sum(data_num), "nums": data_num}


if __name__ == "__main__":
    main_data = read_data(mess="Enter some text to process: ")
    dict_info = process_sum(data=main_data)
    print(f"List of numbers in text: {dict_info['nums']}")
    print(f" Sum of numbers in text: {dict_info['sum']}")
