#!/usr/bin/python3
"""
Add all arguments to a Python list, then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    """
    Save to file
    """
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []


    for item in args:
        my_list.append(item)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
