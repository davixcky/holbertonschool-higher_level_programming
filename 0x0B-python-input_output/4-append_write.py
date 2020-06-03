#!/usr/bin/python3
'''Module for task 4'''


def append_write(filename="", text=""):
    '''Append text to a file'''
    with open(filename, 'a') as f:
        return f.write(text)
