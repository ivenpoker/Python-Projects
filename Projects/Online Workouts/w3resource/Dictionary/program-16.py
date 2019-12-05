#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Gets a dictionary from an object's fields.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 05, 2019.                                                #
#                                                                                          #
############################################################################################

class DictObj:

    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'

    def do_something(self):
        pass

if __name__ == "__main__":
    test = DictObj()
    print(f'Dictionary data -> {test.__dict__}')