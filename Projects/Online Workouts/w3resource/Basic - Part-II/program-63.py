#!/usr/bin/env  python3

######################################################################################
#                                                                                    #
#       Program purpose: Adds up columns and rows of given table (matrix).           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                       #
#       Creation Date  : October 10, 2019                                            #
#                                                                                    #
######################################################################################

def sum_list(data: list):
    temp_sum = 0
    for x in data:
        temp_sum += int(x)
    return temp_sum

def print_rows_sum(main_data: list):
    i = 1
    for row in main_data:
        print(f'Row #{i}: ', end='')
        for x in row:
            print(f'{x} ', end='')
        print(f' --> [{sum_list(data=row)}]')

def print_cols_sum(main_data: list, max_cols: int):
    for x in range(max_cols):
        print(f'Column #{x} sum: ', end='')
        temp_sum = 0
        for row in main_data:
            temp_sum += int(row[x])
        print(f'{temp_sum}')

def get_matrix_data():
    rows = int(input('Enter number of rows: '))
    cols = int(input('Enter number of cols: '))

    print('-' * 25)

    main_data = []

    for x in range(rows):
        try:
            data = list(input(f'Enter row #{x} [{cols} entries]: ').split())
            while len(data) != cols:
                data = list(input(f'Enter row #{x} [{cols} ENTRIES]: ').split())
            main_data.append(data)
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return {'matrix': main_data, 'rows': rows, 'cols': cols}

def process_matrix(matrix_data: dict):
    print_rows_sum(main_data=matrix_data['matrix'])
    print('-' * 25)
    print_cols_sum(main_data=matrix_data['matrix'], max_cols=matrix_data['cols'])


if __name__ == "__main__":
    matrix = get_matrix_data()
    print('-' * 25)
    process_matrix(matrix_data=matrix)
