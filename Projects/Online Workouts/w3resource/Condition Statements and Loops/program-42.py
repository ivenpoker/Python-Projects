#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Computes the sum and average of n integer numbers (input from the #
#                        user). Stop processing input at input 0.                          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : January 28, 2019                                                  #
#                                                                                          #
############################################################################################

def do_suming(input_mess: str) -> dict:
    user_data, cont, main_sum = '', True, 0
    count = 0
    while cont:
        try:
            user_data = int(input(input_mess))
            if user_data == 0:
                cont = False
            else:
                main_sum += user_data
                count += 1
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return dict(main_sum=main_sum, count=count)

def do_computation():

    data_info = do_suming(input_mess='Enter an integer [0 to quit]: ')
    main_sum = data_info['main_sum']
    average = data_info['main_sum'] / data_info['count']

    print('-' * 30)
    print(f' Sum is: {main_sum}')
    print(f'Average: {average}')

if __name__ == "__main__":

    do_computation()
