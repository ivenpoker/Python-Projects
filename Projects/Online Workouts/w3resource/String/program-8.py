#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Given a list of words, program finds the word with the       #
#                        largest length.                                              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 11, 2019                                             #
#                                                                                     #
#######################################################################################


def find_largest_string(list_data: list):
    big_str = ''
    for temp_str in list_data:
        if len(temp_str) > len(big_str):
            big_str = temp_str[:]
    return big_str

if __name__ == "__main__":

    main_data = "It is a long established fact that a reader will be distracted by the readable content of a page" \
                " when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal " \
                "distribution of letters, as opposed to using 'Content here, content here', making it look like " \
                "readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as" \
                " their default model text, and a search for 'lorem ipsum' will uncover many web sites still in " \
                "their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on" \
                " purpose (injected humour and the like)."
    print(f'String with longest length: {find_largest_string(list_data=main_data.split())}')

