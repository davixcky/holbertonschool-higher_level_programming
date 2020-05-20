#!/usr/bin/python3

''' Square form '''


class Square:
    ''' Class with constructor '''

    def __init__(self, size=0):
        ''' Constructor Square '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return self.__size ** 2
