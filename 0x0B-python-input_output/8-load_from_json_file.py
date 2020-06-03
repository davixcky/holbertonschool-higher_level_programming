#!/usr/bin/python3
'''Module for task 8'''
import json


def load_from_json_file(filename):
    '''Return an object from a json'''
    with open(filename) as f:
        file_data = f.read()
        return json.loads(file_data)
