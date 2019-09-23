#!/usr/bin/env  python3

####################################################################################
#                                                                                  #
#       Program purpose: Simple hangman game simulation.                           #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                     #
#       Creation Date  : September 23, 2019                                        #
#                                                                                  #
####################################################################################

import random

def get_filename(mess: str):
    valid = False
    filepath = ""
    while not valid:
        try:
            filepath = str(input(mess).strip())
            valid = True
        except ValueError as ve:
            print(f"[WARNING]: {ve}")

        except RuntimeError as re:
            print(f"[ERROR]: {re}")
    return filepath

def load_data(filename: str):
    data_lines = []
    load_validated = False

    while not load_validated:
        try:
            data = open(file=filename, mode="r")
            for line in data.readlines():
                data_lines.append(line)
            load_validated = True
        except FileNotFoundError as fileNotFound:
            print(f"[FILE_NOT_FOUND]: {fileNotFound}")
            filename = get_filename(mess="Enter new VALID file name: ")

    return data_lines

def process_data(file_data: list):
    if str(type(file_data)).index("list", 0) < 0:
        raise ValueError("Invalid argument. Expected list.")
    main_tokens = []
    for line in file_data:
        temp_data = line.strip().split(" ")
        for temp in temp_data:
            if temp not in main_tokens:
                main_tokens.append(temp)
    return main_tokens

def get_random_word(list_data: list):
    rand_ind_track = []
    found = False

    # while we've not found a valid word and the number of
    # 'invalid' words in sequence isn't same as those in index track list (of invalid words)
    # we keep on searching...

    while not found and len(rand_ind_track) != len(list_data):
        rand_ind = random.choice(seq=range(len(list_data)))
        while rand_ind in rand_ind_track:
            rand_ind = random.choice(seq=range(len(list_data)))

        # check if the word, at the random index in array is valid
        if is_valid_word(some_str=list_data[rand_ind]):
            return list_data[rand_ind]          # we've found a 'valid' 'word' to use, we return it.
        else:
            rand_ind_track.append(rand_ind)     # keep track of the index that contain the 'invalid' word.

    return ""  # returning an empty string is a way of saying, NO 'word' could was found.

def is_valid_word(some_str: str):
    temp_cnt = 0
    for char in some_str:
        if str.isalpha(f"{char}"):
            temp_cnt += 1
        else:
            break
    return temp_cnt == len(some_str)

if __name__ == "__main__":

    file_path = get_filename(mess="Enter file path with words to use for hangman game: ")
    print(f"{'-' * 35}")
    print("   Loading data ... ", end='')
    loaded_data = load_data(filename=file_path)
    print(f"[DONE]")

    print("Processing data ... ", end='')
    new_data = process_data(file_data=loaded_data)
    print("[DONE]")

    print("Setting up game ... ", end='')
    random_word = get_random_word(new_data)
    print("[DONE]")


    print(f"{'-' * 35}")

    rand_word = get_random_word(list_data=new_data)
    if len(rand_word) == 0:
        print(f"Game initialization FAILURE! Please try different file.")
    else:
        print(f"Computer Has guessed a random word from file. Find it!")
        print(f"{'-' * 35}")

        user_trial_list = list('_' * len(rand_word))
        num_chars_found = 0
        num_trials = 1
        while num_chars_found < len(rand_word):
            print(f"[Trial #{num_trials}] Enter a character to get word right {user_trial_list}: ", end="")
            try:
                char = str(input().strip())[0]
            except IndexError as ind_err:

                # If the user pressed enter without providing data.
                # we ignore the input and re-demand for a character for this trial.
                print(f"Please, provide a character input")
                continue

            if char in user_trial_list:

                # This character that the user has guessed, was already found by him/her/it.
                # So, we don't consider it as a found character but as a trial.
                num_trials += 1
                continue                        # user has already found this character.

            if char in rand_word:
                char_ind = []

                # we find the indices in which user character, occurs in original
                # computer generated (guessed) word.

                for x in range(len(rand_word)):
                    if rand_word[x] == char:
                        char_ind.append(x)

                # Now we've got to use those indices generated above to place the
                # character in it's rightful positions.

                for x in char_ind:
                    user_trial_list[x] = char
                num_chars_found += 1

                if num_chars_found == len(rand_word):
                    break
            num_trials += 1

        print(f"You've finally found the word '{rand_word}' after {num_trials} trial(s)! Congrats!")
