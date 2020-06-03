#!/usr/bin/python3
'''Module for task 13'''


class Student:
    '''Defines a student'''

    def __init__(self, first_name, last_name, age):
        '''Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''JSON representation of an instance'''
        if not attrs:
            return self.__dict__

        attrs_dict = {}
        for att in self.__dict__:
            if att in set(attrs):
                attrs_dict[att] = self.__dict__[att]

        return attrs_dict

    def reload_from_json(self, json):
        '''Replaces all attributes by a json dict'''
        for att in json:
            if att in set(self.__dict__.keys()):
                self.__dict__[att] = json[att]
