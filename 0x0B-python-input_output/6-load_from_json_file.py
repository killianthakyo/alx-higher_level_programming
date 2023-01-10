#!/usr/bin/python3
"""
Return the JSON representation of an object
"""


import json


def def load_from_json_file(filename):
    """
    Return JSON representation
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        my_obj = json.load(f)
    return my_onj
