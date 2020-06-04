#!/usr/bin/python3
'''Module for task 14'''


def pascal_triangle(n):
    '''Calculate n triangle pascal'''
    a = []
    for i in range(n):
        a.append([])
        a[i].append(1)

        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])

        if(len(a) > 1):
            a[i].append(1)

    return a
