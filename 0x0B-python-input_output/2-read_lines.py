#!/usr/bin/python3
'''Module for task 2'''


def read_lines(filename="", nb_lines=0):
    '''Reads n lines of a text file'''
    with open(filename) as f:
        for idx, line in enumerate(f):
            print(line, end="")

            if nb_lines == idx + 1:
                break
