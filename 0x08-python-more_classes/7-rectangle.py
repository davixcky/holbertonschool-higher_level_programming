#!/usr/bin/python3
'''Class rectangle'''


class Rectangle:
    '''Form'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        '''Destructor'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''Calculate the area of a rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate the perimeter of a rectangle'''
        w, h = self.__width, self.__height

        if w == 0 or h == 0:
            return 0

        return (w * 2) + (h * 2)

    def __str__(self):
        '''Rectangle like a string'''
        w, h = self.__width, self.__height
        s = self.print_symbol
        return '{}{}'.format((str(s) * w + '\n') * (h - 1), str(s) * w)

    def __repr__(self):
        '''Representation of the rectangle'''
        w, h = self.__width, self.__height
        return 'Rectangle({}, {})'.format(w, h)
