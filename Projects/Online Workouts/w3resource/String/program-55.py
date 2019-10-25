#########################################################################################
#                                                                                       #
#       Program purpose: Find the first repeated word in a given string.                #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                          #
#       Creation Date  : October 25, 2019                                               #
#                                                                                       #
#########################################################################################

def get_user_data(input_mess: str):
    is_valid, user_data  = False, ''
    while is_valid is False:
        try:
            user_data = input(input_mess)
            if len(user_data) == 0:
                raise ValueError('Please enter some string to work with')
            is_valid = True
        except ValueError as ve:
            print(f'[ERROR]: {ve}')
    return user_data

def find_first_repeated_word(main_str: str):
    main_str = main_str.split(' ')
    data = {}
    for word in main_str:
        if word in data:
            data[word] += 1
        else:
            data[word] = 1
    temp = [k for (k, v) in zip(data.keys(), data.values()) if v >= 2]
    return None if len(temp) == 0 else temp[0]

if __name__ == "__main__":
    main_data = get_user_data(input_mess='Enter some string: ')
    print(f'First repeated word: {find_first_repeated_word(main_str=main_data)}')

    # other test
    test_data, i = ["ab ca bc ab", "ab ca bc ab ca ab bc", "ab ca bc ca ab bc", "ab ca bc"], 1
    for test in test_data:
        print(f"Test #{i} for '{test}': {find_first_repeated_word(main_str=test)}")
        i += 1
