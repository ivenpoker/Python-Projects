# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Finds the available built-in modules.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 27, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    import sys
    import textwrap

    module_name = ', '.join(sorted(sys.builtin_module_names))
    print(f"{textwrap.fill(module_name, width=70)}")