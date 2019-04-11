#!/usr/bin/env      python3


def capitalize(_names):
    name_list = _names.split(' ')
    fst_name  = list(str(name_list[0]))
    snd_name  = list(str(name_list[1]))

    fst_name[0] = str.upper(fst_name[0])
    snd_name[0] = str.upper(snd_name[0])

    return ''.join(fst_name) + " " + ''.join(snd_name)

def main():
    data = capitalize(input("Enter your name: "))
    print("After capitalizing: %s" % data)

if __name__ == '__main__':
    print("\n============[ PROGRAM: Capitalize a person names (2) ]==========")
    main()