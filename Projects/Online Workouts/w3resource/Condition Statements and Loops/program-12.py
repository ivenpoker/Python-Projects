#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Accepts a sequence of lines (blank line to terminate) as input    #
#                        and prints the lines as output (all characters in lower case)     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 21, 2019                                                  #
#                                                                                          #
############################################################################################

def obtain_user_lines(input_mess: str) -> list:
    user_lines, stop = [], False
    while not stop:
        try:
            temp_line = input(input_mess)
            if len(temp_line) == 0:
                stop = True
            else:
                user_lines.append(temp_line)
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_lines

def display_lines(main_lines: list) -> None:
    for line in main_lines:
        print(str(line).lower())


if __name__ == "__main__":

    lines = obtain_user_lines(input_mess='Enter a message for line: ')
    print('-' * 30)
    display_lines(main_lines=lines)
