#!/usr/bin/python3
'''Module for task 14'''


def pascal_triangle(n):
    '''Calculate n triangle pascal'''
    pascal = []
    for line in range(1, n + 1):
        r = [1]

        for i in range(1, line):
            r.append(int(r[i - 1] * (line - i) / i))

        pascal.append(r)

    return pascal if pascal is not [] else [[]]
