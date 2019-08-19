# !/usr/bin/env  python3

#######################################################################################
#                                                                                     #
#       Program purpose: Hashes a word from standard input stream                     #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>                        #
#       Creation Date  : August 19, 2019                                              #
#                                                                                     #
#######################################################################################

def hash_word(word):
    soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
    word = word.upper()

    coded = word[0]

    for a in word[1:len(word)]:
        i = 65 - ord(a)
        coded = coded + str(soundex[i])

    return coded


if __name__ == "__main__":
    user_data = input("Enter word to be hashed: ")
    print(f"Hashed word: {hash_word(user_data)}")
