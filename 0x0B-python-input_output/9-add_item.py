#!/usr/bin/python3
'''Module for task 9'''
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file('add_item.json')
except:
    data = []

save_to_json_file(data + sys.argv[1:], 'add_item.json')
