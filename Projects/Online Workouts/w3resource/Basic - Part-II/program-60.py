#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Cut out words of 3 to 6 characters of length from a given   #
#                        sentence not more than 1024 characters.                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def get_sentence(mess: str, max_size: int):
    data = input(mess)
    if len(data) > max_size:
        raise TypeError(f"Max sentence size exceeded [{max_size}]")

    # remove punctuations
    data = data.replace(",", " ")
    data = data.replace(".", " ")
    return data

if __name__ == "__main__":
    main_data = get_sentence(mess="Enter a sentence (1024 characters. max.): ",
                             max_size=1024)
    print("3 to 6 characters length of words: ", end='')
    print(*[datum for datum in main_data.split() if 3 <= len(datum) <= 6])
