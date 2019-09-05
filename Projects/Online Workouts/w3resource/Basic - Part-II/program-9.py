#!/usr/bin/env  python3

###############################################################################
#                                                                             #
#       Program purpose: Get a list of locally installed Python modules.      #                                                            #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                #
#       Creation Date  : September 5, 2019                                    #
#                                                                             #
###############################################################################

import pkg_resources

if __name__ == "__main__":

    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                      for i in installed_packages])
    for m in installed_packages_list:
        print(m)
