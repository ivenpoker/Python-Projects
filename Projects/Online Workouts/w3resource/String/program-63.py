#!/usr/bin/env  python3

###########################################################################################
#                                                                                         #
#       Program purpose: Removes trailing zeroes in an IP address.                        #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                            #
#       Creation Date  : October 30, 2019                                                 #
#                                                                                         #
###########################################################################################

def obtain_user_ip_address(input_mess: str) -> str:
    is_valid, user_ip = False, ''
    while is_valid is False:
        try:
            user_ip = input(input_mess)
            if len(user_ip) == 0:
                raise ValueError('Please, enter an IP address to work with')
            is_valid = True                                         # we're not truly validating the IP
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_ip

def remove_zeros_from_ip(ip_add):
    new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
    return new_ip_add

if __name__ == "__main__":
    main_ip = obtain_user_ip_address(input_mess='Enter an IP address: ')
    print(f'New IP address is: {remove_zeros_from_ip(ip_add=main_ip)}')
