#!/usr/bin/env          python3

#: Program Purpose: See https://www.hackerrank.com/challenges/nested-list/submissions/code/94724341
#: Program Author : Happi Yvan <ivenstienpoker@gmail.com>
#: Program Date   : 11/04/2019

def score(_stud):
    return _stud[-1]

def name(_stud):
    return str.lower(_stud[0])

def main():
    studs = []
    n = int(input())
    for _v in range(n):
        _tmp_stud = [input(), float(input())]
        studs.append(_tmp_stud)

    _new_list = sorted(studs, key=score)
    _low_val = [_new_list[0]]
    _found = False

    for _x in range(len(_new_list)):
        if _new_list[_x][1] > _low_val[0][1] and not _found:
            _low_val.pop(0)
            _low_val.append(_new_list[_x])
            _found = True
        if _found and _new_list[_x][1] == _low_val[0][1] \
                and _new_list[_x][0] != _low_val[0][0]:
            _low_val.append(_new_list[_x])

    _low_val = sorted(_low_val, key=name)
    for _x in _low_val:
        print(_x[0])

if __name__ == "__main__":
    main()
