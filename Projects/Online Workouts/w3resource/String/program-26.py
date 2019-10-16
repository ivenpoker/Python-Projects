#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Display formatted text (width=50) as output.                 #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 16, 2019                                             #
#                                                                                     #
#######################################################################################

import textwrap

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''

if __name__ == "__main__":
    print(textwrap.fill(sample_text, width=50))