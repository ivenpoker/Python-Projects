#!/usr/bin/env  python3

###################################################################################
#                                                                                 #
#       Program purpose: Computes the number of days between 2 different dates    #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                    #
#       Creation Date  : 19/04/2019                                               #
#                                                                                 #
###################################################################################

def main():
    from datetime import date
    f_date = date(2014, 7, 2)           # random data
    l_date = date(2014, 7, 11)          # random data
    date_diff = l_date - f_date
    print("Days difference: {}".format(date_diff.days))

if __name__ == '__main__':
    main()