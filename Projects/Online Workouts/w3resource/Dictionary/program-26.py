#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Counts the values associated with key in dictionary.              #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 10, 2019                                                 #
#                                                                                          #
############################################################################################

student = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

if __name__ == "__main__":
    print(f'Number of students that succeeded: ', end='')
    print(sum(d['success'] for d in student))
