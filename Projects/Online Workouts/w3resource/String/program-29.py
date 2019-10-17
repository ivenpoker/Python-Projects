#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Set the indentation to the first line.                       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : October 17, 2019                                             #
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
    text1 = textwrap.dedent(sample_text).strip()
    print()
    print(textwrap.fill(text1, initial_indent='', subsequent_indent=' '*4, width=80))
    print()