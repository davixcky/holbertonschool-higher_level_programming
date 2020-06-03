#!/usr/bin/python3
'''Module for task 11'''


class Student:
    '''Defines a student'''

    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''JSON representation of an instance'''
        return self.__dict__
