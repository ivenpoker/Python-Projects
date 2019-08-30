# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: List the special variables used within the language.         #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 30, 2019                                              #
#                                                                                     #
#######################################################################################

if __name__ == "__main__":
    s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
    print()
    print('\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)))
    print()
