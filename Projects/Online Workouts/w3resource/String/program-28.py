#!/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Add a prefix text to all the lines in a string.              #
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
    text_without_indentation = textwrap.dedent(sample_text)
    wrapped = textwrap.fill(text_without_indentation, width=50)
    final_result = textwrap.indent(wrapped, '> ')

    print(f'\n{final_result}\n')
