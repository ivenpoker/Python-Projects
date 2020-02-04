#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Makes a chain of function decorators (bold, italic, underline     #
#                        etc).                                                             #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : February 01, 2020                                                 #
#                                                                                          #
############################################################################################

def make_bold(fn):
    def wrapped():
        return f'<b> {fn()} </b>'
    return wrapped

def make_italic(fn):
    def wrapped():
        return f'<i> {fn()} </i>'
    return wrapped

def make_underline(fn):
    def wrapped():
        return f'<u> {fn()} </u>'
    return wrapped

@make_bold
@make_italic
@make_underline
def hello():
    return 'hello world'

if __name__ == "__main__":
    print(hello())
