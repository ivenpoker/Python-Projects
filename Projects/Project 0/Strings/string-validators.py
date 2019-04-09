#!/usr/bin/env  python3


def process(_str):
        print(any(c.isalnum() for c in _str))
        print(any(c.isalpha() for c in _str))
        print(any(c.isdigit() for c in _str))
        print(any(c.islower() for c in _str))
        print(any(c.isupper() for c in _str))

def main():
    user_str = input("Enter a string: ")
    process(user_str)

if __name__ == "__main__":
    print("\n\t==========[ PROGRAM: Validate string ]========")
    main()