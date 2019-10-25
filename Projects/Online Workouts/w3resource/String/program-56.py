#########################################################################################
#                                                                                       #
#       Program purpose: Find the second most repeated word in a given string.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 25, 2019                                               #
#                                                                                       #
#########################################################################################

def get_user_data(input_mess: str):
    is_valid, user_data = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please a sentence to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def obtain_2nd_most_repeated_word(main_str: str):
    data = dict()
    main_str = main_str.split()
    for word in main_str:
        if word in data:
            data[word] += 1
        else:
            data[word] = 1
    counts_x = sorted(data.items(), key=lambda kv: kv[1])
    return counts_x[-2]

if __name__ == "__main__":
    main_data = get_user_data(input_mess='Enter some sentence: ')
    print(f'Second most repeated word in string: {obtain_2nd_most_repeated_word(main_str=main_data)}')