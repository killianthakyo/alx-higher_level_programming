#!/usr/bin/python3
"""
Add all arguments to a Python list, then save them to a file
"""
import json
import sys


filename = "add_item.json"
myArgs = sys.argv
myArgs = myArgs[1:]
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
save_to_json_file(myArgs, filename)
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_list = load_from_json_file(filename)
