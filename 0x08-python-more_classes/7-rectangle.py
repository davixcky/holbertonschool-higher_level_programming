#!/usr/bin/python3
'''Class rectangle'''


class Rectangle:
    '''Form'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        w, h = self.__width, self.__height

        if w == 0 or h == 0:
            return 0

        return (w * 2) + (h * 2)

    def __str__(self):
        w, h = self.__width, self.__height
        s = self.print_symbol
        return '{}{}'.format((str(s) * w + '\n') * (h - 1), str(s) * w)

    def __repr__(self):
        w, h = self.__width, self.__height
        return 'Rectangle({}, {})'.format(w, h)
