#!/usr/bin/env  python3

##################################################################################
#                                                                                #
#       Program purpose: Finds a replace the string "Python" with "Java" and the #
#                        string "Java" with "Python".                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                   #
#       Creation Date  : September 22, 2019                                      #
#                                                                                #
##################################################################################

def read_string(mess: str):
    valid = False
    user_str = ""
    while not valid:
        try:
            user_str = input(mess).strip()
            valid = True
        except ValueError as ve:
            print(f"[ERROR]: {ve}")
    return user_str

def swap_substr(main_str: str, sub_a: str, sub_b: str):
    if main_str.index(sub_a) >= 0 and main_str.index(sub_b) >= 0:
        i = 0
        while i < len(main_str):
            temp_str = main_str[i:i + len(sub_a)]
            if temp_str == sub_a:
                main_str = main_str[0:i] + sub_b + main_str[i+len(sub_a):]
            else:
                temp_str = main_str[i:i + len(sub_b)]
                if temp_str == sub_b:
                    main_str = main_str[0:i] + sub_a + main_str[i+len(sub_b):]
            i += 1
    return main_str

if __name__ == "__main__":

    data = read_string(mess="Enter some string with 'Python' and 'Java': ")
    print(f"Processed string is: {swap_substr(main_str=data, sub_a='Python', sub_b='Java')}")
