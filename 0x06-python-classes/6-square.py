#!/usr/bin/python3

''' Square form '''


class Square:
    ''' Class with constructor '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Constructor Square '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        t = position
        if type(t) is not tuple or len(t) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if type(t[0]) is not int or type(t[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')

        if t[0] < 0 or t[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        t = position
        if type(t) is not tuple or len(t) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if type(t[0]) is not int or type(t[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')

        if t[0] < 0 or t[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def my_print(self):
        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
