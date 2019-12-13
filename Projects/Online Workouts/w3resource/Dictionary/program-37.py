#!/usr/bin/env  python3

############################################################################################
#                                                                                          #
#       Program purpose: Replaces a certain dictionary values with their average.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                             #
#       Creation Date  : December 13, 2019                                                 #
#                                                                                          #
############################################################################################

def do_process_list_data(some_data: list, to_check: list) -> list:
    temp_sum = 0
    new_list_data = []
    for data in some_data:
        cnt, new_dict = 0, {}
        for (k, v) in zip(data.keys(), data.values()):
            if k in to_check:
                temp_sum += v
                cnt += 1
            else:
                new_dict[k] = v
        if cnt > 0:
            new_dict['+'.join(to_check)] = float(temp_sum / len(to_check))
        new_list_data.append(new_dict)
        temp_sum = 0

    return new_list_data



if __name__ == "__main__":
    main_data = [
        {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
        {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
        {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86},
    ]
    print(f'Original list data: {main_data}')
    print('-' * 168)
    print(f'After processing data: {do_process_list_data(some_data=main_data, to_check=["V", "VI"])}')