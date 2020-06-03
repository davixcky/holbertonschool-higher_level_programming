#!/usr/bin/python3
'''Module for task 1'''


def number_of_lines(filename=""):
    '''Returns numbers of lines of a file'''
    with open(filename) as f:
        return len(f.readlines())
