# !/usr/bin/env  python3

#####################################################################################
#                                                                                   #
#       Program purpose: Get the site packages for the python shell executed.       #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                      #
#       Creation Date  : August 9, 2019                                             #
#                                                                                   #
#####################################################################################

if __name__ == "__main__":
    import site
    print(f"Site-packages: {site.getsitepackages()}")