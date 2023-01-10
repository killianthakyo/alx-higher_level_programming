#!/usr/bin/python3
"""
Return the JSON representation of an object
"""


import json
def to_json_string(my_obj):
    """
    Return JSON representation
    """
    return(json.dump(my_obj))

