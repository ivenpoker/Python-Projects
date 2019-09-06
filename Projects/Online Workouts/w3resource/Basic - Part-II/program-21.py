#!/usr/bin/env  python3

##########################################################################
#                                                                        #
#       Program purpose: Finds the number of notes in a number.          #
#       Program Author : Happi Yvan <ivensteinpoker@gmail.com>           #
#       Creation Date  : September 6, 2019                               #
#                                                                        #
##########################################################################

def find_notes(num, notes=[]):
    if notes is None or len(notes) == 0:
        return {}
    data = {}
    notes = sorted(notes, reverse=True)

    for note in notes:
        while num >= note:
            if str(note) in data.keys():
                data[str(note)] += 1
            else:
                data[str(note)] = 1
            num -= note
    return data


if __name__ == "__main__":

    cont = True
    main_amount = 0

    while cont:
        try:
            main_amount = int(input("Enter main amount: "))
            cont = False
        except ValueError as ve:
            print("Invalid input. Try again")

    new_data = find_notes(num=main_amount, notes=[10, 20, 50, 100, 200, 500])
    print(f"Data: {new_data}")

