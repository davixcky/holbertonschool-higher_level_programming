#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]

    res = 0
    for i in argv:
        res = res + int(i)

    print(res)
